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
module: ecs_slb
version_added: "1.0"
short_description: Creates, Sets and Remove backend servers and Describe backend servers health status of SLB
description:
    - Creates, Sets and Remove backend servers and Describe backend servers health status of SLB
options:
  acs_access_key:
    description:
      - Aliyun Cloud access key. If not set then the value of the 'ACS_ACCESS_KEY_ID', 'ACS_ACCESS_KEY' or
        'ECS_ACCESS_KEY' environment variable is used.
    required: false
    default: null
    aliases: ['ecs_access_key', 'access_key']
  acs_secret_access_key:
    description:
      - Aliyun Cloud secret key. If not set then the value of the 'ACS_SECRET_ACCESS_KEY', 'ACS_SECRET_KEY', or
        'ECS_SECRET_KEY' environment variable is used.
    required: false
    default: null
    aliases: ['ecs_secret_key', 'secret_key']
  status:
    description:
      - Create, set, remove or describe backend server health status of an slb
    required: false
    default: 'present'
    aliases: ['state']
    choices: ['present', 'absent', 'check']
  load_balancer_id:
    description:
      - The unique ID of a Server Load Balancer instance
    required: true
    default: null
    aliases: [ 'ecs_slb' ]
  backend_servers:
    description:
      - List of hash/dictionary of backend servers to add or set in (see example)
    required: true
    default: null
    aliases: []
    choices: []
  ports:
    description:
      - list ports used by the Server Load Balancer instance frontend to describe health status for
    required: false
    default: null
    aliases: []

requirements:
  - "python >= 2.7"
  - aliyun-python-sdk-core, aliyun-python-sdk-ecs, aliyun-python-sdk-slb, ecsutils and footmark
notes:
  - If parameters are not set within the module, the following
    environment variables can be used in decreasing order of precedence
    C(ACS_ACCESS_KEY_ID) or C(ACS_ACCESS_KEY) or C(ECS_ACCESS_KEY),
    C(ACS_SECRET_ACCESS_KEY) or C(ACS_SECRET_KEY) or C(ECS_SECRET_KEY)
'''

EXAMPLES = '''
#
# Provisioning new add or remove Backend Server from SLB
#

Basic example to add backend server to load balancer instance
- name: add backend server
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
  tasks:
    - name: add backend server
      ecs_slb:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        load_balancer_id: 'xxxxxxxxxx'
        backend_servers:
          - server_id: xxxxxxxxxx
            weight: 70
          - server_id: xxxxxxxxxx


Basic example to set backend server of load balancer instance
- name: set backend server
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
  tasks:
    - name: set backend server
      ecs_slb:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        load_balancer_id: 'xxxxxxxxxx'
        backend_servers:
          - server_id: xxxxxxxxxx
            weight: 50
          - server_id: xxxxxxxxxx
            weight: 80

Basic example to remove backend servers from load balancer instance
- name: remove backend servers
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
  tasks:
    - name: remove backend servers
      ecs_slb:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        load_balancer_id: 'xxxxxxxxxx'
        status: absent
        backend_servers:
          - xxxxxxxxxx
          - xxxxxxxxxx

Basic example to describe backend server health status of load balancer instance
- name: describe backend server health status
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
  tasks:
    - name: describe backend server health status
      ecs_slb:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        status: check
        load_balancer_id: 'xxxxxxxxxx'
        ports:
          - '80'
          - '120'
'''