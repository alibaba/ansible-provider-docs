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
module: ecs_vpc
version_added: "1.0"
short_description: Create/Delete Vpc and Vswitch, Querying Vswitch and VRouter and Adding Route Entry
description:
    - Create/Delete Vpc and Vswitch, Querying Vswitch and VRouter and Adding Route Entry
options:
  acs_access_key:
    description:
      - Aliyun Cloud access key. If not set then the value of the 'ACS_ACCESS_KEY_ID', 'ACS_ACCESS_KEY'
        or 'ECS_ACCESS_KEY' environment variable is used.
    required: false
    default: null
    aliases: ['ecs_access_key', 'access_key']
  acs_secret_access_key:
    description:
      - Aliyun Cloud secret key. If not set then the value of the 'ACS_SECRET_ACCESS_KEY', 'ACS_SECRET_KEY',
        or 'ECS_SECRET_KEY' environment variable is used.
    required: false
    default: null
    aliases: ['ecs_secret_key', 'secret_key']
  region:
    description:
      - The Aliyun Cloud region to use. If not specified then the value of the 'ACS_REGION', 'ACS_DEFAULT_REGION'
        or 'ECS_REGION' environment variable, if any, is used.
    required: false
    default: null
    aliases: ['acs_region', 'ecs_region']
  status:
    description:
      - Create/delete Vpc and Vswitch, Querying Vswitch and VRouter and Adding Route Entry
    required: false
    default: 'present'
    aliases: ['state']
    choices: ['present', 'absent', 'getinfo_vroute', 'describe_vswitch']
  cidr_block:
    description:
      - The CIDR block representing the VPC, e.g. 10.0.0.0/8. Value options- 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
    required: true
    default: 172.16.0.0/16
    aliases: []
  vpc_name:
    description:
      - The VPC name. The default value is blank. [2, 128] English or Chinese characters, must begin with an uppercase/
        lowercase letter or Chinese character. Can contain numbers, '_' and '-'. The disk description will appear on the
        console. Cannot begin with http:// or https://
    required: false
    default: null
    aliases: []
    choices: ['name']
  description:
    description:
      - The description. The default value is blank. [2, 256] English or Chinese characters. Cannot begin with http://
        or https://
    required: false
    default: null
    aliases: []
    cidr_block:
  user_cidr:
    description:
      - User custom cidr in the VPC
    required: false
    default: null
    aliases: []
  vswitches:
    description:
      - List of hash/dictionary of route tables to add in VPC (see example)
    required: false
    default: null
    aliases: []
    choices: []
  wait:
    description:
      - Wait for the VPC instance to be 'running' before returning.
    required: false
    default: null
    aliases: []
    choices: [true, false]
  wait_timeout:
    description:
      - How long before wait gives up, in seconds
    required: false
    default: 300
    aliases: []
  vpc_id:
    description:
      - The unique ID of a VPC
    required: false
    default: null
    aliases: []
    choices: []
  purge_vswitches:
    description:
      - The List of unique ID of a VSwicth to delete from VPC
    required: true
    default: null
    aliases: []
  route_tables:
    description:
      - A dictionary array of route tables to add or remove from VPC (see example)
    required: true
    default: null
    aliases: []
  purge_routes:
    description:
      - A dictionary array of route tables to add in VPC
    required: false
    default: null
    aliases: []
    choices: []
  purge_vswitches:
    description:
      - A dictionary array of route tables to remove from VPC
    required: false
    default: null
    aliases: []
  vrouter_id:
    description:
      - The ID of the VRouter to be queried
    required: false
    default: null
    aliases: []
  pagenumber:
    description:
      - Page number of the instance status list. The start value is 1.
    required: false
    default: 1
    aliases: []
    choices: []
  pagesize:
    description:
      - The number of lines per page set for paging query. The maximum value is 50.
    required: false
    default: 10
    aliases: []
  vswitch_id:
    description:
      - The ID of the VSwitch to be queried
    required: false
    default: null
    aliases: ['subnet']
  zone_id:
    description:
      - The id of a zone.
    required: false
    default: null
    aliases: ['zone']
    choices: []

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
# Provisioning new VPC and VSwitch
#

# basic provisioning example to create vpc in VPC
- name: create vpc
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-hongkong
    status: present
    cidr_block: 192.168.0.0/16
    vpc_name: Demo_VPC
    description: Demo VPC
    vswitches:
      - zone_id: 'cn-hongkong-b'
        description: 'dummy'
  tasks:
    - name: create vpc
      ecs_vpc:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        status: '{{ status }}'
        cidr_block: '{{ cidr_block }}'
        vpc_name: '{{ vpc_name }}'
        description: '{{ description }}'
        vswitches: '{{ vswitches }}'

# basic provisioning example to delete vpc
- name: delete vpc
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-hongkong
  tasks:
    - name: delete vpc
      ecs_vpc:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        state: absent
        vpc_id: xxxxxxxxxx

# basic provisioning example to create vswitch
- name: create vswitch
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-hongkong
    vpc_id: xxxxxxxxxx
    vswitches:
      - zone_id: cn-hongkong-b
        cidr_block: '172.16.0.0/24'
        name: 'Demo_VSwitch'
        description: 'akashhttp://'
    state: present
  tasks:
    - name: create vswitch
      ecs_vpc:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        vswitches: '{{ vswitches }}'
        vpc_id: '{{ vpc_id }}'
        state: '{{ state }}'

# basic provisioning example to delete vswitch
- name: delete vswitch
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-hongkong
    purge_vswitches:
     - xxxxxxxxxx
    state: present
  tasks:
    - name: delete vswitch
      ecs_vpc:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        purge_vswitches: '{{ purge_vswitches }}'
        state: '{{ state }}'

# basic provisioning example to create custom route
- name: create vpc
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-hongkong
    state: present
    vpc_id: xxxxxxxxxx
    route_tables:
      - dest: '192.168.3.0/24'
        destination_cidrblock: '192.168.4.0/24'
        next_hop_id: 'xxxxxxxxxx'
  tasks:
    - name: create vpc
      ecs_vpc:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        state: '{{ state }}'
        route_tables: '{{ route_tables }}'
        vpc_id: '{{ vpc_id }}'

# basic provisioning example to delete custom route
- name: delete route
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-hongkong
    vpc_id: vpc-j6cjkmappmgb4fywpbj0u
    purge_routes:
         destination_cidrblock: "192.168.4.0/24"
         next_hop_id: "xxxxxxxxxx"
    state: present
  tasks:
    - name: delete route
      ecs_vpc:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        purge_routes: '{{ purge_routes }}'
        state: '{{ state }}'
        vpc_id: '{{ vpc_id }}'

# basic provisioning example to querying vroute
- name: get vrouter list
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-hongkong
    vrouter_id: xxxxxxxxxx
    pagenumber: 1
    pagesize: 10
    state: getinfo_vroute
  tasks:
    - name: get vrouter list
      ecs_vpc:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        vrouter_id: '{{ vrouter_id }}'
        state: '{{ state }}'
        pagenumber: '{{ pagenumber }}'
        pagesize: '{{ pagesize }}'

# basic provisioning example to querying vswitch
- name: querying vswitch status
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: ap-southeast-1
    status: getinfo_vswitch
    zone_id: ap-southeast-1a
    vpc_id: xxxxxxxxxx
    vswitch_id: xxxxxxxxxx
    page_size: 10
    page_number: 1
  tasks:
    - name: querying instance status
      ecs_vpc:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        status: '{{ status }}'
        zone_id: '{{ zone_id }}'
        vpc_id: '{{ vpc_id }}'
        vswitch_id: '{{ vswitch_id }}'
        page_size: '{{ page_size }}'
        page_number: '{{ page_number }}'
'''