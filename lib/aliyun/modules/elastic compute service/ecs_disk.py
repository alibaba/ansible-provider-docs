#!/usr/bin/python
#
# Copyright 2017 Alibaba Group Holding Limited.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible. If not, see http://www.gnu.org/licenses/.


ANSIBLE_METADATA = {'status': ['stableinterface'],
                    'supported_by': 'core',
                    'version': '1.0'}

DOCUMENTATION = '''
---
module: ecs_disk
version_added: "1.0"
short_description: Create, Attach, Detach or Delete a disk
description:
    - Create, Attach, Detach or Delete a disk
options:
  alicloud_access_key:
    description:
      - Aliyun Cloud access key. If not set then the value of the `ALICLOUD_ACCESS_KEY`, `ACS_ACCESS_KEY_ID`, `ACS_ACCESS_KEY` or `ECS_ACCESS_KEY` environment variable is used.
    required: false
    default: null
    aliases: ['acs_access_key', 'ecs_access_key', 'access_key']
  alicloud_secret_key:
    description:
      - Aliyun Cloud secret key. If not set then the value of the `ALICLOUD_SECRET_KEY`, `ACS_SECRET_ACCESS_KEY`, `ACS_SECRET_KEY`, or `ECS_SECRET_KEY` environment variable is used.
    required: false
    default: null
    aliases: ['acs_secret_access_key', 'ecs_secret_key', 'secret_key']
  alicloud_region:
    description:
      - The Aliyun Cloud region to use. If not specified then the value of the `ALICLOUD_REGION`, `ACS_REGION`, `ACS_DEFAULT_REGION` or `ECS_REGION` environment variable, if any, is used.
    required: false
    default: null
    aliases: ['region', 'acs_region', 'ecs_region']
  status:
    description:
      - The state of the instance after operating.
    required: false
    default: 'present'
    aliases: ['state']
    choices: ['present', 'absent']
  alicloud_zone:
    description:
      - Aliyun availability zone ID in which to launch the instance. Parameter is B(required) while creating disk.
    required: false
    default: null
    aliases: ['zone_id', 'availability_zone', 'acs_zone', 'ecs_zone' , 'zone']
  disk_name:
    description:
      - The value of disk name is blank by default. [2, 128] English or Chinese characters, must begin with an uppercase/lowercase letter or Chinese character. Can contain numbers, '.', '_' and '-'. The disk name will appear on the console. It cannot begin with http:// or https://.
    required: false
    default: null
    aliases: ['name']
  description:
    description:
      - The value of disk description is blank by default. [2, 256] characters. The disk description will appear on the console. It cannot begin with http:// or https://.
    required: false
    default: null
    aliases: [ 'disk_description' ]
  disk_category:
    description:
      - Category of the data disk
    required: false
    default: cloud
    aliases: ['volume_type', 'disk_type']
    choices: ['cloud', 'cloud_efficiency', 'cloud_ssd']
  size:
    description:
      - Size of the system disk, in GB.The value should be equal to or greater than the size of the specific SnapshotId. 
    required: false
    default: null
    aliases: ['volume_size', 'disk_size']
  snapshot_id:
    description:
      - Snapshots are used to create the data disk After this parameter is specified, Size is ignored. The actual size of the created disk is the size of the specified snapshot Snapshots from on or before July 15, 2013 cannot be used to create a disk
    required: false
    default: null
    aliases: ['snapshot']
  disk_tags:
    description:
      - A list of hash/dictionaries of instance tags, ['{"tag_key":"value", "tag_value":"value"}'], tag_key must be not null when tag_value isn't null
    required: false
    default: null
    aliases: ['tags']
  instance_id:
    description:
      - The specified instance ID. Parameter is B(required) while attaching disk.
    required: false
    default: null
    aliases: ['instance']
  disk_id:
    description:
      - The disk ID. The disk and Instance must be in the same zone. Parameter is B(required) while attaching disk.
    required: false
    default: null
    aliases: ['vol_id', 'id']
  device:
    description:
      - The value null indicates that the value is allocated by default, starting from /dev/xvdb to /dev/xvdz.
    required: false
    default: null
    aliases: ['device_name']
  delete_with_instance:
    description:
      - Whether or not the disk is released along with the instance. True/Yes indicates that when the instance is released, this disk will be released with it.False/No indicates that when the instance is released, this disk will be retained.
    required: false
    default: none
    aliases: ['delete_on_termination']
    choices: ["yes", "no"]
requirements:
  - "python >= 2.7"
  - aliyun-python-sdk-core, aliyun-python-sdk-ecs, ecsutils and footmark
notes:
  - If parameters are not set within the module, the following
    environment variables can be used in decreasing order of precedence
    C(ACS_ACCESS_KEY_ID) or C(ACS_ACCESS_KEY) or C(ECS_ACCESS_KEY),
    C(ACS_SECRET_ACCESS_KEY) or C(ACS_SECRET_KEY) or C(ECS_SECRET_KEY),
    C(ACS_REGION) or C(ACS_DEFAULT_REGION) or C(ECS_REGION)
'''

EXAMPLES = '''
#
# Provisioning new disk
#

# Basic provisioning example create a disk
- name: create disk
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-beijing
    alicloud_zone: cn-beijing-b
    size: 20
    status: present
  tasks:
    - name: create disk
      ecs_disk:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        alicloud_zone: '{{ alicloud_zone }}'
        size: '{{ size }}'
        status: '{{ status }}'

# Advanced example with tagging and snapshot
- name: create disk
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-hongkong
    alicloud_zone: cn-hongkong-b
    disk_name: disk_1
    description: data disk_1
    size: 20
    snapshot_id: xxxxxxxxxx
    disk_category: cloud_ssd
    status: present
  tasks:
    - name: create disk
      ecs_disk:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        alicloud_zone: '{{ alicloud_zone }}'
        disk_name: '{{ disk_name }}'
        description: '{{ description }}'
        size: '{{ size }}'
        snapshot_id: '{{ snapshot_id }}'
        disk_category: '{{ disk_category }}'
        status: '{{ status }}'

# Example to attach disk to an instance
- name: attach disk to instance
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    status: present
    alicloud_region: us-west-1
    instance_id: xxxxxxxxxx
    disk_id: xxxxxxxxxx
    device: /dev/xvdb
    delete_with_instance: false
  tasks:
    - name: Attach Disk to instance
      ecs_disk:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        status: '{{ status }}'
        alicloud_region: '{{ alicloud_region }}'
        instance_id: '{{ instance_id }}'
        disk_id: '{{ disk_id }}'
        device: '{{ device }}'
        delete_with_instance: '{{ delete_with_instance }}'

# Example to detach disk from instance
- name: detach disk
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: us-west-1
    disk_id: xxxxxxxxxx
    status: present
  tasks:
    - name: detach disk
      ecs_disk:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        id: '{{ disk_id }}'
        status: '{{ status }}'

# Example to delete disk
- name: detach disk
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: us-west-1
    disk_id: xxxxxxxxxx
    status: absent
  tasks:
    - name: detach disk
      ecs_disk:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        disk_id: '{{ disk_id }}'
        status: '{{ status }}'
'''