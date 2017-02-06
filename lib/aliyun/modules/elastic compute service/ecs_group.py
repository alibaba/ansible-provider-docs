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
      - The security group name. [2, 128] English or Chinese characters, must begin with an uppercase/lowercase letter or Chinese character. Can contain numbers, ".", "_" or "-". It cannot begin with http:// or https://.
    required: true
    default: null
    aliases: ['name']
    choices: []
  description:
    description:
      - The description of the security group, which is a string of 2 to 256 characters. It cannot begin with http:// or https://.
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
      - List of firewall inbound rules to enforce in this group. If none are supplied, a default all-out rule is assumed. If an empty list is supplied, no inbound rules will be enabled. Each rule contains four attributes as specified in Inbound Security Group Rules
    required: false
    default: null
    aliases: []
    choices: []
  rules_egress:
    description:
      - List of firewall outbound rules to enforce in this group. If none are supplied, a default all-out rule is assumed. If an empty list is supplied, no outbound rules will be enabled.Each rule contains four attributes as specified in Outbound Security Group Rules
    required: false
    default: null
    aliases: []
    choices: []
  ip_protocol:
    description:
      - IP protocol, with a values tcp | udp | icmp | gre | all .all indicates support for all the four protocols
    required: yes
    default: null
    aliases: ['proto']
    choices: []
  port_range:
    description:
      - The range of port numbers relevant to the IP protocol When the protocol is 'tcp' or 'udp', the default port number range is 1-65535. For example, '1/200' means that the range of the port numbers is 1-200. If the input value is '200/1', the interface call reports an error. When the protocol is 'icmp', the port number range is -1/-1. When the protocol is 'gre', the port number range is -1/-1. When the protocol is all the port number range is -1/-1.
    required: yes
    default: null
    aliases: []
    choices: []
  source_group_id:
    description:
      - The security group ID. Either the source_group_id or cidr_ip parameter must be set. If both are set, then source_cidr_ip is authorized by default. If source_group_id is specified and source_cidr_ip is not specified, nic_type must be set to intranet
    required: false
    default: null
    aliases: ['group_id']
    choices: []
  source_group_owner_id:
    description:
      - When the cross-user security group authorization, the source security group belongs to the user's Ali cloud account Id. The parameter is optional, if not set, the default is the same account between the security group authorization. source_cidr_ip This parameter has no effect if it has been set.
    default: null
    required: false
    aliases: ['group_owner_id']
    choices: []
  source_cidr_ip:
    description:
      - The source IP address range (CIDR format is used to specify the IP address range). The default value is 0.0.0.0/0 (which means no restriction will be applied). Other supported formats include 10.159.6.18/12. Only IPv4 is supported.
    default: null
    required: false
    aliases: ['cidr_ip']
    choices: []
  policy:
    description:
      - Authorization policy
    default: accept
    required: false
    aliases: []
    choices: ['accept', 'drop']
  priority:
    description:
      - Authorization policy priority
    default: 1
    required: false
    aliases: []
    choices: [1-100]
  nic_type:
    description:
      - Network type
    default: internet
    required: false
    choices: ['internet', 'intranet']
    aliases: []
  dest_group_id:
    description:
      - The target security group ID within the same region. Either the dest_group_id or dest_cidr_ip must be set. If both are set, then dest_cidr_ip is authorized by default. If this field is specified, but no dest_cidr_ip is specified, the nic_type can only select intranet
    default: null
    required: false
    aliases: ['group_id']
    choices: []
  dest_group_owner_id:
    description:
      - The Alibaba Cloud user account Id of the target security group when security groups are authorized across accounts. This parameter is optional. If it is not set, then authorization is performed for security groups of the same account. This parameter is invalid if DestCidrIp has already been set.
    default: null
    required: false
    aliases: ['group_owner_id']
    choices: []
  dest_cidr_ip:
    description:
      - The target IP address range (CIDR format is used to specify the IP address range). The default value is 0.0.0.0/0 (which means no restriction will be applied). Other supported formats include 10.159.6.18/12. Only IPv4 is supported.
    default: null
    required: false
    aliases: ['cidr_ip']
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
        acs_access_key_id: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        security_group_name: 'AliyunSG'
      register: result_details
    - debug: var=result_details


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
        acs_access_key_id: '{{ acs_access_key }}'
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
      register: result_details
    - debug: var=result_details


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
        acs_access_key_id: '{{ acs_access_key }}'
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
      register: result_details
    - debug: var=result_details


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
        acs_access_key_id: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        security_group_ids: '{{ security_group_ids }}'
        status: '{{ status }}'
      register: result
    - debug: var=result


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
        acs_access_key_id: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        status: '{{ status }}'
      register: result
'''