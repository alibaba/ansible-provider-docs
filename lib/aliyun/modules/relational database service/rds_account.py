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
module: rds_account
version_added: "1.0"
short_description: Create account, delete account, reset instance password, reset account, grant account permission and revoke account permission in RDS.
description:
    - Create account, delete account, reset instance password, reset account, grant account permission and revoke account permission in RDS.

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
  command:
    description:
      - The state of the instance after operating.
    required: True
    default: 'create'
    choices: [ 'create', 'delete', 'reset_password', 'reset', 'grant', 'revoke' ]
  db_instance_id:
    description:
      - Id of instance.
    required: True
    default: null
  account_name:
    description:
      - Operation account requiring a uniqueness check. It may consist of lower case letters, numbers and underlines, and must start with a letter and have no more than 16 characters
    required: True
    default: null
    aliases: [ 'name' ]
  account_password:
    description:
      - Operation password. It may consist of letters, digits, or underlines, with a length of 6 to 32 characters.
    required: True
    default: null
    aliases: ['password']
  description:
    description:
      - Account remarks, which cannot exceed 256 characters. It cannot begin with http:// , https:// .  It must start with a Chinese character or English letter. It can include Chinese and english characters/letters, underlines (_), hyphens (-), and numbers. The length may be 2-256 characters
    required: False
    default: null
  account_type:
    description:
      - Privilege type of account. Normal - Common privilege, Super - High privilege, default value is Normal. This parameter is valid for MySQL 5.5/5.6 only
    required: True
    default: Normal
    choices: ['Normal', 'normal', 'Super', 'super']
  db_name:
    description:
      - Name of the database associated with this account.
    required: True
    default: null
  account_privilege:
    description:
      - Account permission
    required: True
    default: null
    aliases: ['privilege']
    choices: ['ReadOnly', 'ReadWrite']
'''

EXAMPLES = '''
#
# provisioning for rds
#

# basic provisioning example to create account
- name: create account
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-hongkong
    command: create
    db_instance_id: xxxxxxxxxx
    account_name: xxxxxxxxxx
    account_password: rohit@123
    description: normal account
    account_type: normal
  tasks:
    - name: create account
      rds_account:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        command: '{{ command }}'
        db_instance_id: '{{ db_instance_id }}'
        account_name: '{{ account_name }}'
        account_password: '{{ account_password }}'
        description: '{{ description }}'
        account_type: '{{ account_type }}'

# basic provisioning example to reset an instance password
- name: Reset an instance password
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-hongkong
    command: reset_password
    db_instance_id: xxxxxxxxxx
    account_name: xxxxxxxxxx
    account_password: testuser@123
  tasks:
    - name: Reset an instance password
      rds_account:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        command: '{{ command }}'
        db_instance_id: '{{ db_instance_id }}'
        account_name: '{{ account_name }}'
        account_password: '{{ account_password }}'

# basic provisioning example to reset an account
- name: Reset an account
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-hongkong
    command: reset
    db_instance_id: xxxxxxxxxx
    account_name: xxxxxxxxxx
    account_password: testuser@123   
  tasks:
    - name: Reset an account
      rds_account:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        command: '{{ command }}'
        db_instance_id: '{{ db_instance_id }}'
        account_name: '{{ account_name }}'
        account_password: '{{ account_password }}'

# basic provisioning example to delete an account
- name: delete account
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-hongkong
    command: delete
    db_instance_id: xxxxxxxxxx
    account_name: xxxxxxxxxx
  tasks:
    - name: delete account
      rds_account:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        command: '{{ command }}'
        db_instance_id: '{{ db_instance_id }}'
        account_name: '{{ account_name }}'

# basic provisioning example to grant account permission
- name: grant account permission
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-hongkong
    command: grant
    db_instance_id: xxxxxxxxxx
    db_name: xxxxxxxxxx
    account_name: xxxxxxxxxx
    account_privilege: ReadOnly
  tasks:
    - name: grant account permission
      rds_account:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        command: '{{ command }}'
        db_instance_id: '{{ db_instance_id }}'
        db_name: '{{ db_name }}'
        account_name: '{{ account_name }}'
        account_privilege: '{{ account_privilege }}'

# basic provisioning example to revoke account permission
- name: revoke account permission
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-hongkong
    command: revoke
    db_instance_id: xxxxxxxxxx
    db_name: xxxxxxxxxx
    account_name:  xxxxxxxxxx
  tasks:
    - name: revoke account permission
      rds_account:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        command: '{{ command }}'
        db_instance_id: '{{ db_instance_id }}'
        db_name: '{{ db_name }}'
        account_name: '{{ account_name }}'
'''