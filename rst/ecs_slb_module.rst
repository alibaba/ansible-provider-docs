.. _ecs_slb:


ecs_slb - Creates, Sets and Remove backend servers and Describe backend servers health status of SLB
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Creates, Sets and Remove backend servers and Describe backend servers health status of SLB


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
    <td>ports<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>list ports used by the Server Load Balancer instance frontend to describe health status for</div></td></tr>
            <tr>
    <td>status<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>present</li><li>absent</li><li>check</li></ul></td>
        <td><div>Create, set, remove or describe backend server health status of an slb</div></br>
        <div style="font-size: small;">aliases: state<div></td></tr>
        </table>
    </br>



Examples
--------

 ::

    #
    # Provisioning new add or remove Backend Server from SLB
    #
    
    Basic example to add backend server to load balancer instance
    - name: add backend server
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
      tasks:
        - name: add backend server
          ecs_slb:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            load_balancer_id: 'xxxxxxxxxx'
            backend_servers:
              - server_id: xxxxxxxxxx
                weight: 70
              - server_id: xxxxxxxxxx
    
    
    Basic example to set backend server of load balancer instance
    - name: set backend server
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
      tasks:
        - name: set backend server
          ecs_slb:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            load_balancer_id: 'xxxxxxxxxx'
            backend_servers:
              - server_id: xxxxxxxxxx
                weight: 50
              - server_id: xxxxxxxxxx
                weight: 80
    
    Basic example to remove backend servers from load balancer instance
    - name: remove backend servers
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
      tasks:
        - name: remove backend servers
          ecs_slb:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            load_balancer_id: 'xxxxxxxxxx'
            status: absent
            backend_servers:
              - xxxxxxxxxx
              - xxxxxxxxxx
    
    Basic example to describe backend server health status of load balancer instance
    - name: describe backend server health status
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
      tasks:
        - name: describe backend server health status
          ecs_slb:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            status: check
            load_balancer_id: 'xxxxxxxxxx'
            ports:
              - '80'
              - '120'


Notes
-----

.. note:: If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence ``ACS_ACCESS_KEY_ID`` or ``ACS_ACCESS_KEY`` or ``ECS_ACCESS_KEY``, ``ACS_SECRET_ACCESS_KEY`` or ``ACS_SECRET_KEY`` or ``ECS_SECRET_KEY``



Status
~~~~~~

This module is flagged as **stableinterface** which means that the maintainers for this module guarantee that the no backward incompatible interface changes will be made.


Support
~~~~~~~

This module is maintained by those with core commit privileges





