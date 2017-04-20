.. _rds_acc_mgmt:


rds_acc_mgmt - Create account, delete account, resetting instance password, resetting account, granting account permission and revoking account permission in RDS.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Create account, delete account, resetting instance password, resetting account, granting account permission and revoking account permission in RDS.




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
    <td>account_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Operation account requiring a uniqueness check. It may consist of lower case letters, numbers and underlines, and must start with a letter and have no more than 16 characters</div></br>
        <div style="font-size: small;">aliases: name<div></td></tr>
            <tr>
    <td>account_password<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Operation password. It may consist of letters, digits, or underlines, with a length of 6 to 32 characters.</div></br>
        <div style="font-size: small;">aliases: password<div></td></tr>
            <tr>
    <td>account_privilege<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul><li>ReadOnly</li><li>ReadWrite</li></ul></td>
        <td><div>Account permission</div></br>
        <div style="font-size: small;">aliases: privilege<div></td></tr>
            <tr>
    <td>account_type<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td>Normal</td>
        <td><ul><li>Normal</li><li>normal</li><li>Super</li><li>super</li></ul></td>
        <td><div>Privilege type of account. Normal - Common privilege, Super - High privilege, default value is Normal. This parameter is valid for MySQL 5.5/5.6 only</div></td></tr>
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
    <td>command<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td>create</td>
        <td><ul><li>create</li><li>delete</li><li>reset_password</li><li>reset</li><li>grant</li><li>revoke</li></ul></td>
        <td><div>The state of the instance after operating.</div></td></tr>
            <tr>
    <td>db_instance_id<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Id of instance.</div></td></tr>
            <tr>
    <td>db_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Name of the database associated with this account.</div></td></tr>
            <tr>
    <td>description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Account remarks, which cannot exceed 256 characters. It cannot begin with http:// , https:// .  It must start with a Chinese character or English letter. It can include Chinese and english characters/letters, underlines (_), hyphens (-), and numbers. The length may be 2-256 characters</div></td></tr>
        </table>
    </br>



Examples
--------

 ::

    #
    # provisioning for rds
    #
    
    # basic provisioning example to create account
    
    - name: create account
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        command: create
        db_instance_id: xxxxxxxxxx
        account_name: xxxxxxxxxx
        account_password: test@123
        description: normal account
        account_type: normal
      tasks:
        - name: create account
          rds_acc_mgmt:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            command: '{{ command }}'
            db_instance_id: '{{ db_instance_id }}'
            account_name: '{{ account_name }}'
            account_password: '{{ account_password }}'
            description: '{{ description }}'
            account_type: '{{ account_type }}'
          register: result
        - debug: var=result
    
    
    # basic provisioning example to resetting an instance password
    
    - name: Resetting an instance password
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        command: reset_password
        db_instance_id: xxxxxxxxxx
        account_name: xxxxxxxxxx
        account_password: testuser@123
      tasks:
        - name: Resetting an instance password
          rds_acc_mgmt:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            command: '{{ command }}'
            db_instance_id: '{{ db_instance_id }}'
            account_name: '{{ account_name }}'
            account_password: '{{ account_password }}'
          register: result
        - debug: var=result
    
    
    # basic provisioning example to resetting an account
    
    - name: Resetting an account
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        command: reset
        db_instance_id: xxxxxxxxxx
        account_name: xxxxxxxxxx
        account_password: testuser@123   
      tasks:
        - name: Resetting an account
          rds_acc_mgmt:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            command: '{{ command }}'
            db_instance_id: '{{ db_instance_id }}'
            account_name: '{{ account_name }}'
            account_password: '{{ account_password }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to delete an account
    
    - name: delete account
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        command: delete
        db_instance_id: xxxxxxxxxx
        account_name: xxxxxxxxxx
      tasks:
        - name: delete account
          rds_acc_mgmt:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            command: '{{ command }}'
            db_instance_id: '{{ db_instance_id }}'
            account_name: '{{ account_name }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to granting account permission
    
    - name: granting account permission
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        command: grant
        db_instance_id: xxxxxxxxxx
        db_name: xxxxxxxxxx
        account_name: xxxxxxxxxx
        account_privilege: ReadOnly
      tasks:
        - name: granting account permission
          rds_acc_mgmt:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            command: '{{ command }}'
            db_instance_id: '{{ db_instance_id }}'
            db_name: '{{ db_name }}'
            account_name: '{{ account_name }}'
            account_privilege: '{{ account_privilege }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to revoking account permission
    
    - name: revoking account permission
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        command: revoke
        db_instance_id: xxxxxxxxxx
        db_name: xxxxxxxxxx
        account_name:  xxxxxxxxxx
      tasks:
        - name: revoking account permission
          rds_acc_mgmt:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            command: '{{ command }}'
            db_instance_id: '{{ db_instance_id }}'
            db_name: '{{ db_name }}'
            account_name: '{{ account_name }}'
          register: result
        - debug: var=result





Status
~~~~~~

This module is flagged as **stableinterface** which means that the maintainers for this module guarantee that the no backward incompatible interface changes will be made.


Support
~~~~~~~

This module is maintained by those with core commit privileges





