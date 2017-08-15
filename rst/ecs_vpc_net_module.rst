.. _ecs_vpc_net:


ecs_vpc_net - Request, Bind, Unbind, Modify and Release EIP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Request, Bind, Unbind, Modify and Release EIP


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
    <td>allocation_id<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The allocation ID of the EIP to be bound or unbound. The allocation ID uniquely identifies the EIP</div></td></tr>
            <tr>
    <td>bandwidth<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>5Mbps</td>
        <td><ul></ul></td>
        <td><div>The rate limit of the EIP</div></td></tr>
            <tr>
    <td>instance_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The ID of the ECS instance to be bound or unbound</div></td></tr>
            <tr>
    <td>internet_charge_type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>PayByBandwidth</td>
        <td><ul><li>PayByBandwidth</li><li>PayByTraffic</li></ul></td>
        <td><div>Internet charge type</div></td></tr>
            <tr>
    <td>region<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The Aliyun Cloud region to use. If not specified then the value of the 'ACS_REGION', 'ACS_DEFAULT_REGION' or 'ECS_REGION' environment variable, if any, is used.</div></br>
        <div style="font-size: small;">aliases: acs_region, ecs_region<div></td></tr>
            <tr>
    <td>status<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>present</li><li>join</li><li>absent</li><li>leave</li></ul></td>
        <td><div>Status for requesting eip addresses, bind eip, unbind eip, modify eip attributes and release eip</div></td></tr>
        </table>
    </br>



Examples
--------

 ::

    #
    # Provisioning Request, Bind, Unbind and Release EIP
    #
    
    # basic provisioning example to requesting eip addresses in EIP
    - name: requesting eip
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        internet_charge_type: PayByTraffic
        bandwidth: 5
        status: present
      tasks:
        - name: requesting eip
          ecs_vpc_net:
            acs_access_key_id: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            internet_charge_type: '{{ internet_charge_type }}'
            bandwidth: '{{ bandwidth }}'
            status: '{{ status }}'
    
    # basic provisioning example to bind eip
    - name: create disk
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        allocation_id: xxxxxxxxxx
        instance_id: xxxxxxxxxx
        status: join
      tasks:
        - name: Bind eip
          ecs_vpc_net:
            acs_access_key_id: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            allocation_id: '{{ allocation_id }}'
            instance_id: '{{ instance_id }}'
            status: '{{ status }}'
    
    # basic provisioning example to unbind eip
    - name: unbind eip
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        allocation_id: exxxxxxxxxx
        instance_id: xxxxxxxxxx
        state: leave
      tasks:
        - name: unbind eip
          ecs_vpc_net:
            acs_access_key_id: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            allocation_id: '{{ allocation_id }}'
            instance_id: '{{ instance_id }}'
            state: '{{ state }}'
    
    # basic provisioning example to modifying eip
    - name: modifying eip
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        allocation_id: xxxxxxxxxx
        bandwidth: 3
        status: present
      tasks:
        - name: Modify eip
          ecs_vpc_net:
            acs_access_key_id: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            allocation_id: '{{ allocation_id }}'
            bandwidth: '{{ bandwidth }}'
            status: '{{ status }}'
    
    # basic provisioning example to release eip
    - name: release eip
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        allocation_id: xxxxxxxxxx
        status: absent
      tasks:
        - name: release eip
          ecs_vpc_net:
            acs_access_key_id: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            allocation_id: '{{ allocation_id }}'
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





