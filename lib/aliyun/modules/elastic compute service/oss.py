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
module: oss
version_added: "1.0"
short_description: Create/Delete Bucket and Objects/Folder. Upload Files in OSS
description:
    - This module allows the user to manage OSS buckets and the objects within them. Includes support for
      creating and deleting both objects and buckets, retrieving object keys. This module has a dependency on footmark and ossutils.
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
    default: cn-hangzhou
    aliases: [ 'acs_region', 'ecs_region']
  mode:
    description:
      - Switches the module behaviour between create (bucket), delete (bucket), put (upload), put_folder
        (create folder), list (list keys) and delobj (delete object).
    required: true
    choices: ['create', 'delete', 'put', 'put_folder', 'list', 'delobj']
  bucket:
    description:
      - Bucket name.
    required: true
    default: null
    aliases: [ 'bucket_name', 'name' ]
  permission:
    description:
      - This option lets the user set the canned permissions on the bucket that are created. The permissions that
          can be set are 'private', 'public-read', 'public-read-write'. Multiple permissions can be specified as a list.
    required: false
    default: private
    choices: [ 'private', 'public-read', 'public-read-write' ]
  expiration:
    description:
      - Time limit (in seconds) for the URL generated and returned by OSS/Walrus when performing a mode=put or mode=geturl operation.
    required: false
    default: 600
    aliases: []
  headers:
    description:
      - Custom headers for PUT operation, as a dictionary of 'key=value' and 'key=value,key=value'.
    required: false
    default: null
  encrypt:
    description:
      - When set for PUT mode, asks for server-side encryption
    required: false
    default: no
  metadata:
    description:
      - Metadata for PUT operation, as a dictionary of 'key=value' and 'key=value,key=value'.
    required: false
    default: null
  overwrite:
    description:
      - Force overwrite either locally on the filesystem or remotely with the object/key. Used with PUT and GET
          operations. Boolean or one of [always, never, different], true is equal to 'always' and false is equal to
          'never'.
    required: false
    default: 'always'
  src:
    description:
      - The source file path when performing a PUT operation.
    required: true
    default: null
    aliases: []
  file_name:
    description:
      - Name to file after uploaded to bucket
    required: true
    default: null
    aliases: []
  folder_name:
    description:
      - name of the folder to create
    required: true
    default: null
  marker:
    description:
      - Specifies the key to start with when using list mode. Object keys are returned in alphabetical order,
          starting with key after the marker in order
    required: false
    default: null
  max_keys:
    description:
      - Max number of results to return in list mode, set this if you want to retrieve fewer than the default 1000 keys.
    required: false
    default: 1000
  object_list:
    description:
      - Specify list of objects to delete from a bucket
    required: false
    default: null


'''

EXAMPLES = '''
#
# provisioning new oss bucket
#

# basic provisioning example to create bucket
- name: create oss bucket
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-hangzhou
    mode: create
    bucket: bucketname
    permission: public-read-write    
  tasks:
    - name: create oss bucket
      oss:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        mode: '{{ mode }}'
        bucket: '{{ bucket }}'
        permission: '{{ permission }}'        
      register: result
    - debug: var=result

# basic provisioning example to delete bucket
- name: delete oss bucket
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-hangzhou
    mode: delete
    bucket: bucketname    
  tasks:
    - name: delete oss bucket
      oss:
        acs_access_key_id: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        mode: '{{ mode }}'
        bucket: '{{ bucket }}'        
      register: result
    - debug: var=result

# basic provisioning example to upload a file
- name: simple upload to bucket
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-hangzhou
    mode: put
    bucket: bucketname
    src: 'local_file.txt'
    file_name: 'remote_file.txt'
    headers:
      Content-Type: 'text/html'
      Content-Encoding: md5
    metadata:
      x-oss-meta-key: value
    expiration: 30    
  tasks:
    - name: simple upload to bucket
      oss:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        mode: '{{ mode }}'
        bucket: '{{ bucket }}'
        src: '{{ src }}'
        file_name: '{{ file_name }}'
        headers: '{{ headers }}'
        metadata: '{{ metadata }}'
        expiration: '{{ expiration }}'       
      register: result
    - debug: var=result

# basic provisioning example to create a folder in bucket
- name: create folder in a bucket
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-hangzhou
    mode: put_folder
    bucket: bucketname
    folder_name: MeetingDocs
  tasks:
    - name: create bucket folder
      oss:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        mode: '{{ mode }}'
        bucket: '{{ bucket }}'
        folder_name: '{{ folder_name }}'
      register: folder_result
    - debug: var=folder_result

# basic provisioning example to list bucket objects
- name: list bucket objects
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-hangzhou
    mode: list
    bucket: bucketname
    marker: xxxx
    max_keys: 150    
  tasks:
    - name: list bucket objects
      oss:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        mode: '{{ mode }}'
        bucket: '{{ bucket }}'
        marker: '{{ marker }}'
        max_keys: '{{ max_keys }}'
      register: list_result
    - debug: var=list_result

# basic provisioning example to delete bucket objects
- name: delete bucket objects
  hosts: localhost
  connection: local
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-hangzhou
    mode: delobj
    bucket: bucketname
    object_list:
      - objectname
      - objectname    
  tasks:
    - name: delete bucket objects
      oss:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        mode: '{{ mode }}'
        bucket: '{{ bucket }}'
        object_list: '{{ object_list }}'
      register: delete_objects_result
    - debug: var=delete_objects_result

'''