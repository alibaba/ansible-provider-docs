.. _rds:


rds - Create instance, Create database, Create read-only instance, Modify rds instance, Changing rds instance type, Restart instance, Switching between primary and standby database, Delete database and Release Instance in RDS.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Create instance, Create database, Create read-only instance, Modify rds instance, Changing rds instance type, Restart instance, Switching between primary and standby database, Delete database and Release Instance in RDS.




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
    <td>allocate_public_ip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Whether to allocate public IP.</div></td></tr>
            <tr>
    <td>backup_retention_period<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Number of days backups are retained.</div></br>
        <div style="font-size: small;">aliases: backup_retention<div></td></tr>
            <tr>
    <td>character_set_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Associate the DB instance with a specified character set.</div></td></tr>
            <tr>
    <td>command<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td>create</td>
        <td><ul><li>create</li><li>delete</li><li>replicate</li><li>modify</li><li>reboot</li><li>switch</li></ul></td>
        <td><div>Specifies the action to take.</div></td></tr>
            <tr>
    <td>connection_mode<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>Performance</li><li>Safe</li></ul></td>
        <td><div>The connection mode of the rds instance.</div></td></tr>
            <tr>
    <td>connection_string_ prefix<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Target connection string.</div></td></tr>
            <tr>
    <td>current_connection_string<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Current connection string of an instance.</div></td></tr>
            <tr>
    <td>db_description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Description of a database to create within the instance.  If not specified then no database is created.</div></td></tr>
            <tr>
    <td>db_engine<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul><li>MySQL</li><li>SQLServer</li><li>PostgreSQL</li><li>PPAS</li></ul></td>
        <td><div>The type of database.</div></td></tr>
            <tr>
    <td>db_instance_class<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The instance type of the database.</div></br>
        <div style="font-size: small;">aliases: instance_type<div></td></tr>
            <tr>
    <td>db_instance_storage<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Size in gigabytes of the initial storage for the DB instance.</div></br>
        <div style="font-size: small;">aliases: size<div></td></tr>
            <tr>
    <td>db_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Name of a database to create within the instance.  If not specified then no database is created.</div></td></tr>
            <tr>
    <td>db_tags<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>A hash of db tags, tag_key must be not null when tag_value isn't null.</div></td></tr>
            <tr>
    <td>engine_version<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Version number of the database engine to use. If not specified, then the current Aliyun RDS default engine version is used.</div></td></tr>
            <tr>
    <td>force<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Yes- forced, No- unforced, default value- unforced</div></td></tr>
            <tr>
    <td>instance_description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The description of the DB instance</div></td></tr>
            <tr>
    <td>instance_id<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>ID of the database to change.</div></br>
        <div style="font-size: small;">aliases: source_instance<div></td></tr>
            <tr>
    <td>instance_net_type<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul><li>Internet</li><li>Intranet</li></ul></td>
        <td><div>The net type of the DB instance</div></td></tr>
            <tr>
    <td>instance_network_type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>Classic</td>
        <td><ul><li>VPC</li><li>Classic</li></ul></td>
        <td><div>The network type of the instance.</div></br>
        <div style="font-size: small;">aliases: network_type<div></td></tr>
            <tr>
    <td>maint_window<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Maintenance window in format of ddd:hh24:mi-ddd:hh24:mi.  (Example: Mon:22:00-Mon:23:15) If not specified then a random maintenance window is assigned.</div></td></tr>
            <tr>
    <td>node_id<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Unique ID of a node.</div></td></tr>
            <tr>
    <td>pay_type<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul><li>Postpaid</li><li>Prepaid</li></ul></td>
        <td><div>The pay type of the DB instance.</div></td></tr>
            <tr>
    <td>period<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>Year</li><li>Month</li></ul></td>
        <td><div>The type of the Prepaid</div></td></tr>
            <tr>
    <td>port<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Target port.</div></td></tr>
            <tr>
    <td>preferred_backup_period<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Backup period.</div></br>
        <div style="font-size: small;">aliases: backup_window<div></td></tr>
            <tr>
    <td>preferred_backup_time<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Backup time, in the format ofHH:mmZ- HH:mm Z.This parameter is required if preferred_backup_period and backup_retention_period is passed.</div></td></tr>
            <tr>
    <td>private_ip_address<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>IP address of an VPC under VSwitchId. If no value is specified, the system will automatically assign a VPC IP address.</div></td></tr>
            <tr>
    <td>public_connection_string_prefix<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The public connection string.</div></td></tr>
            <tr>
    <td>public_port<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The public connection port.</div></td></tr>
            <tr>
    <td>region<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The ACS region to use. If not specified then the value of the ECS_REGION environment variable, if any, is used</div></br>
        <div style="font-size: small;">aliases: acs_region, ecs_region<div></td></tr>
            <tr>
    <td>security_ip_list<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>IP list that be allowed to access all DBs in the instance. Support CIDR mode.</div></td></tr>
            <tr>
    <td>used_time<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The duration of the Prepaid</div></td></tr>
            <tr>
    <td>vpc_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The ID of the VPC.</div></td></tr>
            <tr>
    <td>vswitch_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The ID of the VSwitch.</div></td></tr>
            <tr>
    <td>wait<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>no</td>
        <td><ul><li>yes</li><li>Yes</li><li>no</li><li>No</li><li>True</li><li>False</li><li>true</li><li>false</li></ul></td>
        <td><div>wait for the RDS instance to be in state 'running' before returning.</div></td></tr>
            <tr>
    <td>wait_timeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>300</td>
        <td><ul></ul></td>
        <td><div>how long before wait gives up, in seconds</div></td></tr>
            <tr>
    <td>zone<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>availability zone in which to launch the instance. Used only when command=create, command=replicate.</div></br>
        <div style="font-size: small;">aliases: acs_zone, ecs_zone<div></td></tr>
        </table>
    </br>



Examples
--------

 ::

    #
    # provisioning for rds
    #
    
    # basic provisioning example to create rds instance
    
    - name: create rds instance
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-beijing
        command: create
        zone: cn-beijing-a
        db_engine: MySQL
        engine_version: 5.6
        db_instance_class: rds.mysql.t1.small
        db_instance_storage: 10
        instance_net_type: Intranet
        instance_description: ahttp://
        security_ip_list: 192.168.0.2/24
        pay_type: Postpaid
        connection_mode: Safe
        instance_network_type: VPC
        vpc_id: xxxxxxxxxx
        vswitch_id: xxxxxxxxxx
        private_ip_address: 192.168.0.25
        allocate_public_ip: yes
        public_connection_string_prefix: test
        public_port: 3306
        db_name: testmysql
        db_description: test mysql
        character_set_name: utf8
        modifying_db_instance_maint_time: 02:00Z-06:00Z
        preferred_backup_time: 02:00Z-03:00Z
        preferred_backup_period: Monday,Tuesday
        backup_retention_period: 7
        wait: yes
        wait_timeout: 20
        db_tags:
          name: test
      tasks:
        - name: create rds instance
          rds:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            zone: '{{ zone }}'
            command: '{{ command }}'
            db_engine: '{{ db_engine }}'
            engine_version: '{{ engine_version }}'
            db_instance_class: '{{ db_instance_class }}'
            db_instance_storage: '{{ db_instance_storage }}'
            instance_net_type: '{{ instance_net_type }}'
            instance_description: '{{ instance_description }}'
            security_ip_list: '{{ security_ip_list }}'
            pay_type: '{{ pay_type }}'
            connection_mode: '{{ connection_mode }}'
            instance_network_type: '{{ instance_network_type }}'
            vpc_id: '{{ vpc_id }}'
            vswitch_id: '{{ vswitch_id }}'
            private_ip_address: '{{ private_ip_address }}'
            allocate_public_ip: '{{ allocate_public_ip }}'
            public_connection_string_prefix: '{{ public_connection_string_prefix }}'
            public_port: '{{ public_port }}'
            db_name: '{{ db_name }}'
            db_description: '{{ db_description }}'
            character_set_name: '{{ character_set_name }}'
            modifying_db_instance_maint_time: '{{ modifying_db_instance_maint_time }}'
            preferred_backup_time: '{{ preferred_backup_time }}'
            preferred_backup_period: '{{ preferred_backup_period }}'
            backup_retention_period: '{{ backup_retention_period }}'
            db_tags: '{{ db_tags }}'
            wait: '{{ wait }}'
            wait_timeout: '{{ wait_timeout }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to changing rds instance type
    
    - name: changing rds instance type
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-beijing
        command: modify
        instance_id: xxxxxxxxxx
        db_instance_class: rds.mysql.s1.small
        db_instance_storage: 35
        pay_type: Postpaid
      tasks:
        - name: changing rds instance type
          rds:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            command: '{{ command }}'
            instance_id: '{{ instance_id }}'
            db_instance_class: '{{ db_instance_class }}'
            db_instance_storage: '{{ db_instance_storage }}'
            pay_type: '{{ pay_type }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to modify rds instance
    
    - name: modify rds instance
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-beijing
        command: modify
        instance_id: xxxxxxxxxx
        db_instance_class: rds.mysql.t1.small
        db_instance_storage: 45
        instance_description: xyz
        security_ip_list: 192.168.0.2/24
        pay_type: Postpaid
        connection_mode: Safe
        instance_network_type: VPC
        vpc_id: xxxxxxxxxx
        vswitch_id: xxxxxxxxxx
        current_connection_string: test.mysql.rds.aliyuncs.com
        connection_string_prefix: test123
        port: 3390
        maint_window: 02:00Z-06:00Z
        preferred_backup_time:  02:00Z-03:00Z
        preferred_backup_period: Monday
        backup_retention_period: 50
      tasks:
        - name: modify rds instance
          rds:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            command: '{{ command }}'
            instance_id: '{{ instance_id }}'
            db_instance_class: '{{ db_instance_class }}'
            db_instance_storage: '{{ db_instance_storage }}'
            instance_description: '{{ instance_description }}'
            security_ip_list: '{{ security_ip_list }}'
            pay_type: '{{ pay_type }}'
            connection_mode: '{{ connection_mode }}'
            instance_network_type: '{{ instance_network_type }}'
            vpc_id: '{{ vpc_id }}'
            vswitch_id: '{{ vswitch_id }}'
            current_connection_string: '{{ current_connection_string }}'
            connection_string_prefix: '{{ connection_string_prefix }}'
            port: '{{ port }}'
            maint_window: '{{ maint_window }}'
            preferred_backup_time: '{{ preferred_backup_time }}'
            preferred_backup_period: '{{ preferred_backup_period }}'
            backup_retention_period: '{{ backup_retention_period }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to create database
    
    - name: create database
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        command: create
        instance_id: xxxxxxxxxx
        db_name: testdb
        db_description: test
        character_set_name: utf8
      tasks:
        - name: create database
          rds:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            command: '{{ command }}'
            instance_id: '{{ instance_id }}'
            db_name: '{{ db_name }}'
            db_description: '{{ db_description }}'
            character_set_name: '{{ character_set_name }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to delete database
    
    - name: delete database
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        command: delete
        instance_id: xxxxxxxxxx
        db_name: testdb
      tasks:
        - name: delete database
          rds:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            command: '{{ command }}'
            instance_id: '{{ instance_id }}'
            db_name: '{{ db_name }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to switching between primary and standby database of an rds
    
    - name: switching between primary and standby database
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        command: switch
        instance_id: xxxxxxxxxx
        node_id: xxxxxxxxxx
        force: 'Yes'
      tasks:
        - name: switching between primary and standby database
          rds:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            command: '{{ command }}'
            instance_id: '{{ instance_id }}'
            node_id: '{{ node_id }}'
            force: '{{ force }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to restarting rds instance
    
    - name: Restarting RDS Instance
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-beijing
        command: reboot
        instance_id: xxxxxxxxxx
      tasks:
        - name: Restarting RDS Instance
          rds:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            command: '{{ command }}'
            instance_id: '{{ instance_id }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to releasing rds instance
    
    - name: Releasing RDS Instance
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-beijing
        command: delete
        instance_id: xxxxxxxxxx
      tasks:
        - name: Releasing RDS Instance
          rds:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            command: '{{ command }}'
            instance_id: '{{ instance_id }}'
          register: result
        - debug: var=result
    





Status
~~~~~~

This module is flagged as **stableinterface** which means that the maintainers for this module guarantee that the no backward incompatible interface changes will be made.


Support
~~~~~~~

This module is maintained by those with core commit privileges





