.. _ecs_ami:


ecs_ami - Create or Delete User-defined Image
+++++++++++++++++++++++++++++++++++++++++++++



.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Creates or deletes User-defined Images


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
        <td><div>The description of the image, with a length limit of 0 to 256 characters.</div></td></tr>
            <tr>
    <td>disk_mapping<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>An optional list of device hashes/dictionaries with custom configurations (see example).</div></td></tr>
            <tr>
    <td>image_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>ID of an image. Parameter is <b>required</b> while deleting user defined image.</div></td></tr>
            <tr>
    <td>image_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The name of the image, [2, 128] English or Chinese characters.</div></br>
        <div style="font-size: small;">aliases: name<div></td></tr>
            <tr>
    <td>image_version<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The version number of the image, with a length limit of 1 to 40 English characters.</div></br>
        <div style="font-size: small;">aliases: version<div></td></tr>
            <tr>
    <td>images_tags<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>A list of hash/dictionaries of image tags, '[{tag_key:"value", tag_value:"value"}]', tag_key must be not null when tag_value isn't null</div></br>
        <div style="font-size: small;">aliases: tags<div></td></tr>
            <tr>
    <td>instance_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>instance id of the image to create.</div></br>
        <div style="font-size: small;">aliases: instance<div></td></tr>
            <tr>
    <td>launch_permission<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Users that should be able to launch the ami</div></td></tr>
            <tr>
    <td>region<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The Aliyun Cloud region to use. If not specified then the value of the `ACS_REGION`, `ACS_DEFAULT_REGION` or `ECS_REGION` environment variable, if any, is used.</div></br>
        <div style="font-size: small;">aliases: acs_region, ecs_region<div></td></tr>
            <tr>
    <td>snapshot_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The snapshot ID. A user-defined image is created from the specified snapshot.</div></br>
        <div style="font-size: small;">aliases: snapshot<div></td></tr>
            <tr>
    <td>status<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>present</li><li>absent</li></ul></td>
        <td><div>The state of the image for operating.</div></br>
        <div style="font-size: small;">aliases: state<div></td></tr>
            <tr>
    <td>wait<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>no</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Wait for the image creation.</div></td></tr>
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
    # provisioning to create new user-defined image
    #
    
    # basic provisioning example to create image using ecs instance
    - name: create image from ecs instance
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        instance_id: xxxxxxxxxx
      tasks:
        - name: create image form ecs instance
          ecs_ami:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            instance_id: '{{ instance_id }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to create image using snapshot
    - name: create image using snapshot
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        snapshot_id: xxxxxxxxxx
        status: present
      tasks:
        - name: create image using snapshot
          ecs_ami:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            snapshot_id: '{{ snapshot_id }}'
            status: '{{ status }}'
          register: result
        - debug: var=result
    
    # basic provisioning example to create image using disk mapping
    - name: create image using disk mapping
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        disk_mapping:
          - device: /dev/xvda
            disk_size: 5
            snapshot_id: xxxxxxxxxx
        status: present
      tasks:
        - name: create image using disk mapping
          ecs_ami:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            disk_mapping: '{{ disk_mapping }}'
            status: '{{ status }}'
          register: result
        - debug: var=result
    
    # advanced example to create image with tagging, version and launch permission
    - name: create image
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hongkong
        image_name: image_test
        image_version: 4
        description: description
        images_tags:
          - tag_key: key
            tag_value: value
        disk_mapping:
          - device: /dev/xvda
            disk_size: 5
            snapshot_id: xxxxxxxxxx
        status: present
        wait: false
        wait_timeout: 10
        launch_permission: xxxxxxxxxx
      tasks:
        - name: create image
          ecs_ami:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            image_name: '{{ image_name }}'
            image_version: '{{ image_version }}'
            description: '{{ description }}'
            images_tags: '{{ images_tags }}'
            disk_mapping: '{{ disk_mapping }}'
            status: '{{ status }}'
            wait: '{{ wait }}'
            wait_timeout: '{{ wait_timeout }}'
            launch_permission: '{{ launch_permission }}'
          register: result
        - debug: var=result
    
    #
    # provisioning to delete user-defined image
    #
    
    # provisioning to delete user-defined image
    - name: delete image
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: us-west-1
        image_id: xxxxxxxxxx
        status: absent
      tasks:
        - name: delete image
          ecs_ami:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            image_id: '{{ image_id }}'
            status: '{{ status }}'
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





