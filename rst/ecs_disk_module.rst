.. _ecs_disk:


ecs_disk - Create, Attach, Detach or Delete a disk
++++++++++++++++++++++++++++++++++++++++++++++++++



.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Create, Attach, Detach or Delete a disk


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
    <td>delete_with_instance<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>none</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Whether or not the disk is released along with the instance. True/Yes indicates that when the instance is released, this disk will be released with it.False/No indicates that when the instance is released, this disk will be retained.</div></br>
        <div style="font-size: small;">aliases: delete_on_termination<div></td></tr>
            <tr>
    <td>description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The value of disk description is blank by default. [2, 256] characters. The disk description will appear on the console. It cannot begin with http:// or https://.</div></br>
        <div style="font-size: small;">aliases: disk_description<div></td></tr>
            <tr>
    <td>device<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The value null indicates that the value is allocated by default, starting from /dev/xvdb to /dev/xvdz.</div></br>
        <div style="font-size: small;">aliases: device_name<div></td></tr>
            <tr>
    <td>disk_category<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>cloud</td>
        <td><ul><li>cloud</li><li>cloud_efficiency</li><li>cloud_ssd</li></ul></td>
        <td><div>Category of the data disk</div></br>
        <div style="font-size: small;">aliases: volume_type, disk_type<div></td></tr>
            <tr>
    <td>disk_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The disk ID. The disk and Instance must be in the same zone. Parameter is <b>required</b> while attaching disk.</div></br>
        <div style="font-size: small;">aliases: vol_id, id<div></td></tr>
            <tr>
    <td>disk_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The value of disk name is blank by default. [2, 128] English or Chinese characters, must begin with an uppercase/lowercase letter or Chinese character. Can contain numbers, '.', '_' and '-'. The disk name will appear on the console. It cannot begin with http:// or https://.</div></br>
        <div style="font-size: small;">aliases: name<div></td></tr>
            <tr>
    <td>disk_tags<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>A list of hash/dictionaries of instance tags, ['{"tag_key":"value", "tag_value":"value"}'], tag_key must be not null when tag_value isn't null</div></br>
        <div style="font-size: small;">aliases: tags<div></td></tr>
            <tr>
    <td>instance_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The specified instance ID. Parameter is <b>required</b> while attaching disk.</div></br>
        <div style="font-size: small;">aliases: instance<div></td></tr>
            <tr>
    <td>region<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The Aliyun Cloud region to use. If not specified then the value of the `ACS_REGION`, `ACS_DEFAULT_REGION` or `ECS_REGION` environment variable, if any, is used.</div></br>
        <div style="font-size: small;">aliases: acs_region, ecs_region<div></td></tr>
            <tr>
    <td>size<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Size of the system disk, in GB.The value should be equal to or greater than the size of the specific SnapshotId.</div></br>
        <div style="font-size: small;">aliases: volume_size, disk_size<div></td></tr>
            <tr>
    <td>snapshot_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Snapshots are used to create the data disk After this parameter is specified, Size is ignored. The actual size of the created disk is the size of the specified snapshot Snapshots from on or before July 15, 2013 cannot be used to create a disk</div></br>
        <div style="font-size: small;">aliases: snapshot<div></td></tr>
            <tr>
    <td>status<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>present</li><li>absent</li></ul></td>
        <td><div>The state of the instance after operating.</div></br>
        <div style="font-size: small;">aliases: state<div></td></tr>
            <tr>
    <td>zone_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Aliyun availability zone ID in which to launch the instance. Parameter is <b>required</b> while creating disk.</div></br>
        <div style="font-size: small;">aliases: zone, availability_zone, acs_zone, ecs_zone, zone<div></td></tr>
        </table>
    </br>



Examples
--------

 ::

    #
    # Provisioning new disk
    #
    
    # Basic provisioning example create a disk
    - name: create disk
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-beijing
        zone: cn-beijing-b
        size: 20
        status: present
      tasks:
        - name: create disk
          ecs_disk:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            zone: '{{ zone }}'
            size: '{{ size }}'
            status: '{{ status }}'
    
    # Advanced example with tagging and snapshot
    - name: create disk
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        zone: cn-hongkong-b
        disk_name: disk_1
        description: data disk_1
        size: 20
        snapshot_id: xxxxxxxxxx
        disk_category: cloud_ssd
        status: present
      tasks:
        - name: create disk
          ecs_disk:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            zone: '{{ zone }}'
            disk_name: '{{ disk_name }}'
            description: '{{ description }}'
            size: '{{ size }}'
            snapshot_id: '{{ snapshot_id }}'
            disk_category: '{{ disk_category }}'
            status: '{{ status }}'
    
    
    # Example to attach disk to an instance
    - name: attach disk to instance
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        status: present
        region: us-west-1
        instance_id: xxxxxxxxxx
        disk_id: xxxxxxxxxx
        device: /dev/xvdb
        delete_with_instance: false
      tasks:
        - name: Attach Disk to instance
          ecs_disk:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            status: '{{ status }}'
            region: '{{ region }}'
            instance_id: '{{ instance_id }}'
            disk_id: '{{ disk_id }}'
            device: '{{ device }}'
            delete_with_instance: '{{ delete_with_instance }}'
    
    
    # Example to detach disk from instance
    - name: detach disk
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: us-west-1
        disk_id: xxxxxxxxxx
        status: present
      tasks:
        - name: detach disk
          ecs_disk:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            id: '{{ disk_id }}'
            status: '{{ status }}'
    
    
    # Example to delete disk
    - name: detach disk
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: us-west-1
        disk_id: xxxxxxxxxx
        status: absent
      tasks:
        - name: detach disk
          ecs_disk:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            disk_id: '{{ disk_id }}'
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





