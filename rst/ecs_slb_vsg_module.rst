.. _ecs_slb_vsg:


ecs_slb_vsg - Create, set and Delete VServer Group, add, remove, modify VServer Group Backend Server
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Create, set and Delete VServer Group
* Add, remove and modify VServer Group Backend Server


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
        <td><div>Aliyun Cloud access key. If not set then the value of the `ACS_ACCESS_KEY_ID`, `ACS_ACCESS_KEY` or `ECS_ACCESS_KEY` environment variable is used.</div></br>
        <div style="font-size: small;">aliases: ecs_access_key, access_key<div></td></tr>
            <tr>
    <td>acs_secret_access_key<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Aliyun Cloud secret key. If not set then the value of the `ACS_SECRET_ACCESS_KEY`, `ACS_SECRET_KEY`, or `ECS_SECRET_KEY` environment variable is used.</div></br>
        <div style="font-size: small;">aliases: ecs_secret_key, secret_key<div></td></tr>
            <tr>
    <td>backend_servers<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>List of hash/dictionary of backend servers to add or set in (see example)</div></td></tr>
            <tr>
    <td>load_balancer_id<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The unique ID of a Server Load Balancer instance</div></br>
        <div style="font-size: small;">aliases: ecs_slb<div></td></tr>
            <tr>
    <td>purge_backend_servers<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>List of hash/dictionary of backend servers to delete (see example)</div></td></tr>
            <tr>
    <td>region<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The Aliyun Cloud region to use. If not specified then the value of the `ACS_REGION`, `ACS_DEFAULT_REGION` or `ECS_REGION` environment variable, if any, is used.</div></br>
        <div style="font-size: small;">aliases: acs_region, ecs_region<div></td></tr>
            <tr>
    <td>status<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>present</li><li>absent</li></ul></td>
        <td><div>To create VServer Group, provide state as ‘present’</div></br>
        <div style="font-size: small;">aliases: state<div></td></tr>
            <tr>
    <td>vserver_group_id<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The unique identifier for the virtual server group</div></td></tr>
            <tr>
    <td>vserver_group_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Virtual server group name</div></td></tr>
        </table>
    </br>



Examples
--------

 ::

    #
    # Provisioning new VServer Group
    #
    
    Basic provisioning example to create vserver group and add backend server
    - name: create vserver group and add backend server
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-shenzhen
        status: present
        load_balancer_id: xxxxxxxxxx
        vserver_group_name : test
        backend_servers:
           -  server_id: xxxxxxxxxx
              port: 8085
              weight: 95
      tasks:
        - name: create vserver group and add backend server
          ecs_slb_vsg:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            status: '{{ status }}'
            load_balancer_id: '{{ load_balancer_id }}'
            vserver_group_name: '{{ vserver_group_name }}'
            backend_servers: '{{ backend_servers }}'
    
    Basic provisioning example add backend server to vserver group
    - name: add backend server to vserver group
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-shenzhen
        status: present
        vserver_group_id: xxxxxxxxxx
        backend_servers:
           -  server_id: xxxxxxxxxx
              port: 8085
              weight: 95
      tasks:
        - name: add backend server to vserver group
          ecs_slb_vsg:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            status: '{{ status }}'
            vserver_group_id: '{{ vserver_group_id }}'
            backend_servers: '{{ backend_servers }}'
    
    
    Provisioning example set vserver group backend server
    - name: set vserver group backend server
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-shenzhen
        status: present
        vserver_group_id: xxxxxxxxxx
        vserver_group_name : testa
        backend_servers:
           -  server_id: xxxxxxxxxx
              port: 8085
              weight: 95
      tasks:
        - name: set vserver group backend server
          ecs_slb_vsg:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            status: '{{ status }}'
            vserver_group_id: '{{ vserver_group_id}}'
            vserver_group_name: '{{ vserver_group_name }}'
            backend_servers: '{{ backend_servers }}'
    
    
    # Provisioning example to remove vserver group backend server
    - name: remove vserver group backend server
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-shenzhen
        status: present
        vserver_group_id: xxxxxxxxxx
        purge_backend_servers:
           -  server_id: xxxxxxxxxx
              port: 8085
      tasks:
        - name: remove vserver group backend server
          ecs_slb_vsg:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            status: '{{ status }}'
            vserver_group_id: '{{ vserver_group_id }}'
            purge_backend_servers: '{{ purge_backend_servers }}'
    
    
    # Provisioning example to modifying vserver group backend server
    - name: modifying vserver group backend server
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-shenzhen
        status: present
        vserver_group_id: xxxxxxxxxx
        purge_backend_servers:
           -  server_id: xxxxxxxxxx
              port: 8085
        backend_servers:
           -  server_id: xxxxxxxxxx
              port: 8085
              weight: 95
      tasks:
        - name: modifying vserver group backend server
          ecs_slb_vsg:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            status: '{{ status }}'
            vserver_group_id: '{{ vserver_group_id }}'
            purge_backend_servers: '{{ purge_backend_servers }}'
            backend_servers: '{{ backend_servers }}'
    
    # Provisioning example to delete vserver group
    - name: delete vserver group
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-shenzhen
        status: absent
        vserver_group_id: xxxxxxxxxx
      tasks:
        - name: delete vserver group
          ecs_slb_vsg:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            status: '{{ status }}'
            vserver_group_id: '{{ vserver_group_id }}'


Notes
-----

.. note:: If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence ``ACS_ACCESS_KEY_ID`` or ``ACS_ACCESS_KEY`` or ``ECS_ACCESS_KEY``, ``ACS_SECRET_ACCESS_KEY`` or ``ACS_SECRET_KEY`` or ``ECS_SECRET_KEY``, ``ACS_REGION`` or ``ACS_DEFAULT_REGION`` or ``ECS_REGION``



Status
~~~~~~

This module is flagged as **stableinterface** which means that the maintainers for this module guarantee that the no backward incompatible interface changes will be made.


Support
~~~~~~~

This module is maintained by those with core commit privileges





