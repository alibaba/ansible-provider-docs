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
module: rds
version_added: "1.0"
short_description: Create instance, Create database, Create read-only instance, Modify rds instance, Change rds instance type, Restart instance, Switch between primary and standby database, Delete database and Release Instance in RDS.
description:
    - Create instance, Create database, Create read-only instance, Modify rds instance, Change rds instance type, Restart instance, Switch between primary and standby database, Delete database and Release Instance in RDS.

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
      - Specifies the action to take.
    required: True
    default: 'create'
    choices: [ 'create', 'delete', 'replicate', 'modify', 'reboot', 'switch' ]
  alicloud_zone:
    description:
      - availability zone in which to launch the instance. Used only when command=create, command=replicate.
    required: false
    default: null
    aliases: ['acs_zone', 'ecs_zone', 'zone']
  db_engine:
    description:
      - The type of database.
    required: true
    default: null
    choices: [ 'MySQL','SQLServer', 'PostgreSQL', 'PPAS']
  db_instance_class:
    description:
      - The instance type of the database.
    required: true
    default: null
    aliases: ['instance_type']
  db_instance_storage:
    description:
      - Size in gigabytes of the initial storage for the DB instance.
    required: true
    default: null
    aliases: ['size']
  instance_net_type:
    description:
      - The net type of the DB instance
    required: true
    default: false
    choices: ['Internet', 'Intranet']
  instance_description:
    description:
      - The description of the DB instance
    required: false
    default: null
  security_ip_list:
    description:
      - IP list that be allowed to access all DBs in the instance. Support CIDR mode.
    required: true
    default: null
  pay_type:
    description:
      - The pay type of the DB instance.
    required: true
    default: null
    choices: ['Postpaid', 'Prepaid']
  instance_network_type:
    description:
      - The network type of the instance.
    default: Classic
    required: false
    choices: ['VPC', 'Classic']
    aliases: ['network_type']
  connection_mode:
    description:
      - The connection mode of the rds instance.
    required: false
    choices: ['Performance', 'Safe']
  private_ip_address:
    description:
      - IP address of an VPC under VSwitchId. If no value is specified, the system will automatically assign a VPC IP address.
    default: null
    required: false
  allocate_public_ip:
    description:
      - Whether to allocate public IP.
    default: null
    required: false
  public_port:
    description:
      - The public connection port.
    default: null
    required: false
  db_name:
    description:
      - Name of a database to create within the instance.  If not specified then no database is created.
    required: True
    default: null
  db_description:
    description:
      - Description of a database to create within the instance.  If not specified then no database is created.
    required: false
    default: null
  character_set_name:
    description:
      - Associate the DB instance with a specified character set.
    required: True
    default: null
  maint_window:
    description:
      - "Maintenance window in format of ddd:hh24:mi-ddd:hh24:mi.  (Example: Mon:22:00-Mon:23:15) If not specified
      then a random maintenance window is assigned."
    required: false
    default: null
  preferred_backup_time:
    description:
      - Backup time, in the format ofHH:mmZ- HH:mm Z.This parameter is required if preferred_backup_period and
       backup_retention_period is passed.
    required: false
    default: null
  preferred_backup_period:
    description:
      - Backup period.
    required: false
    default: null
    aliases: ['backup_window']
  backup_retention_period:
    description:
      - Number of days backups are retained.
    required: false
    default: null
    aliases: ['backup_retention']
  db_tags:
    description:
      - A hash of db tags, tag_key must be not null when tag_value isn't null.
    required: false
    default: null
  wait:
    description:
      - wait for the RDS instance to be in state 'running' before returning.
    required: false
    default: "no"
    choices: [ 'yes', 'Yes', 'no', 'No', 'True', 'False', 'true', 'false' ]
  wait_timeout:
    description:
      - how long before wait gives up, in seconds
    required: false
    default: 300
  instance_id:
    description:
      - ID of the database to change.
    required: true
    default: null
    aliases: ['source_instance']
  engine_version:
    description:
      - Version number of the database engine to use. If not specified, then the current Aliyun RDS default engine
       version is used.
    required: true
    default: null
  current_connection_string:
    description:
      - Current connection string of an instance.
    default: null
    required: false
  connection_string_ prefix:
    description:
      - Target connection string.
    default: null
    required: false
  port:
    description:
      - Target port.
    default: null
    required: false
  node_id:
    description:
      - Unique ID of a node.
    required: True
    default: null
  force:
    description:
      - Yes- forced, No- unforced, default value- unforced
    required: false
    default: no
  period:
    description:
      - The type of the Prepaid
    default: null
    required: false
    choices: ['Year', 'Month']
  used_time:
    description:
      - The duration of the Prepaid
    default: null
    required: false
  vpc_id:
    description:
      - The ID of the VPC.
    default: null
    required: false
  vswitch_id:
    description:
      - The ID of the VSwitch.
    default: null
    required: false
'''

EXAMPLES = """
#
# provisioning for rds
#


# basic provisioning example to create rds instance

- name: create rds instance
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-beijing
    command: create
    alicloud_zone: cn-beijing-a
    db_engine: MySQL 
    engine_version: 5.6
    db_instance_class: rds.mysql.t1.small
    db_instance_storage: 10 
    instance_net_type: Intranet
    instance_description: ahttp://
    security_ip_list: 192.168.0.2/24
    pay_type: Postpaid
    connection_mode: Safe
    instance_network_type: VPC
    vpc_id: xxxxxxxxxx	
    vswitch_id: xxxxxxxxxx
    private_ip_address: 192.168.0.25
    allocate_public_ip: yes
    connection_string_prefix: test
    public_port: 3306
    db_name: testmysql
    db_description: test mysql 
    character_set_name: utf8
    maint_window: 02:00Z-06:00Z
    preferred_backup_time: 02:00Z-03:00Z
    preferred_backup_period: Monday,Tuesday
    backup_retention_period: 7
    wait: yes
    wait_timeout: 20
    db_tags:	
      name: test
  tasks:
    - name: create rds instance
      rds:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}' 
        alicloud_region: '{{ alicloud_region }}'
        alicloud_zone: '{{ alicloud_zone }}'
        command: '{{ command }}'
        db_engine: '{{ db_engine }}'
        engine_version: '{{ engine_version }}'
        db_instance_class: '{{ db_instance_class }}'
        db_instance_storage: '{{ db_instance_storage }}'		
        instance_net_type: '{{ instance_net_type }}'
        instance_description: '{{ instance_description }}'
        security_ip_list: '{{ security_ip_list }}'
        pay_type: '{{ pay_type }}'  
        connection_mode: '{{ connection_mode }}'
        instance_network_type: '{{ instance_network_type }}'
        vpc_id: '{{ vpc_id }}'
        vswitch_id: '{{ vswitch_id }}'
        private_ip_address: '{{ private_ip_address }}'
        allocate_public_ip: '{{ allocate_public_ip }}'
        connection_string_prefix: '{{ connection_string_prefix }}'
        public_port: '{{ public_port }}'
        db_name: '{{ db_name }}'    
        db_description: '{{ db_description }}'
        character_set_name: '{{ character_set_name }}'
        maint_window: '{{ maint_window }}'
        preferred_backup_time: '{{ preferred_backup_time }}'
        preferred_backup_period: '{{ preferred_backup_period }}'
        backup_retention_period: '{{ backup_retention_period }}'
        db_tags: '{{ db_tags }}'
        wait: '{{ wait }}'
        wait_timeout: '{{ wait_timeout }}'
      register: result
    - debug: var=result

# basic provisioning example to change rds instance type

- name: change rds instance type
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-beijing
    command: modify
    instance_id: xxxxxxxxxx
    db_instance_class: rds.mysql.s1.small
    db_instance_storage: 35 
    pay_type: Postpaid
  tasks:
    - name: change rds instance type
      rds:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        command: '{{ command }}'
        instance_id: '{{ instance_id }}'
        db_instance_class: '{{ db_instance_class }}'
        db_instance_storage: '{{ db_instance_storage }}'
        pay_type: '{{ pay_type }}'
      register: result
    - debug: var=result   

# basic provisioning example to modify rds instance   
 
- name: modify rds instance
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-beijing
    command: modify
    instance_id: xxxxxxxxxx
    db_instance_class: rds.mysql.t1.small
    db_instance_storage: 45    
    instance_description: xyz 
    security_ip_list: 192.168.0.2/24
    pay_type: Postpaid
    connection_mode: Safe
    instance_network_type: VPC
    vpc_id: xxxxxxxxxx	
    vswitch_id: xxxxxxxxxx
    current_connection_string: test.mysql.rds.aliyuncs.com
    connection_string_prefix: test123
    port: 3390
    maint_window: 02:00Z-06:00Z
    preferred_backup_time:  02:00Z-03:00Z
    preferred_backup_period: Monday
    backup_retention_period: 50
  tasks:
    - name: modify rds instance
      rds:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        command: '{{ command }}'
        instance_id: '{{ instance_id }}'
        db_instance_class: '{{ db_instance_class }}'
        db_instance_storage: '{{ db_instance_storage }}'		
        instance_description: '{{ instance_description }}'
        security_ip_list: '{{ security_ip_list }}'
        pay_type: '{{ pay_type }}'      
        connection_mode: '{{ connection_mode }}'
        instance_network_type: '{{ instance_network_type }}'
        vpc_id: '{{ vpc_id }}'
        vswitch_id: '{{ vswitch_id }}'
        current_connection_string: '{{ current_connection_string }}'
        connection_string_prefix: '{{ connection_string_prefix }}'
        port: '{{ port }}'
        maint_window: '{{ maint_window }}'
        preferred_backup_time: '{{ preferred_backup_time }}'
        preferred_backup_period: '{{ preferred_backup_period }}'
        backup_retention_period: '{{ backup_retention_period }}'
      register: result
    - debug: var=result 

# basic provisioning example to create database

- name: create database
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-hongkong
    command: create
    instance_id: xxxxxxxxxx
    db_name: testdb
    db_description: test
    character_set_name: utf8
  tasks:
    - name: create database
      rds:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        command: '{{ command }}'
        instance_id: '{{ instance_id }}'
        db_name: '{{ db_name }}'
        db_description: '{{ db_description }}'
        character_set_name: '{{ character_set_name }}'
    
# basic provisioning example to delete database

- name: delete database
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-hongkong
    command: delete
    instance_id: xxxxxxxxxx
    db_name: testdb
  tasks:
    - name: delete database
      rds:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        command: '{{ command }}'
        instance_id: '{{ instance_id }}'
        db_name: '{{ db_name }}'
    
# basic provisioning example to switch between primary and standby database of an rds

- name: switch between primary and standby database
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-hongkong
    command: switch
    instance_id: xxxxxxxxxx
    node_id: xxxxxxxxxx
    force: 'Yes'
  tasks:
    - name: switch between primary and standby database
      rds:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        command: '{{ command }}'
        instance_id: '{{ instance_id }}'
        node_id: '{{ node_id }}'
        force: '{{ force }}'
    
# basic provisioning example to restart rds instance

- name: Restart RDS Instance
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-beijing
    command: reboot
    instance_id: xxxxxxxxxx
  tasks:
    - name: Restart RDS Instance
      rds:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        command: '{{ command }}'
        instance_id: '{{ instance_id }}'
    
# basic provisioning example to release rds instance

- name: Release RDS Instance
  hosts: localhost
  connection: local
  vars:
    alicloud_access_key: xxxxxxxxxx
    alicloud_secret_key: xxxxxxxxxx
    alicloud_region: cn-beijing
    command: delete
    instance_id: xxxxxxxxxx
  tasks:
    - name: Release RDS Instance
      rds:
        alicloud_access_key: '{{ alicloud_access_key }}'
        alicloud_secret_key: '{{ alicloud_secret_key }}'
        alicloud_region: '{{ alicloud_region }}'
        command: '{{ command }}'
        instance_id: '{{ instance_id }}'
"""

