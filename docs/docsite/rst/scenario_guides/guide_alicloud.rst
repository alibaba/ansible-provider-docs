Alibaba Cloud Compute Services Guide
====================================

.. _alicloud_intro:

Introduction
````````````

Ansible contains several modules for controlling and managing Alibaba Cloud Compute Services (Alicloud).  This guide
explains how to use the Alicloud Ansible modules together.

All Alicloud modules require ``footmark`` - install it on your control machine with ``pip install --no-cache-dir footmark``.

Cloud modules, including Alicloud modules, execute on your local machine (the control machine) with ``connection: local``, rather than on remote machines defined in your hosts.

Normally, you'll use the following pattern for plays that provision Alicloud resources::

    - hosts: localhost
      connection: local
      vars:
        - ...
      tasks:
        - ...

.. _alicloud_authentication:

Authentication
``````````````
The Alicloud provider accepts several ways to enter credentials for authentication. The following methods are supported, in this order, and explained below::

    - Environment variables
    - ECS Role
    - Assume role
    - Profile


Environment variables:

    You can provide your credentials via ALICLOUD_ACCESS_KEY and ALICLOUD_SECRET_KEY environment variables, representing your Alicloud access key and secret key respectively. ALICLOUD_REGION is also used, if applicable:

::

    Usage::

        $ export ALICLOUD_ACCESS_KEY="anaccesskey"
        $ export ALICLOUD_SECRET_KEY="asecretkey"
        $ export ALICLOUD_REGION="cn-beijing"


ECS Role:

    If you're running Ansible from an ECS instance with RAM Instance using RAM Role, Ansible will just access the metadata URL: http://100.100.100.200/latest/meta-data/ram/security-credentials/<ecs_role_name> to obtain the STS credential. Refer to details Access other Cloud Product APIs by the Instance RAM Role.
    This is a preferred approach over any other when running in ECS as you can avoid hard coding credentials. Instead these are leased on-the-fly by Ansible which reduces the chance of leakage.

::

    Usage::

        ecs_role_name : '{{ ansible-provider-alicloud }}'
        region        : '{{ region }}

    Note::

        You can provide your credentials via ALICLOUD_ECS_ROLE_NAME environment variables


Assume role:

    If provided with a role ARN, Ansible will attempt to assume this role using the supplied credentials.

::

    Usage::

        assume_role:
            role_arn            : "acs:ram::ACCOUNT_ID:role/ROLE_NAME"
            policy              : "POLICY"
            session_name        : "SESSION_NAME"
            session_expiration  :  999


    Note::

        You can provide your credentials via ALICLOUD_ASSUME_ROLE_ARN, ALICLOUD_ASSUME_ROLE_SESSION_NAME, ALICLOUD_ASSUME_ROLE_SESSION_EXPIRATION environment variables


Profile:

    If use Alibaba Cloud CLI and configure the credential information, Ansible will read credentials file.

::

    Usage::

        profile                 : '{{ ansible_profile }}'
        shared_credentials_file : '{{ shared_credentials_file_path }}'

    Note::

        profile is the Alicloud profile name as set in the shared credentials file. It can also be sourced from the ALICLOUD_PROFILE environment variable.
        shared_credentials_file is the path to the shared credentials file. It can also be sourced from the ALICLOUD_SHARED_CREDENTIALS_FILE environment variable. If this is not set and a profile is specified, ~/.aliyun/config.json will be used.
.. _alicloud_provisioning:

Provisioning
````````````

Alicloud modules create Alicloud ECS instances, disks, virtual private clouds, virtual switches, security groups and other resources.

You can use the ``count`` parameter to control the number of resources you create or terminate. For example, if you want exactly 5 instances tagged ``NewECS``,
set the ``count`` of instances to 5 and the ``count_tag`` to ``NewECS``, as shown in the last task of the example playbook below.
If there are no instances with the tag ``NewECS``, the task creates 5 new instances. If there are 2 instances with that tag, the task
creates 3 more. If there are 8 instances with that tag, the task terminates 3 of those instances.

If you do not specify a ``count_tag``, the task creates the number of instances you specify in ``count`` with the ``instance_name`` you provide.

::

    # alicloud_setup.yml

    - hosts: localhost
      connection: local

      tasks:

        - name: Create VPC
          ali_vpc:
            cidr_block: '{{ cidr_block }}'
            vpc_name: new_vpc
          register: created_vpc

        - name: Create VSwitch
          ali_vswitch:
            alicloud_zone: '{{ alicloud_zone }}'
            cidr_block: '{{ vsw_cidr }}'
            vswitch_name: new_vswitch
            vpc_id: '{{ created_vpc.vpc.id }}'
          register: created_vsw

        - name: Create security group
          ali_security_group:
            name: new_group
            vpc_id: '{{ created_vpc.vpc.id }}'
            rules:
              - proto: tcp
                port_range: 22/22
                cidr_ip: 0.0.0.0/0
                priority: 1
            rules_egress:
              - proto: tcp
                port_range: 80/80
                cidr_ip: 192.168.0.54/32
                priority: 1
          register: created_group

        - name: Create a set of instances
          ali_instance:
             security_groups: '{{ created_group.group_id }}'
             instance_type: ecs.n4.small
             image_id: "{{ ami_id }}"
             instance_name: "My-new-instance"
             instance_tags:
                 Name: NewECS
                 Version: 0.0.1
             count: 5
             count_tag:
                 Name: NewECS
             allocate_public_ip: true
             max_bandwidth_out: 50
             vswitch_id: '{{ created_vsw.vswitch.id}}'
          register: create_instance

In the example playbook above, data about the vpc, vswitch, group, and instances created by this playbook
are saved in the variables defined by the "register" keyword in each task.

Each Alicloud module offers a variety of parameter options. Not all options are demonstrated in the above example.
See each individual module for further details and examples.
