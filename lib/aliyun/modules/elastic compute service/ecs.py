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
short_description: create, start, stop, restart or terminate an instance in ecs
description:
    - Creates or terminates ecs instances.
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
    choices: ['present', 'pending', 'running', 'stopped', 'restarted', 'absent', 'getstatus']
  zone_id:
    description: Aliyun availability zone ID in which to launch the instance
    required: false
    default: null
    aliases: [ 'acs_zone', 'ecs_zone', 'zone']
  image_id:
    description: Image ID to use for the instance.
    required: true
    default: null
    aliases: ['image']
  instance_type:
    description: Instance type to use for the instance.
    required: true
    default: null
    aliases: [ 'type' ]
  group_id:
    description: Security group id to use with the instance
    required: false
    default: null
    aliases: []
  io_optimized:
    description: Whether instance is using optimized volumes.
    required: false
    default: False
    aliases: []
    choices: [true, false]
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
            - max_bandwidth_out(required=false, default=0).
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
            - device_category (required=false; default="cloud"; choices=["cloud", "cloud_efficiency", "cloud_ssd", "ephemeral_ssd"] )
            - device_size (required=false; default=null; choices=depends on disk_category)
            - device_size (required=false; default=null; choices=depends on disk_category)
            - device_name (required=false; default=null)
            - device_description (required=false; default=null)
            - delete_on_termination (required=false, default="true")
            - snapshot (required=false; default=null), volume_type (str), iops (int) - device_type is deprecated use volume_type, iops must be set when volume_type='io1', ephemeral and snapshot are mutually exclusive.
      required: false
      default: null
      aliases: ['volumes']
  count:
      description:
        - The number of the new instance.
      required: false
      default: 1
      aliases: []
  allocate_public_ip:
      description:
        - Whether allocate a public ip for the new instance.
      required: false
      default: "true"
      aliases: ['assign_public_ip']
  bind_eip:
      description:
        - ID of Elastic IP Address bind to the new instance.
      required: false
      default: null
      aliases: []
  private_ip:
      description:
        - Private IP address for the new instance.
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
      choices: [1-12]
      default: null
  auto_renew:
      description:
        - Whether automate renew the charge of the instance.
      required: false
      choices: [true, false]
      default: "false"
  auto_renew_period:
      description:
        - The duration of the automatic renew the charge of the instance. It is vaild when auto_renew is true.
      required: false
      choices: [1, 2, 3, 6, 12]
      default: "false"
  ids:
      description:
        - A list of identifier for this instance or set of instances, so that the module will be idempotent with respect to ECS instances. This identifier should not be reused for another call later on. For details, see the description of client token at U(https://help.aliyun.com/document_detail/25693.html?spm=5176.doc25499.2.7.mrVgE2).
        - The length of the ids is the same with count
      required: false
      default: null
  wait:
      description:
        - Wait for the instance to be 'running' before returning.
      required: false
      choices: [true, false]
      default: "false"
  wait_timeout:
      description:
        - how long before wait gives up, in seconds
      required: false
      choices: []
      default: "300"
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
# Note: These examples do not set authentication details.
# Basic provisioning example
- ecs:
    key_name: mykey
    instance_type: t2.micro
    image: ami-123456
    wait: yes
    group: webserver
    count: 3
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes
# Advanced example with tagging and CloudWatch
- ecs:
    key_name: mykey
    group: databases
    instance_type: t2.micro
    image: ami-123456
    wait: yes
    wait_timeout: 500
    count: 5
    instance_tags:
       db: postgres
    monitoring: yes
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes
# Single instance with additional IOPS volume from snapshot and volume delete on termination
- ecs:
    key_name: mykey
    group: webserver
    instance_type: c3.medium
    image: ami-123456
    wait: yes
    wait_timeout: 500
    volumes:
      - device_name: /dev/sdb
        snapshot: snap-abcdef12
        volume_type: io1
        iops: 1000
        volume_size: 100
        delete_on_termination: true
    monitoring: yes
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes
# Single instance with ssd gp2 root volume
- ecs:
    key_name: mykey
    group: webserver
    instance_type: c3.medium
    image: ami-123456
    wait: yes
    wait_timeout: 500
    volumes:
      - device_name: /dev/xvda
        volume_type: gp2
        volume_size: 8
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes
    exact_count: 1
# Multiple groups example
- ecs:
    key_name: mykey
    group: ['databases', 'internal-services', 'sshable', 'and-so-forth']
    instance_type: m1.large
    image: ami-6e649707
    wait: yes
    wait_timeout: 500
    count: 5
    instance_tags:
        db: postgres
    monitoring: yes
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes
# Multiple instances with additional volume from snapshot
- ecs:
    key_name: mykey
    group: webserver
    instance_type: m1.large
    image: ami-6e649707
    wait: yes
    wait_timeout: 500
    count: 5
    volumes:
    - device_name: /dev/sdb
      snapshot: snap-abcdef12
      volume_size: 10
    monitoring: yes
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes
# Dedicated tenancy example
- local_action:
    module: ecs
    assign_public_ip: yes
    group_id: sg-1dc53f72
    key_name: mykey
    image: ami-6e649707
    instance_type: m1.small
    tenancy: dedicated
    vpc_subnet_id: subnet-29e63245
    wait: yes
# Spot instance example
- ecs:
    spot_price: 0.24
    spot_wait_timeout: 600
    keypair: mykey
    group_id: sg-1dc53f72
    instance_type: m1.small
    image: ami-6e649707
    wait: yes
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes
    spot_launch_group: report_generators
# Examples using pre-existing network interfaces
- ecs:
    key_name: mykey
    instance_type: t2.small
    image: ami-f005ba11
    network_interface: eni-deadbeef
- ecs:
    key_name: mykey
    instance_type: t2.small
    image: ami-f005ba11
    network_interfaces: ['eni-deadbeef', 'eni-5ca1ab1e']
# Launch instances, runs some tasks
# and then terminate them
- name: Create a sandbox instance
  hosts: localhost
  gather_facts: False
  vars:
    key_name: my_keypair
    instance_type: m1.small
    security_group: my_securitygroup
    image: my_ami_id
    region: us-east-1
  tasks:
    - name: Launch instance
      ecs:
         key_name: "{{ keypair }}"
         group: "{{ security_group }}"
         instance_type: "{{ instance_type }}"
         image: "{{ image }}"
         wait: true
         region: "{{ region }}"
         vpc_subnet_id: subnet-29e63245
         assign_public_ip: yes
      register: ecs
    - name: Add new instance to host group
      add_host:
        hostname: "{{ item.public_ip }}"
        groupname: launched
      with_items: "{{ ecs.instances }}"
    - name: Wait for SSH to come up
      wait_for:
        host: "{{ item.public_dns_name }}"
        port: 22
        delay: 60
        timeout: 320
        state: started
      with_items: "{{ ecs.instances }}"
- name: Configure instance(s)
  hosts: launched
  become: True
  gather_facts: True
  roles:
    - my_awesome_role
    - my_awesome_test
- name: Terminate instances
  hosts: localhost
  connection: local
  tasks:
    - name: Terminate instances that were previously launched
      ecs:
        state: 'absent'
        instance_ids: '{{ ecs.instance_ids }}'
# Start a few existing instances, run some tasks
# and stop the instances
- name: Start sandbox instances
  hosts: localhost
  gather_facts: false
  connection: local
  vars:
    instance_ids:
      - 'i-xxxxxx'
      - 'i-xxxxxx'
      - 'i-xxxxxx'
    region: us-east-1
  tasks:
    - name: Start the sandbox instances
      ecs:
        instance_ids: '{{ instance_ids }}'
        region: '{{ region }}'
        state: running
        wait: True
        vpc_subnet_id: subnet-29e63245
        assign_public_ip: yes
  roles:
    - do_neat_stuff
    - do_more_neat_stuff
- name: Stop sandbox instances
  hosts: localhost
  gather_facts: false
  connection: local
  vars:
    instance_ids:
      - 'i-xxxxxx'
      - 'i-xxxxxx'
      - 'i-xxxxxx'
    region: us-east-1
  tasks:
    - name: Stop the sandbox instances
      ecs:
        instance_ids: '{{ instance_ids }}'
        region: '{{ region }}'
        state: stopped
        wait: True
        vpc_subnet_id: subnet-29e63245
        assign_public_ip: yes
#
# Start stopped instances specified by tag
#
- local_action:
    module: ecs
    instance_tags:
        Name: ExtraPower
    state: running
#
# Restart instances specified by tag
#
- local_action:
    module: ecs
    instance_tags:
        Name: ExtraPower
    state: restarted
#
# Enforce that 5 instances with a tag "foo" are running
# (Highly recommended!)
#
- ecs:
    key_name: mykey
    instance_type: c1.medium
    image: ami-40603AD1
    wait: yes
    group: webserver
    instance_tags:
        foo: bar
    exact_count: 5
    count_tag: foo
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes
#
# Enforce that 5 running instances named "database" with a "dbtype" of "postgres"
#
- ecs:
    key_name: mykey
    instance_type: c1.medium
    image: ami-40603AD1
    wait: yes
    group: webserver
    instance_tags:
        Name: database
        dbtype: postgres
    exact_count: 5
    count_tag:
        Name: database
        dbtype: postgres
    vpc_subnet_id: subnet-29e63245
    assign_public_ip: yes
#
# count_tag complex argument examples
#
    # instances with tag foo
    count_tag:
        foo:
    # instances with tag foo=bar
    count_tag:
        foo: bar
    # instances with tags foo=bar & baz
    count_tag:
        foo: bar
        baz:
    # instances with tags foo & bar & baz=bang
    count_tag:
        - foo
        - bar
        - baz: bang
'''