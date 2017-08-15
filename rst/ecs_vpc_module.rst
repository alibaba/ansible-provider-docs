.. _ecs_vpc:


ecs_vpc - Create/Delete Vpc and Vswitch, Querying Vswitch and VRouter and Adding Route Entry
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Create/Delete Vpc and Vswitch, Querying Vswitch and VRouter and Adding Route Entry


Requirements (on host that executes module)
-------------------------------------------

  * python >= 2.7
  * aliyun-python-sdk-core, aliyun-python-sdk-ecs, ecsutils and footmark


Options
-------

.. raw:: html

    <table border=1 cellpadding=4>
    <tr>
    <th class="head">parameter</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>
            <tr>
    <td>acs_access_key<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Aliyun Cloud access key. If not set then the value of the 'ACS_ACCESS_KEY_ID', 'ACS_ACCESS_KEY' or 'ECS_ACCESS_KEY' environment variable is used.</div></br>
        <div style="font-size: small;">aliases: ecs_access_key, access_key<div></td></tr>
            <tr>
    <td>acs_secret_access_key<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Aliyun Cloud secret key. If not set then the value of the 'ACS_SECRET_ACCESS_KEY', 'ACS_SECRET_KEY', or 'ECS_SECRET_KEY' environment variable is used.</div></br>
        <div style="font-size: small;">aliases: ecs_secret_key, secret_key<div></td></tr>
            <tr>
    <td>cidr_block<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>172.16.0.0/16</td>
        <td><ul></ul></td>
        <td><div>The CIDR block representing the VPC, e.g. 10.0.0.0/8. Value options- 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16</div></td></tr>
            <tr>
    <td>description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The description. The default value is blank. [2, 256] English or Chinese characters. Cannot begin with http:// or https://</div></td></tr>
            <tr>
    <td>pagenumber<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>1</td>
        <td><ul></ul></td>
        <td><div>Page number of the instance status list. The start value is 1.</div></td></tr>
            <tr>
    <td>pagesize<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>10</td>
        <td><ul></ul></td>
        <td><div>The number of lines per page set for paging query. The maximum value is 50.</div></td></tr>
            <tr>
    <td>purge_routes<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>A dictionary array of route tables to add in VPC</div></td></tr>
            <tr>
    <td>purge_vswitches<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>A dictionary array of route tables to remove from VPC</div></td></tr>
            <tr>
    <td>region<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The Aliyun Cloud region to use. If not specified then the value of the 'ACS_REGION', 'ACS_DEFAULT_REGION' or 'ECS_REGION' environment variable, if any, is used.</div></br>
        <div style="font-size: small;">aliases: acs_region, ecs_region<div></td></tr>
            <tr>
    <td>route_entries<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>A dictionary array of route tables to add or remove from VPC (see example)</div></td></tr>
            <tr>
    <td>status<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>present</li><li>absent</li><li>getinfo_vroute</li><li>describe_vswitch</li></ul></td>
        <td><div>Create/delete Vpc and Vswitch, Querying Vswitch and VRouter and Adding Route Entry</div></br>
        <div style="font-size: small;">aliases: state<div></td></tr>
            <tr>
    <td>user_cidr<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>User custom cidr in the VPC</div></td></tr>
            <tr>
    <td>vpc_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The unique ID of a VPC</div></td></tr>
            <tr>
    <td>vpc_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>name</li></ul></td>
        <td><div>The VPC name. The default value is blank. [2, 128] English or Chinese characters, must begin with an uppercase/ lowercase letter or Chinese character. Can contain numbers, '_' and '-'. The disk description will appear on the console. Cannot begin with http:// or https://</div></td></tr>
            <tr>
    <td>vrouter_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The ID of the VRouter to be queried</div></td></tr>
            <tr>
    <td>vswitch_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The ID of the VSwitch to be queried</div></br>
        <div style="font-size: small;">aliases: subnet<div></td></tr>
            <tr>
    <td>vswitches<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>List of hash/dictionary of route tables to add in VPC (see example)</div></td></tr>
            <tr>
    <td>wait<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>True</li><li>False</li></ul></td>
        <td><div>Wait for the VPC instance to be 'running' before returning.</div></td></tr>
            <tr>
    <td>wait_timeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>300</td>
        <td><ul></ul></td>
        <td><div>How long before wait gives up, in seconds</div></td></tr>
            <tr>
    <td>zone_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The id of a zone.</div></br>
        <div style="font-size: small;">aliases: zone<div></td></tr>
        </table>
    </br>



Examples
--------

 ::

    #
    # provisioning to create vpc in VPC
    #
    
    # basic provisioning example to create vpc in VPC
    - name: create vpc
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        status: present
        cidr_block: 192.168.0.0/16
        vpc_name: Demo_VPC
        description: Demo VPC
        vswitches:
          - zone_id: 'cn-hongkong-b'
            description: 'dummy'
            cidr_block: '172.16.0.0/24'
      tasks:
        - name: create vpc
          ecs_vpc:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            status: '{{ status }}'
            cidr_block: '{{ cidr_block }}'
            vpc_name: '{{ vpc_name }}'
            description: '{{ description }}'
            vswitches: '{{ vswitches }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to delete vpc
    - name: delete vpc
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
      tasks:
        - name: delete vpc
          ecs_vpc:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            state: absent
            vpc_id: xxxxxxxxxx
          register: result
        - debug: var=result
    
    # basic provisioning example to create vswitch
    - name: create vswitch
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        vpc_id: xxxxxxxxxx
        vswitches:
          - zone_id: cn-hongkong-b
            cidr_block: '172.16.0.0/24'
            name: 'Demo_VSwitch'
            description: 'akashhttp://'
        state: present
      tasks:
        - name: create vswitch
          ecs_vpc:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            vswitches: '{{ vswitches }}'
            vpc_id: '{{ vpc_id }}'
            state: '{{ state }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to delete vswitch
    - name: delete vswitch
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        vpc_id: xxxxxxxxxx
        purge_vswitches:
         - xxxxxxxxxx
        state: present
      tasks:
        - name: delete vswitch
          ecs_vpc:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            vpc_id: '{{ vpc_id }}'
            purge_vswitches: '{{ purge_vswitches }}'
            state: '{{ state }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to create custom route
    - name: create vpc
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        state: present
        vpc_id: xxxxxxxxxx
        route_entries:
          - destination_cidrblock: '192.168.4.0/24'
            next_hop_id: 'xxxxxxxxxx'
      tasks:
        - name: create vpc
          ecs_vpc:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            state: '{{ state }}'
            route_entries: '{{ route_entries }}'
            vpc_id: '{{ vpc_id }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to delete custom route
    - name: delete route
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        vpc_id: vpc-j6cjkmappmgb4fywpbj0u
        purge_routes:
             destination_cidrblock: "192.168.4.0/24"
             next_hop_id: "xxxxxxxxxx"
        state: present
      tasks:
        - name: delete route
          ecs_vpc:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            purge_routes: '{{ purge_routes }}'
            state: '{{ state }}'
            vpc_id: '{{ vpc_id }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to querying vroute
    - name: get vrouter list
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        vrouter_id: xxxxxxxxxx
        pagenumber: 1
        pagesize: 10
        state: getinfo_vroute
      tasks:
        - name: get vrouter list
          ecs_vpc:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            vrouter_id: '{{ vrouter_id }}'
            state: '{{ state }}'
            pagenumber: '{{ pagenumber }}'
            pagesize: '{{ pagesize }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to querying vswitch
    - name: querying vswitch status
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: ap-southeast-1
        status: getinfo_vswitch
        zone_id: ap-southeast-1a
        vpc_id: xxxxxxxxxx
        vswitch_id: xxxxxxxxxx
        page_size: 10
        page_number: 1
      tasks:
        - name: querying instance status
          ecs_vpc:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            status: '{{ status }}'
            zone_id: '{{ zone_id }}'
            vpc_id: '{{ vpc_id }}'
            vswitch_id: '{{ vswitch_id }}'
            page_size: '{{ page_size }}'
            page_number: '{{ page_number }}'
          register: result
        - debug: var=result
    


Notes
-----

.. note:: If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence ``ACS_ACCESS_KEY_ID`` or ``ACS_ACCESS_KEY`` or ``ECS_ACCESS_KEY``, ``ACS_SECRET_ACCESS_KEY`` or ``ACS_SECRET_KEY`` or ``ECS_SECRET_KEY``, ``ACS_REGION`` or ``ACS_DEFAULT_REGION`` or ``ECS_REGION``



Status
~~~~~~

This module is flagged as **stableinterface** which means that the maintainers for this module guarantee that the no backward incompatible interface changes will be made.


Support
~~~~~~~

This module is maintained by those with core commit privileges





