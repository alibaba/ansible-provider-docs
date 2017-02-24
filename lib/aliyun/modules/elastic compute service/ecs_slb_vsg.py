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
module: ecs_slb_vsg
version_added: "1.0"
short_description: Create, set and Delete VServer Group, add, remove, modify VServer Group Backend Server
description:
    - Create, set and Delete VServer Group
    - Add, remove and modify VServer Group Backend Server
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
    aliases: [ 'acs_region', 'ecs_region']
  status:
    description:
      - To create VServer Group, provide state as ‘present’
    required: false
    default: 'present'
    aliases: ['state']
    choices: ['present', 'absent']
  load_balancer_id:
    description:
      - The unique ID of a Server Load Balancer instance
    required: true
    default: null
    aliases: ['ecs_slb']
    choices: []
  vserver_group_name:
    description:
      - Virtual server group name
    required: true
    default: null
    aliases: []
    choices: []
  vserver_group_id:
    description:
      - The unique identifier for the virtual server group
    required: true
    default: null
    aliases: []
    choices: []
  backend_servers:
    description:
      - List of hash/dictionary of backend servers to add or set in (see example)
    required: true
    default: null
    aliases: []
    choices: []
  purge_backend_servers:
    description:
      - List of hash/dictionary of backend servers to delete (see example)
    required: true
    default: null
    aliases: []
    choices: []
requirements:
  - "python >= 2.7"
  - aliyun-python-sdk-core, aliyun-python-sdk-ecs, aliyun-python-sdk-slb, ecsutils and footmark
notes:
  - If parameters are not set within the module, the following
    environment variables can be used in decreasing order of precedence
    C(ACS_ACCESS_KEY_ID) or C(ACS_ACCESS_KEY) or C(ECS_ACCESS_KEY),
    C(ACS_SECRET_ACCESS_KEY) or C(ACS_SECRET_KEY) or C(ECS_SECRET_KEY),
    C(ACS_REGION) or C(ACS_DEFAULT_REGION) or C(ECS_REGION)
'''

EXAMPLES = '''
#
# Provisioning new VServer Group
#

Basic provisioning example to create vserver group and add backend server
- name: create vserver group and add backend server
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-shenzhen
    status: present
    load_balancer_id: xxxxxxxxxx
    vserver_group_name : test
    backend_servers:
       -  server_id: xxxxxxxxxx
          port: 8085
          weight: 95
  tasks:
    - name: create vserver group and add backend server
      ecs_slb_vsg:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        status: '{{ status }}'
        load_balancer_id: '{{ load_balancer_id }}'
        vserver_group_name: '{{ vserver_group_name }}'
        backend_servers: '{{ backend_servers }}'

Basic provisioning example add backend server to vserver group
- name: add backend server to vserver group
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-shenzhen
    status: present
    vserver_group_id: xxxxxxxxxx
    backend_servers:
       -  server_id: xxxxxxxxxx
          port: 8085
          weight: 95
  tasks:
    - name: add backend server to vserver group
      ecs_slb_vsg:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        status: '{{ status }}'
        vserver_group_id: '{{ vserver_group_id }}'
        backend_servers: '{{ backend_servers }}'


Provisioning example set vserver group backend server
- name: set vserver group backend server
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-shenzhen
    status: present
    vserver_group_id: xxxxxxxxxx
    vserver_group_name : testa
    backend_servers:
       -  server_id: xxxxxxxxxx
          port: 8085
          weight: 95
  tasks:
    - name: set vserver group backend server
      ecs_slb_vsg:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        status: '{{ status }}'
        vserver_group_id: '{{ vserver_group_id}}'
        vserver_group_name: '{{ vserver_group_name }}'
        backend_servers: '{{ backend_servers }}'


# Provisioning example to remove vserver group backend server
- name: remove vserver group backend server
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-shenzhen
    status: present
    vserver_group_id: xxxxxxxxxx
    purge_backend_servers:
       -  server_id: xxxxxxxxxx
          port: 8085
  tasks:
    - name: remove vserver group backend server
      ecs_slb_vsg:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        status: '{{ status }}'
        vserver_group_id: '{{ vserver_group_id }}'
        purge_backend_servers: '{{ purge_backend_servers }}'


# Provisioning example to modifying vserver group backend server
- name: modifying vserver group backend server
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-shenzhen
    status: present
    vserver_group_id: xxxxxxxxxx
    purge_backend_servers:
       -  server_id: xxxxxxxxxx
          port: 8085
    backend_servers:
       -  server_id: xxxxxxxxxx
          port: 8085
          weight: 95
  tasks:
    - name: modifying vserver group backend server
      ecs_slb_vsg:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        status: '{{ status }}'
        vserver_group_id: '{{ vserver_group_id }}'
        purge_backend_servers: '{{ purge_backend_servers }}'
        backend_servers: '{{ backend_servers }}'

# Provisioning example to delete vserver group
- name: delete vserver group
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-shenzhen
    status: absent
    vserver_group_id: xxxxxxxxxx
  tasks:
    - name: delete vserver group
      ecs_slb_vsg:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        status: '{{ status }}'
        vserver_group_id: '{{ vserver_group_id }}'
'''