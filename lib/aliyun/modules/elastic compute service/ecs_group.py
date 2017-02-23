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
module: ecs_group
version_added: "1.0"
short_description: Create, Query or Delete Security Group
description:
    - Create, Query or Delete Security Group
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
      - For creating new security group and/or authorizing.
    required: false
    default: 'present'
    aliases: ['state']
    choices: ['present', 'absent', 'getinfo']
  security_group_name:
    description:
      - The security group name. 
    required: false
    default: null
    aliases: ['name']
    choices: []
  description:
    description:
      - The description of the security group.
    required: false
    default: null
    aliases: []
    choices: []
  vpc_id:
    description:
      - The ID of the VPC to which the security group belongs. If this parameter is not passed, the security group will be created using classic network type.
    required: false
    default: null
    aliases: []
    choices: []
  group_tags:
    description:
      - A list of hash/dictionaries of group tags, ['{"tag_key":"value", "tag_value":"value"}'], tag_key must be not null when tag_value isn't null
    required: false
    default: null
    aliases: []
    choices: []
  group_id:
    description:
      - Provide the security group id to perform rules authorization. This parameter is not required for creating new security group.
    required: false
    default: null
    aliases: ['security_group_id', 'group_ids', 'security_group_ids']
    choices: []
  rules:
    description:
      - List of firewall inbound rules to enforce in this group. (see example)
    required: false
    default: null
    aliases: []
    choices: []
  rules_egress:
    description:
      - List of firewall outbound rules to enforce in this group. (see example)
    required: false
    default: null
    aliases: []
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
# Provisioning new Security Group
#

Basic provisioning example to create security group
- name: create security group
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-shenzhen
  tasks:
    - name: create security grp
      ecs_group:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        security_group_name: 'AliyunSG'


Basic provisioning example authorize security group
- name: authorize security grp
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-shenzhen
  tasks:
    - name: authorize security group
      ecs_group:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        security_group_id: xxxxxxxxxx
        region: '{{ region }}'
        rules:
          - ip_protocol: tcp
            port_range: 1/122
            source_cidr_ip: '10.159.6.18/12'
        rules_egress:
          - proto: all
            port_range: -1/-1
            dest_group_id: xxxxxxxxxx
            nic_type: intranet


Provisioning example create and authorize security group
- name: create and authorize security group
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-shenzhen
  tasks:
    - name: create and authorize security grp
      ecs_group:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        security_group_name: 'AliyunSG'
        description: 'an example ECS group'
        region: '{{ region }}'
        rules:
          - ip_protocol: tcp
            port_range: 1/122
            source_cidr_ip: '10.159.6.18/12'
            priority: 10
            policy: drop
            nic_type: intranet
        rules_egress:
          - proto: all
            port_range: -1/-1
            dest_group_id: xxxxxxxxxx
            group_owner_id: xxxxxxxxxx
            priority: 10
            policy: accept
            nic_type: intranet


# Provisioning example to delete security group
- name: delete security grp
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: us-west-1
    security_group_ids:
     - xxxxxxxxxx
    status: absent
  tasks:
    - name: delete security grp
      ecs_group:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        security_group_ids: '{{ security_group_ids }}'
        status: '{{ status }}'


# Provisioning example to querying security group list
- name: querying security group list
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-beijing
    status: getinfo
  tasks:
    - name: Querying Security group list
      ecs_group:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        status: '{{ status }}'
'''