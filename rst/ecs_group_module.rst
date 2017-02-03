.. _ecs_disk:


ecs_disk - Create, Query or Delete Security Group
+++++++++++++++++++++++++++++++++++++++++++++++++



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
        <td><div>The description of the security group, which is a string of 2 to 256 characters. It cannot begin with http:// or https://.</div></td></tr>
            <tr>
    <td>dest_cidr_ip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The target IP address range (CIDR format is used to specify the IP address range). The default value is 0.0.0.0/0 (which means no restriction will be applied). Other supported formats include 10.159.6.18/12. Only IPv4 is supported.</div></br>
        <div style="font-size: small;">aliases: cidr_ip<div></td></tr>
            <tr>
    <td>dest_group_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The target security group ID within the same region. Either the dest_group_id or dest_cidr_ip must be set. If both are set, then dest_cidr_ip is authorized by default. If this field is specified, but no dest_cidr_ip is specified, the nic_type can only select intranet</div></br>
        <div style="font-size: small;">aliases: group_id<div></td></tr>
            <tr>
    <td>dest_group_owner_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The Alibaba Cloud user account Id of the target security group when security groups are authorized across accounts. This parameter is optional. If it is not set, then authorization is performed for security groups of the same account. This parameter is invalid if DestCidrIp has already been set.</div></br>
        <div style="font-size: small;">aliases: group_owner_id<div></td></tr>
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
    <td>ip_protocol<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>IP protocol, with a values tcp | udp | icmp | gre | all .all indicates support for all the four protocols</div></br>
        <div style="font-size: small;">aliases: proto<div></td></tr>
            <tr>
    <td>nic_type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>internet</td>
        <td><ul></ul></td>
        <td><div>Network type</div></br>
        <div style="font-size: small;">aliases: internet, intranet<div></td></tr>
            <tr>
    <td>policy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>accept</td>
        <td><ul><li>accept</li><li>drop</li></ul></td>
        <td><div>Authorization policy</div></td></tr>
            <tr>
    <td>port_range<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The range of port numbers relevant to the IP protocol When the protocol is 'tcp' or 'udp', the default port number range is 1-65535. For example, '1/200' means that the range of the port numbers is 1-200. If the input value is '200/1', the interface call reports an error. When the protocol is 'icmp', the port number range is -1/-1. When the protocol is 'gre', the port number range is -1/-1. When the protocol is all the port number range is -1/-1.</div></td></tr>
            <tr>
    <td>priority<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>1</td>
        <td><ul><li>1-100</li></ul></td>
        <td><div>Authorization policy priority</div></td></tr>
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
        <td><div>List of firewall inbound rules to enforce in this group. If none are supplied, a default all-out rule is assumed. If an empty list is supplied, no inbound rules will be enabled. Each rule contains four attributes as specified in Inbound Security Group Rules</div></td></tr>
            <tr>
    <td>rules_egress<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>List of firewall outbound rules to enforce in this group. If none are supplied, a default all-out rule is assumed. If an empty list is supplied, no outbound rules will be enabled.Each rule contains four attributes as specified in Outbound Security Group Rules</div></td></tr>
            <tr>
    <td>security_group_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The security group name. [2, 128] English or Chinese characters, must begin with an uppercase/lowercase letter or Chinese character. Can contain numbers, ".", "_" or "-". It cannot begin with http:// or https://.</div></br>
        <div style="font-size: small;">aliases: name<div></td></tr>
            <tr>
    <td>source_cidr_ip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The source IP address range (CIDR format is used to specify the IP address range). The default value is 0.0.0.0/0 (which means no restriction will be applied). Other supported formats include 10.159.6.18/12. Only IPv4 is supported.</div></br>
        <div style="font-size: small;">aliases: cidr_ip<div></td></tr>
            <tr>
    <td>source_group_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The security group ID. Either the source_group_id or cidr_ip parameter must be set. If both are set, then source_cidr_ip is authorized by default. If source_group_id is specified and source_cidr_ip is not specified, nic_type must be set to intranet</div></br>
        <div style="font-size: small;">aliases: group_id<div></td></tr>
            <tr>
    <td>source_group_owner_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>When the cross-user security group authorization, the source security group belongs to the user's Ali cloud account Id. The parameter is optional, if not set, the default is the same account between the security group authorization. source_cidr_ip This parameter has no effect if it has been set.</div></br>
        <div style="font-size: small;">aliases: group_owner_id<div></td></tr>
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
            acs_access_key_id: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            security_group_name: 'AliyunSG'
          register: result_details
        - debug: var=result_details.group_id
    
    
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
            acs_access_key_id: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            security_group_id: 'sg-wz98gmai3qwhpmlmw42'
            region: '{{ region }}'
            rules:
              - ip_protocol: tcp
                port_range: 1/122
                source_cidr_ip: '10.159.6.18/12'
            rules_egress:
              - proto: all
                port_range: -1/-1
                dest_group_id: 'sg-wz98gmai3qwhpmlmw42c'
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
            acs_access_key_id: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            security_group_name: 'AliyunSG'
            description: 'an example EC2 group'
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
                dest_group_id: 'sg-wz98gmai3qwhpmlmw42c'
                group_owner_id: 'contact@click2cloud.net'
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
         - sg-rj9akooukwik6xil4n53
        state: absent
      tasks:
        - name: delete security grp
          ecs_group:
            acs_access_key_id: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            security_group_ids: '{{ security_group_ids }}'
            state: '{{ state }}'
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
        state: getinfo
      tasks:
        - name: Querying Security group list
          ecs_group:
            acs_access_key_id: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            state: '{{ state }}'
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





