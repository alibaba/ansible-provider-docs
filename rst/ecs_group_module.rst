.. _ecs_group:


ecs_group - Create, Query or Delete Security Group
++++++++++++++++++++++++++++++++++++++++++++++++++



.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Create, Query or Delete Security Group


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
    <td>description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The description of the security group.</div></td></tr>
            <tr>
    <td>group_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Provide the security group id to perform rules authorization. This parameter is not required for creating new security group.</div></br>
        <div style="font-size: small;">aliases: security_group_id, group_ids, security_group_ids<div></td></tr>
            <tr>
    <td>group_tags<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>A list of hash/dictionaries of group tags, ['{"tag_key":"value", "tag_value":"value"}'], tag_key must be not null when tag_value isn't null</div></td></tr>
            <tr>
    <td>region<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The Aliyun Cloud region to use. If not specified then the value of the `ACS_REGION`, `ACS_DEFAULT_REGION` or `ECS_REGION` environment variable, if any, is used.</div></br>
        <div style="font-size: small;">aliases: acs_region, ecs_region<div></td></tr>
            <tr>
    <td>rules<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>List of firewall inbound rules to enforce in this group. (see example)</div></td></tr>
            <tr>
    <td>rules_egress<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>List of firewall outbound rules to enforce in this group. (see example)</div></td></tr>
            <tr>
    <td>security_group_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The security group name.</div></br>
        <div style="font-size: small;">aliases: name<div></td></tr>
            <tr>
    <td>status<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>present</li><li>absent</li><li>getinfo</li></ul></td>
        <td><div>For creating new security group and/or authorizing.</div></br>
        <div style="font-size: small;">aliases: state<div></td></tr>
            <tr>
    <td>vpc_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The ID of the VPC to which the security group belongs. If this parameter is not passed, the security group will be created using classic network type.</div></td></tr>
        </table>
    </br>



Examples
--------

 ::

    #
    # Provisioning new Security Group
    #
    
    Basic provisioning example to create security group
    - name: create security group
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-shenzhen
      tasks:
        - name: create security grp
          ecs_group:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            security_group_name: 'AliyunSG'
          register: result_details
        - debug: var=result_details
    
    
    Basic provisioning example authorize security group
    - name: authorize security grp
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-shenzhen
      tasks:
        - name: authorize security group
          ecs_group:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            security_group_id: xxxxxxxxxx
            region: '{{ region }}'
            rules:
              - ip_protocol: tcp
                port_range: 1/122
                source_cidr_ip: '10.159.6.18/12'
            rules_egress:
              - proto: all
                port_range: -1/-1
                dest_group_id: xxxxxxxxxx
                nic_type: intranet
          register: result_details
        - debug: var=result_details
    
    
    Provisioning example create and authorize security group
    - name: create and authorize security group
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-shenzhen
      tasks:
        - name: create and authorize security grp
          ecs_group:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            security_group_name: 'AliyunSG'
            description: 'an example ECS group'
            region: '{{ region }}'
            rules:
              - ip_protocol: tcp
                port_range: 1/122
                source_cidr_ip: '10.159.6.18/12'
                priority: 10
                policy: drop
                nic_type: intranet
            rules_egress:
              - proto: all
                port_range: -1/-1
                dest_group_id: xxxxxxxxxx
                group_owner_id: xxxxxxxxxx
                priority: 10
                policy: accept
                nic_type: intranet
          register: result_details
        - debug: var=result_details
    
    
    # Provisioning example to delete security group
    - name: delete security grp
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: us-west-1
        security_group_ids:
         - xxxxxxxxxx
        status: absent
      tasks:
        - name: delete security grp
          ecs_group:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            security_group_ids: '{{ security_group_ids }}'
            status: '{{ status }}'
          register: result
        - debug: var=result
    
    
    # Provisioning example to querying security group list
    - name: querying security group list
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-beijing
        status: getinfo
      tasks:
        - name: Querying Security group list
          ecs_group:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            status: '{{ status }}'
          register: result


Notes
-----

.. note:: If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence ``ACS_ACCESS_KEY_ID`` or ``ACS_ACCESS_KEY`` or ``ECS_ACCESS_KEY``, ``ACS_SECRET_ACCESS_KEY`` or ``ACS_SECRET_KEY`` or ``ECS_SECRET_KEY``, ``ACS_REGION`` or ``ACS_DEFAULT_REGION`` or ``ECS_REGION``



Status
~~~~~~

This module is flagged as **stableinterface** which means that the maintainers for this module guarantee that the no backward incompatible interface changes will be made.


Support
~~~~~~~

This module is maintained by those with core commit privileges





