.. _ecs_slb_lb:


ecs_slb_lb - Create, Delete, Enable or Disable Server Load Balancer in ECS
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Create, Delete, Enable or Disable Server Load Balancer in ECS


Requirements (on host that executes module)
-------------------------------------------

  * python >= 2.7
  * aliyun-python-sdk-core, aliyun-python-sdk-ecs, aliyun-python-sdk-slb, ecsutils and footmark


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
    <td>address_type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>internet</td>
        <td><ul><li>internet</li><li>intranet</li></ul></td>
        <td><div>The address type of the SLB</div></br>
        <div style="font-size: small;">aliases: scheme<div></td></tr>
            <tr>
    <td>bandwidth<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>1</td>
        <td><ul><li>1-1000 Mbps</li></ul></td>
        <td><div>Bandwidth peak of the public network instance charged per fixed bandwidth</div></td></tr>
            <tr>
    <td>instance_ids<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>List of instance ids to attach to this SLB</div></td></tr>
            <tr>
    <td>internet_charge_type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>paybytraffic</td>
        <td><ul><li>paybybandwidth</li><li>paybytraffic</li></ul></td>
        <td><div>Charging mode for the public network instance</div></td></tr>
            <tr>
    <td>listeners<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>List of ports/protocols for this SLB to listen on (see example)</div></td></tr>
            <tr>
    <td>load_balancer_id<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The List of unique ID of a Server Load Balancer instance</div></br>
        <div style="font-size: small;">aliases: ecs_slb<div></td></tr>
            <tr>
    <td>load_balancer_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The name of the server load balancer</div></br>
        <div style="font-size: small;">aliases: name<div></td></tr>
            <tr>
    <td>master_zone_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The main usable area ID of the created Load Balancer can be found by the DescribeZone interface</div></td></tr>
            <tr>
    <td>purge_instance_ids<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>True</td>
        <td><ul></ul></td>
        <td><div>Purge existing instance ids on SLB that are not found in instance_ids</div></td></tr>
            <tr>
    <td>purge_listeners<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>True</td>
        <td><ul></ul></td>
        <td><div>Purge existing listeners on SLB that are not found in listeners</div></td></tr>
            <tr>
    <td>region<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The Aliyun Cloud region to use. If not specified then the value of the 'ACS_REGION', 'ACS_DEFAULT_REGION' or 'ECS_REGION' environment variable, if any, is used.</div></br>
        <div style="font-size: small;">aliases: acs_region, ecs_region<div></td></tr>
            <tr>
    <td>slave_zone_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The ID of the standby zone of the created Load Balancer can be found on the DescribeZone interface</div></td></tr>
            <tr>
    <td>status<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>present</li><li>absent</li><li>active</li><li>inactive</li></ul></td>
        <td><div>For creating new Server Load Balancer</div></br>
        <div style="font-size: small;">aliases: state<div></td></tr>
            <tr>
    <td>tags<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>An associative array of stickness policy settings. Policy will be applied to all listeners</div></td></tr>
            <tr>
    <td>validate_certs<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>When set to "no", SSL certificates will not be validated</div></td></tr>
            <tr>
    <td>vswitch_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The vswitch id of the VPC instance</div></br>
        <div style="font-size: small;">aliases: subnet_id, subnet<div></td></tr>
            <tr>
    <td>wait<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>no</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Wait for the SLB instance to be 'running' before returning</div></td></tr>
            <tr>
    <td>wait_timeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>300</td>
        <td><ul></ul></td>
        <td><div>how long before wait gives up, in seconds</div></td></tr>
        </table>
    </br>



Examples
--------

 ::

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


Notes
-----

.. note:: If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence ``ACS_ACCESS_KEY_ID`` or ``ACS_ACCESS_KEY`` or ``ECS_ACCESS_KEY``, ``ACS_SECRET_ACCESS_KEY`` or ``ACS_SECRET_KEY`` or ``ECS_SECRET_KEY``, ``ACS_REGION`` or ``ACS_DEFAULT_REGION`` or ``ECS_REGION``



Status
~~~~~~

This module is flagged as **stableinterface** which means that the maintainers for this module guarantee that the no backward incompatible interface changes will be made.


Support
~~~~~~~

This module is maintained by those with core commit privileges





