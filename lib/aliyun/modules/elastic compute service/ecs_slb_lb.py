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
module: ecs_slb_lb
version_added: "1.0"
short_description: Create, Delete, Enable or Disable Server Load Balancer in ECS
description:
    - Create, Delete, Enable or Disable Server Load Balancer in ECS
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
  region:
    description:
      - The Aliyun Cloud region to use. If not specified then the value of the 'ACS_REGION', 'ACS_DEFAULT_REGION' or
        'ECS_REGION' environment variable, if any, is used.
    required: false
    default: null
    aliases: [ 'acs_region', 'ecs_region']
  status:
    description:
      - For creating new Server Load Balancer
    required: false
    default: 'present'
    aliases: ['state']
    choices: ['present', 'absent', 'active', 'inactive']
  load_balancer_name:
    description:
      - The name of the server load balancer
    required: false
    default: null
    aliases: [ 'name' ]
  load_balancer_id:
    description:
      - This parameter is required when user wants to perform edit operation in Load Balancer
    required: false
    default: null
    aliases: [ 'ecs_slb' ]
  address_type:
    description:
      - The address type of the SLB
    required: false
    default: 'internet'
    aliases: [ 'scheme' ]
    choices: ['internet', 'intranet']
  vswitch_id:
    description:
      - The vswitch id of the VPC instance
    required: false
    default: null
    aliases: ['subnet_id', 'subnet']
  internet_charge_type:
    description:
      - The charge type of internet
    required: false
    default: 'paybytraffic'
    aliases: ['paybybandwidth', 'paybytraffic']
  master_zone_id:
    description:
      - The main usable area ID of the created Load Balancer can be found by the DescribeZone interface
    required: false
    default: null
    aliases: []
  slave_zone_id:
    description:
      - The ID of the standby zone of the created Load Balancer can be found on the DescribeZone interface
    required: false
    default: null
    aliases: []
  bandwidth:
    description:
      - Bandwidth peak of the public network instance charged per fixed bandwidth
    required: false
    default: 1
    aliases: []
    choices: [ 1-1000 Mbps ]
  listeners:
    description:
       - List of ports/protocols for this SLB to listen on (see example)
    required: false
    default: null
    aliases: []
  purge_listeners:
    description:
      - Purge existing listeners on SLB that are not found in listeners
    required: false
    default: true
    aliases: []
    choices: []
  instance_ids:
    description:
      - List of instance ids to attach to this SLB
    required: false
    default: null
    aliases: []
    choices: []
  purge_instance_ids:
    description:
      - Purge existing instance ids on SLB that are not found in instance_ids
    required: false
    default: true
    aliases: []
    choices: []
  validate_certs:
    description:
      - When set to "no", SSL certificates will not be validated
    required: false
    default: 'yes'
    aliases: []
    choices: ['yes', 'no']
  tags:
    description:
      - An associative array of stickness policy settings. Policy will be applied to all listeners
    required: false
    default: null
    aliases: []
    choices: []
  wait:
    description:
      - Wait for the SLB instance to be 'running' before returning
    required: false
    default: 'no'
    aliases: []
    choices: ['yes', 'no']
  wait_timeout:
    description:
      - how long before wait gives up, in seconds
    required: false
    default: 300
    aliases: []
    choices: []
  load_balancer_id:
    description:
      - The List of unique ID of a Server Load Balancer instance
    required: true
    default: null
    aliases: ['ecs_slb']
    choices: []
  internet_charge_type:
    description:
      - Charging mode for the public network instance
    required: false
    default: 'paybytraffic'
    aliases: []
    choices: ['paybybandwidth', 'paybytraffic']

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
# Provisioning new Server Load Balancer
#

# Basic provisioning example to create Load Balancer
- name: create server load balancer add listeners and add backend server
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-beijing
    load_balancer_name: demo_slb
    address_type: internet
    internet_charge_type: paybytraffic
    state: present
  tasks:
    - name: create server load balancer add listeners and add backend server
      ecs_slb_lb:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        load_balancer_name: '{{ load_balancer_name }}'
        address_type: '{{ address_type }}'
        internet_charge_type: '{{ internet_charge_type }}'
        state: '{{ state }}'

# Advanced provisioning example to create Load Balancer with Listeners and Backend Servers
- name: create server load balancer, add listeners and add backend server
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-beijing
    master_zone_id: cn-beijing-a
    slave_zone_id: cn-beijing-b
    load_balancer_name: demo_slb
    scheme: internet
    internet_charge_type: paybytraffic
    bandwidth: 1
    listeners:
      - protocol: http
        load_balancer_port: 80
        instance_port: 80
        bandwidth: 1
        scheduler: wrr
        gzip: "on"
        health_check:
          ping_port: 80
          ping_path: /index.html
          response_timeout: 5
          interval: 30
          unhealthy_threshold: 2
          healthy_threshold: 10
          http_code: http_2xx
        stickiness:
          enabled: "on"
          session_type: insert
          cookie: 300
          cookie_timeout: 1
    vswitch_id: xxxxxxxxxx
    instance_ids:
      - xxxxxxxxxx
      - xxxxxxxxxx
    state: present
  tasks:
    - name: create server load balancer add listeners and add backend server
      ecs_slb_lb:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        master_zone_id: '{{ master_zone_id }}'
        slave_zone_id: '{{ slave_zone_id }}'
        load_balancer_name: '{{ load_balancer_name }}'
        scheme: '{{ scheme }}'
        internet_charge_type: '{{ internet_charge_type }}'
        bandwidth: '{{ bandwidth }}'
        listeners: '{{ listeners }}'
        instance_ids: '{{ instance_ids }}'
        vswitch_id: '{{ vswitch_id }}'
        state: '{{ state }}'

# Basic provisioning example to Modify  SLB Internet Specification
- name: modify server load balancer internet specification
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-beijing
    load_balancer_id: xxxxxxxxxx
    internet_charge_type: paybytraffic
    bandwidth: 5
  tasks:
    - name: modify server load balancer internet specification
      ecs_slb_lb:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        load_balancer_id: '{{ load_balancer_id }}'
        internet_charge_type: '{{ internet_charge_type }}'
        bandwidth: '{{ bandwidth }}'

# Basic provisioning example to Delete Server Load Balancer
- name: delete server load balancer
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-beijing
    load_balancer_id: xxxxxxxxxx
    status : absent
  tasks:
    - name: delete server load balancer
      ecs_slb_lb:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        load_balancer_id: '{{ load_balancer_id }}'
        status: '{{ status }}'

# Basic provisioning example to set  SLB Status
- name: set server load balancer status
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-beijing
    load_balancer_id: xxxxxxxxxx
    status: active
  tasks:
    - name: set server load balancer
      ecs_slb:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        load_balancer_id: '{{ load_balancer_id }}'
        status: '{{ status }}'

# Basic provisioning example to set Server Load Balancer Name
- name: set server load balancer name
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-beijing
    load_balancer_id: xxxxxxxxxx
    load_balancer_name: slb_new_name
    status : present
  tasks:
    - name: set server load balancer name
      ecs_slb_lb:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        load_balancer_id: '{{ load_balancer_id }}'
        load_balancer_name: '{{ load_balancer_name }}'
        status: '{{ status }}'
'''