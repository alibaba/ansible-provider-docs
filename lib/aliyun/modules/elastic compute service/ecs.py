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
module: ecs
version_added: "1.0"
short_description: Create, Start, Stop, Restart or Terminate an Instance in ECS. Add or Remove Instance to/from a Security Group
description:
    - Creates, starts, stops, restarts or terminates ecs instances.
    - Adds or removes ecs instances to/from security group.
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
      - The state of the instance after operating.
    required: false
    default: 'present'
    aliases: ['state']
    choices: ['present', 'pending', 'running', 'stopped', 'restarted', 'absent', 'getinfo', 'getstatus']
  zone_id:
    description: Aliyun availability zone ID in which to launch the instance
    required: false
    default: null
    aliases: [ 'acs_zone', 'ecs_zone', 'zone'] 
  image_id:
    description: Image ID to use for the instance. Parameter is B(required) when provisioning new ecs instance
    required: false
    default: null
    aliases: ['image']
  instance_type:
    description: Instance type to use for the instance. Parameter is B(required) when provisioning new ecs instance
    required: false
    default: null
    aliases: [ 'type' ]
  group_id:
    description: Security group id to use with the instance. Parameter is B(required) while joining or leaving security group
    required: false
    default: null
    aliases: []
  io_optimized:
    description: Whether instance is using optimized volumes.
    required: false
    default: "no"
    aliases: []
    choices: ["yes", "no"]
  vswitch_id:
    description: The subnet ID in which to launch the instance (VPC).
    required: false
    default: null
    aliases: ['vpc_subnet_id']
  instance_name:
    description: Name of the instance to use.
    required: false
    default: null
    aliases: []
  description:
    description: Description of the instance to use.
    required: false
    default: null
    aliases: []
  internet_data:
    description:
       - A hash/dictionaries of internet to the new instance; '{"key":"value"}';
       - keys allowed are
            - charge_type (required=false; default="PayByBandwidth", choices=["PayByBandwidth", "PayByTraffic"])
            - max_bandwidth_in(required=false, default=200)
            - max_bandwidth_out(required=false, default=0)
    required: false
    default: null
    aliases: []
  host_name:
    description: Instance host name.
    required: false
    default: null
    aliases: []
  password:
    description: The password to login instance.
    required: false
    default: null
    aliases: []
  system_disk:
    description:
        - A hash/dictionaries of system disk to the new instance; '{"key":"value"}';
        - keys allowed are
            - disk_category (required=false; default="cloud"; choices=["cloud", "cloud_efficiency", "cloud_ssd", "ephemeral_ssd"] )
            - disk_size (required=false; default=max[40, ImageSize]; choices=[40-500] )
            - disk_name (required=false; default=null)
            - disk_description (required=false; default=null)
    required: false
    default: null
    aliases: []
  disks:
      description:
        - A list of hash/dictionaries of volumes to add to the new instance; '[{"key":"value", "key":"value"}]';
        - keys allowed are
            - disk_category (required=false; default="cloud"; choices=["cloud", "cloud_efficiency", "cloud_ssd", "ephemeral_ssd"] )
            - disk_size (required=false; default=null; choices=depends on disk_category)
            - disk_name (required=false; default=null)
            - disk_description (required=false; default=null)
            - delete_on_termination (required=false, default="true")
            - snapshot_id (required=false; default=null), volume_type (str), iops (int) - device_type is deprecated use volume_type, iops must be set when volume_type='io1', ephemeral and snapshot are mutually exclusive.
      required: false
      default: null
      aliases: ['volumes']
  count:
      description: The number of the new instance.
      required: false
      default: 1
      aliases: []
  allocate_public_ip:
      description: Whether allocate a public ip for the new instance.
      required: false
      default: "yes"
      aliases: ['assign_public_ip']
      choices: ["yes", "no"]
  bind_eip:
      description: ID of Elastic IP Address bind to the new instance.
      required: false
      default: null
      aliases: []
  private_ip:
      description:
        - Private IP address of the instance, which cannot be specified separately.
      required: false
      default: null
      aliases: []
  instance_tags:
      description:
        - A list of hash/dictionaries of instance tags, '[{tag_key:"value", tag_value:"value"}]', tag_key must be not null when tag_value isn't null
      required: false
      default: null
      aliases: ['tags']
  instance_charge_type:
      description:
        - The charge type of the instance.
      required: false
      choices: ["PrePaid", "PostPaid"]
      default: "PostPaid"
  period:
      description:
        - The charge duration of the instance, the value is vaild when instance_charge_type is "PrePaid".
      required: false
      choices: [1~9,12,24,36]
      default: null
  auto_renew:
      description:
        - Whether automate renew the charge of the instance.
      required: false
      choices: ["yes", "no"]
      default: "no"
  auto_renew_period:
      description:
        - The duration of the automatic renew the charge of the instance. It is vaild when auto_renew is yes.
      required: false
      choices: [1, 2, 3, 6, 12]
      default: "no"
  ids:
      description:
        - A list of identifier for this instance or set of instances, so that the module will be idempotent with respect to ECS instances. This identifier should not be reused for another call later on. For details, see the description of client token at U(https://help.aliyun.com/document_detail/25693.html?spm=5176.doc25499.2.7.mrVgE2).
        - The length of the ids is the same with count
      required: false
      default: null
      aliases: ["id"]
  wait:
      description:
        - Wait for the instance to be 'running' before returning.
      required: false
      choices: ["yes", "no"]
      default: "no"
  wait_timeout:
      description:
        - how long before wait gives up, in seconds
      required: false
      choices: []
      default: "300"
  attributes:
      description:
        - A list of hash/dictionaries of instance attributes; '[{"key":"value", "key":"value"}]';. Parameter is B(required) when modifying an ecs instance
        - keys allowed are
            - id (required=true; default=null; description=ID of an ECS instance )
            - name (required=false; default=null; description=Name of the instance to modify)
            - description (required=false; default=null; description=Description of the instance to use)
            - password (required=false; default=null; description=The password to login instance)
            - host_name (required=false; default=null; description=Instance host name)
      required: false
      choices: []
      default: null
  instance_id:
      description:
        - A list of instance ids. Parameter is B(required) while starting, stopping, restarting, terminating, joining or leaving security group
      required: false
      default: null
      aliases: ["instance_ids"]
  sg_action:
      description:
        - The action of operating security group. Parameter is B(required) while joining or leaving security group
      required: false
      choices: ["join", "leave"]
      default: null
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
# provisioning new ecs instance
#

# basic provisioning example classic network
- name: basic provisioning example
  hosts: localhost
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-beijing
    zone: cn-beijing-a
    image: ubuntu1404_64_40G_cloudinit_20160727.raw
    instance_type: ecs.n1.small
    assign_public_ip: yes
  tasks:
    - name: classic network
      ecs:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        zone: '{{ zone }}'
        image: '{{ image }}'
        instance_type: '{{ instance_type }}'
        count: 2
        assign_public_ip: '{{ assign_public_ip }}'

# basic provisioning example vpc network
- name: basic provisioning example
  hosts: localhost
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-beijing
    image: ubuntu1404_64_40G_cloudinit_20160727.raw
    instance_type: ecs.n1.small
    vswitch_id: xxxxxxxxxx
    assign_public_ip: no
  tasks:
    - name: vpc network
      ecs:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        image: '{{ image }}'
        instance_type: '{{ instance_type }}'
        vswitch_id: '{{ vswitch_id }}'
        assign_public_ip: '{{ assign_public_ip }}'


# advanced example with tagging and host name password
- name: advanced provisioning example
  hosts: localhost
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-beijing
    image: ubuntu1404_64_40G_cloudinit_20160727.raw
    instance_type: ecs.n1.small
    group_id: xxxxxxxxxx
    host_name: myhost
    password: mypassword
  tasks:
    - name: tagging and host name password
      ecs:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        image: '{{ image }}'
        instance_type: '{{ instance_type }}'
        assign_public_ip: yes
        group_id: '{{ group_id }}'
        instance_tags:
            - tag_key : postgress
              tag_value: 1
        host_name: '{{ host_name }}'
        password: '{{ password }}'
        wait: yes
        wait_timeout: 500

# single instance with internet data configuration and instance details
- name: advanced provisioning example
  hosts: localhost
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-beijing
    image: ubuntu1404_64_40G_cloudinit_20160727.raw
    instance_type: ecs.n1.small
    group_id: xxxxxxxxxx
    instance_name: myinstance
    description: my description
  tasks:
    - name: internet data configuration and instance details
      ecs:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        image: '{{ image }}'
        instance_type: '{{ instance_type }}'
        group_id: '{{ group_id }}'
        instance_name: '{{ instance_name }}'
        description: '{{ description }}'
        internet_data:
            charge_type: PayByBandwidth
            max_bandwidth_in: 200
            max_bandwidth_out: 50


# single instance with additional volume from snapshot and volume delete on termination
- name: advanced provisioning example
  hosts: localhost
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-beijing
    image: ubuntu1404_64_40G_cloudinit_20160727.raw
    instance_type: ecs.n1.small
  tasks:
    - name: additional volume
      ecs:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        image: '{{ image }}'
        instance_type: '{{ instance_type }}'
        assign_public_ip: yes
        volumes:
          - disk_name: /dev/sdb
            snapshot_id: xxxxxxxxxx
            disk_category: cloud_efficiency
            disk_size: 100
            delete_on_termination: true

# example with system disk configuration and IO optimized
- name: advanced provisioning example
  hosts: localhost
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-beijing
    image: ubuntu1404_64_40G_cloudinit_20160727.raw
    instance_type: ecs.n1.small
    io_optimized: yes
    system_disk:
      disk_category: cloud_efficiency
      disk_size: 100
      disk_name: DiskName
      disk_description: Disk Description
  tasks:
    - name: additional volume
      ecs:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        image: '{{ image }}'
        instance_type: '{{ instance_type }}'
        io_optimized: '{{ io_optimized }}'
        system_disk: '{{ system_disk }}'

# example with prepaid internet charge type configuration
- name: advanced provisioning example
  hosts: localhost
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-beijing
    image: ubuntu1404_64_40G_cloudinit_20160727.raw
    instance_type: ecs.n1.small
  tasks:
    - name: prepaid internet charge type configuration
      ecs:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        image: '{{ image }}'
        instance_type: '{{ instance_type }}'
        assign_public_ip: yes
        instance_charge_type: PrePaid
        period: 1
        auto_renew: yes
        auto_renew_period: 3

#
# modifying attributes of ecs instance
#
- name: modify attribute example
  hosts: localhost
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-beijing
  tasks:
    - name: modify attribute of multiple instances
      ecs:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        attributes:
            - id:  xxxxxxxxxx
              name: InstanceName
              description: volume attributes
              password: mypassword
              host_name: hostName
            - id:  xxxxxxxxxx
              name: InstanceName
              description: volume attributes
              password: mypassword
              host_name: hostcomes

#
# querying instance status
#
- name: query instance status
  hosts: localhost
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-beijing
    zone: cn-beijing-a
    status: getstatus
    pagenumber: 1
    pagesize: 10
  tasks:
    - name: query instance status from the particular zone
      ecs:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        zone: '{{ zone }}'
        status: '{{ status }}'
        pagenumber: '{{ pagenumber }}'
        pagesize: '{{ pagesize }}'

#
# start or terminate instance
#
- name: start or terminate instance
  hosts: localhost
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-shenzhen
    instance_ids: xxxxxxxxxx
    instance_tags:
    - tag_key: xz_test
      tag_value: '1.20'
    status: running
  tasks:
    - name: start instance
      ecs_model:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        instance_ids: '{{ instance_ids }}'
        instance_tags: '{{ instance_tags }}'
        status: '{{ status }}'

#
# stop or restarted instance
#
- name: start stop restart instance
  hosts: localhost
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-shenzhen
    instance_ids: xxxxxxxxxx
    instance_tags:
    - tag_key: xz_test
      tag_value: '1.20'
    force: False
    status: restarted
  tasks:
    - name: Restart instance
      ecs_model:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        instance_ids: '{{ instance_ids }}'
        instance_tags: '{{ instance_tags }}'
        status: '{{ status }}'

#
# add an instance to security group
#
- name: Add an instance to security group
  hosts: localhost
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-shenzhen
    instance_id: xxxxxxxxxx
    group_id: xxxxxxxxxx
    sg_action: join
  tasks:
    - name: Add an instance to security group
      ecs_model:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        instance_id: '{{ instance_id }}'
        group_id: '{{ group_id }}'
        sg_action: '{{ sg_action }}'

#
# remove instance from security group
#
- name: Remove an instance from security group
  hosts: localhost
  vars:
    acs_access_key: xxxxxxxxxx
    acs_secret_access_key: xxxxxxxxxx
    region: cn-shenzhen
    instance_id: xxxxxxxxxx
    group_id: xxxxxxxxxx
    sg_action: leave
  tasks:
    - name: Remove an instance from security group
      ecs_model:
        acs_access_key: '{{ acs_access_key }}'
        acs_secret_access_key: '{{ acs_secret_access_key }}'
        region: '{{ region }}'
        instance_id: '{{ instance_id }}'
        group_id: '{{ group_id }}'
        sg_action: '{{ sg_action }}'
'''