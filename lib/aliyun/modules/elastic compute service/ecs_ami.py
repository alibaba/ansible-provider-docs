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
module: ecs_ami
version_added: "1.0"
short_description: Create or Delete User-defined Image
description:
    - Creates or deletes User-defined Images
options:
  acs_access_key:
    description:
      - Aliyun Cloud access key. If not set then the value of the `ACS_ACCESS_KEY_ID`, `ACS_ACCESS_KEY` or `ECS_ACCESS_KEY` environment variable is used.
    required: false
    default: null
    aliases: ['ecs_access_key','access_key']
  acs_secret_access_key:
    description:
      - Aliyun Cloud secret key. If not set then the value of the `ACS_SECRET_ACCESS_KEY`, `ACS_SECRET_KEY`, or `ECS_SECRET_KEY` environment variable is used.
    required: false
    default: null
    aliases: ['ecs_secret_key','secret_key']
  region:
    description:
      - The Aliyun Cloud region to use. If not specified then the value of the `ACS_REGION`, `ACS_DEFAULT_REGION` or `ECS_REGION` environment variable, if any, is used.
    required: false
    default: null
    aliases: ['acs_region', 'ecs_region']
  status:
    description:
      - The state of the image for operating.
    required: false
    default: 'present'
    aliases: ['state']
    choices: ['present', 'absent']
  instance_id:
    description:
      - instance id of the image to create.
    required: false
    default: null
    aliases: ['instance']
  snapshot_id:
    description:
      - The snapshot ID. A user-defined image is created from the specified snapshot.
    required: false
    default: null
    aliases: ['snapshot']
  image_name:
    description:
      - The name of the image, [2, 128] English or Chinese characters.
    required: false
    default: null
    aliases: ['name']
  image_version:
    description:
      - The version number of the image, with a length limit of 1 to 40 English characters.
    required: false
    default: null
    aliases: ['version']
  description:
    description:
      - The description of the image, with a length limit of 0 to 256 characters.
    required: false
    default: null
    aliases: []
  disk_mapping:
    description:
      - An optional list of device hashes/dictionaries with custom configurations (see example).
    required: false
    default: null
    aliases: []
  images_tags:
    description:
      - A list of hash/dictionaries of image tags, '[{tag_key:"value", tag_value:"value"}]', tag_key must be not null when tag_value isn't null
    required: false
    default: null
    aliases: ['tags']
  launch_permission:
    description:
      - Users that should be able to launch the ami
    required: false
    default: null
    aliases: []
  wait:
      description:
        - Wait for the image creation.
      required: false
      default: "no"
      choices: ["yes", "no"]
  wait_timeout:
      description:
        - how long before wait gives up, in seconds
      required: false
      default: "300"
      choices: []
  image_id:
      description:
        - ID of an image. Parameter is B(required) while deleting user defined image.
      required: false
      default: null
      aliases: []

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
# provisioning to create new user-defined image
#

# basic provisioning example to create image using ecs instance
- name: create image from ecs instance
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-hongkong
    instance_id: xxxxxxxxxx
  tasks:
    - name: create image form ecs instance
      ecs_ami:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        instance_id: '{{ instance_id }}'

# basic provisioning example to create image using snapshot
- name: create image using snapshot
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-hongkong
    snapshot_id: xxxxxxxxxx
    status: present
  tasks:
    - name: create image using snapshot
      ecs_ami:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        snapshot_id: '{{ snapshot_id }}'
        status: '{{ status }}'

# basic provisioning example to create image using disk mapping
- name: create image using disk mapping
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-hongkong
    disk_mapping:
      - device: /dev/xvda
        disk_size: 5
        snapshot_id: xxxxxxxxxx
    status: present
  tasks:
    - name: create image using disk mapping
      ecs_ami:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        disk_mapping: '{{ disk_mapping }}'
        status: '{{ status }}'

# advanced example to create image with tagging, version and launch permission
- name: create image
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-hongkong
    image_name: image_test
    image_version: 4
    description: description
    images_tags:
      - tag_key: key
        tag_value: value
    disk_mapping:
      - device: /dev/xvda
        disk_size: 5
        snapshot_id: xxxxxxxxxx
    status: present
    wait: false
    wait_timeout: 10
    launch_permission: xxxxxxxxxx
  tasks:
    - name: create image
      ecs_ami:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        image_name: '{{ image_name }}'
        image_version: '{{ image_version }}'
        description: '{{ description }}'
        images_tags: '{{ images_tags }}'
        disk_mapping: '{{ disk_mapping }}'
        status: '{{ status }}'
        wait: '{{ wait }}'
        wait_timeout: '{{ wait_timeout }}'
        launch_permission: '{{ launch_permission }}'

#
# provisioning to delete user-defined image
#

# provisioning to delete user-defined image
- name: delete image
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: us-west-1
    image_id: xxxxxxxxxx
    status: absent
  tasks:
    - name: delete image
      ecs_ami:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        image_id: '{{ image_id }}'
        status: '{{ status }}'
'''