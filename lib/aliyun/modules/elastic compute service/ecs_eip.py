#!/usr/bin/python
# coding=utf-8
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
module: ecs_eip
version_added: "1.0"
short_description: Request, Bind, Unbind, Modify and Release EIP
description:
    - Request, Bind, Unbind, Modify and Release EIP
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
      - Status for requesting eip addresses, bind eip, unbind eip, modify eip attributes and release eip
    required: false
    default: present
    choices: ['present', 'join', 'absent', 'leave']
    aliases: []
  bandwidth:
    description:
      - The rate limit of the EIP
    required: false
    default: 5Mbps
    aliases: []
  internet_charge_type:
    description:
      - Internet charge type
    required: false
    default: PayByBandwidth
    aliases: []
    choices: ['PayByBandwidth', 'PayByTraffic']
  allocation_id:
    description:
      - The allocation ID of the EIP to be bound or unbound. The allocation ID uniquely identifies the EIP
    required: true
    default: null
    aliases: []
  instance_id:
    description:
      - The ID of the ECS instance to be bound or unbound
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
# Provisioning Request, Bind, Unbind and Release EIP
#

# basic provisioning example to requesting eip addresses in EIP
- name: requesting eip
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-hongkong
    internet_charge_type: PayByTraffic
    bandwidth: 5
    status: present
  tasks:
    - name: requesting eip
      ecs_eip:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        internet_charge_type: '{{ internet_charge_type }}'
        bandwidth: '{{ bandwidth }}'
        status: '{{ status }}'

# basic provisioning example to bind eip
- name: create disk
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-hongkong
    allocation_id: xxxxxxxxxx
    instance_id: xxxxxxxxxx
    status: join
  tasks:
    - name: Bind eip
      ecs_eip:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        allocation_id: '{{ allocation_id }}'
        instance_id: '{{ instance_id }}'
        status: '{{ status }}'

# basic provisioning example to unbind eip
- name: unbind eip
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-hongkong
    allocation_id: exxxxxxxxxx
    instance_id: xxxxxxxxxx
    state: leave
  tasks:
    - name: unbind eip
      ecs_eip:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        allocation_id: '{{ allocation_id }}'
        instance_id: '{{ instance_id }}'
        state: '{{ state }}'

# basic provisioning example to modifying eip
- name: modifying eip
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-hongkong
    allocation_id: xxxxxxxxxx
    bandwidth: 3
    status: present
  tasks:
    - name: Modify eip
      ecs_eip:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        allocation_id: '{{ allocation_id }}'
        bandwidth: '{{ bandwidth }}'
        status: '{{ status }}'

# basic provisioning example to release eip
- name: release eip
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-hongkong
    allocation_id: xxxxxxxxxx
    status: absent
  tasks:
    - name: release eip
      ecs_eip:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        allocation_id: '{{ allocation_id }}'
        status: '{{ status }}'
'''