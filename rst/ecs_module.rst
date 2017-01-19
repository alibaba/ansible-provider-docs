.. _ecs:


ecs - create, start, stop, restart or terminate an instance in ecs
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Creates or terminates ecs instances.


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
    <td>allocate_public_ip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Whether allocate a public ip for the new instance.</div></br>
        <div style="font-size: small;">aliases: assign_public_ip<div></td></tr>
            <tr>
    <td>auto_renew<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>no</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Whether automate renew the charge of the instance.</div></td></tr>
            <tr>
    <td>auto_renew_period<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>no</td>
        <td><ul><li>1</li><li>2</li><li>3</li><li>6</li><li>12</li></ul></td>
        <td><div>The duration of the automatic renew the charge of the instance. It is vaild when auto_renew is yes.</div></td></tr>
            <tr>
    <td>bind_eip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>ID of Elastic IP Address bind to the new instance.</div></td></tr>
            <tr>
    <td>count<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>1</td>
        <td><ul></ul></td>
        <td><div>The number of the new instance.</div></td></tr>
            <tr>
    <td>description<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Description of the instance to use.</div></td></tr>
            <tr>
    <td>disks<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>A list of hash/dictionaries of volumes to add to the new instance; '[{"key":"value", "key":"value"}]';</div><div>keys allowed are - device_category (required=false; default="cloud"; choices=["cloud", "cloud_efficiency", "cloud_ssd", "ephemeral_ssd"] ) - device_size (required=false; default=null; choices=depends on disk_category) - device_size (required=false; default=null; choices=depends on disk_category) - device_name (required=false; default=null) - device_description (required=false; default=null) - delete_on_termination (required=false, default="true") - snapshot (required=false; default=null), volume_type (str), iops (int) - device_type is deprecated use volume_type, iops must be set when volume_type='io1', ephemeral and snapshot are mutually exclusive.</div></br>
        <div style="font-size: small;">aliases: volumes<div></td></tr>
            <tr>
    <td>group_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Security group id to use with the instance</div></td></tr>
            <tr>
    <td>host_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Instance host name.</div></td></tr>
            <tr>
    <td>ids<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>A list of identifier for this instance or set of instances, so that the module will be idempotent with respect to ECS instances. This identifier should not be reused for another call later on. For details, see the description of client token at <a href='https://help.aliyun.com/document_detail/25693.html?spm=5176.doc25499.2.7.mrVgE2'>https://help.aliyun.com/document_detail/25693.html?spm=5176.doc25499.2.7.mrVgE2</a>.</div><div>The length of the ids is the same with count</div></td></tr>
            <tr>
    <td>image_id<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Image ID to use for the instance.</div></br>
        <div style="font-size: small;">aliases: image<div></td></tr>
            <tr>
    <td>instance_charge_type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>PostPaid</td>
        <td><ul><li>PrePaid</li><li>PostPaid</li></ul></td>
        <td><div>The charge type of the instance.</div></td></tr>
            <tr>
    <td>instance_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Name of the instance to use.</div></td></tr>
            <tr>
    <td>instance_tags<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>A list of hash/dictionaries of instance tags, '[{tag_key:"value", tag_value:"value"}]', tag_key must be not null when tag_value isn't null</div></br>
        <div style="font-size: small;">aliases: tags<div></td></tr>
            <tr>
    <td>instance_type<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Instance type to use for the instance.</div></br>
        <div style="font-size: small;">aliases: type<div></td></tr>
            <tr>
    <td>internet_data<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>A hash/dictionaries of internet to the new instance; '{"key":"value"}';</div><div>keys allowed are - charge_type (required=false; default="PayByBandwidth", choices=["PayByBandwidth", "PayByTraffic"]) - max_bandwidth_in(required=false, default=200) - max_bandwidth_out(required=false, default=0).</div></td></tr>
            <tr>
    <td>io_optimized<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>no</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Whether instance is using optimized volumes.</div></td></tr>
            <tr>
    <td>password<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The password to login instance.</div></td></tr>
            <tr>
    <td>period<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>1-12</li></ul></td>
        <td><div>The charge duration of the instance, the value is vaild when instance_charge_type is "PrePaid".</div></td></tr>
            <tr>
    <td>private_ip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Private IP address for the new instance.</div></td></tr>
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
        <td><ul><li>present</li><li>pending</li><li>running</li><li>stopped</li><li>restarted</li><li>absent</li><li>getstatus</li></ul></td>
        <td><div>The state of the instance after operating.</div></br>
        <div style="font-size: small;">aliases: state<div></td></tr>
            <tr>
    <td>system_disk<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>A hash/dictionaries of system disk to the new instance; '{"key":"value"}';</div><div>keys allowed are - disk_category (required=false; default="cloud"; choices=["cloud", "cloud_efficiency", "cloud_ssd", "ephemeral_ssd"] ) - disk_size (required=false; default=max[40, ImageSize]; choices=[40-500] ) - disk_name (required=false; default=null) - disk_description (required=false; default=null)</div></td></tr>
            <tr>
    <td>vswitch_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The subnet ID in which to launch the instance (VPC).</div></br>
        <div style="font-size: small;">aliases: vpc_subnet_id<div></td></tr>
            <tr>
    <td>wait<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>no</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Wait for the instance to be 'running' before returning.</div></td></tr>
            <tr>
    <td>wait_timeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>300</td>
        <td><ul></ul></td>
        <td><div>how long before wait gives up, in seconds</div></td></tr>
            <tr>
    <td>zone_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Aliyun availability zone ID in which to launch the instance</div></br>
        <div style="font-size: small;">aliases: acs_zone, ecs_zone, zone<div></td></tr>
        </table>
    </br>



Examples
--------

 ::

    #
    # provisioning new ecs instance
    #
    
    # basic provisioning example classic network
    - name: basic provisioning example
      hosts: localhost
      vars:
        acs_access_key: XXXXXXXXXXXXXX
        acs_secret_access_key: XXXXXXXXXXXXXX
        region: cn-beijing
        zone: cn-beijing
        image: ubuntu1404_64_40G_cloudinit_20160727.raw
        instance_type: ecs.n1.small
        assign_public_ip: yes
      tasks:
        - name: classic network
          ecs:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            zone: '{{ zone }}'
            image: '{{ image }}'
            instance_type: '{{ instance_type }}'
            count: 2
            assign_public_ip: '{{ assign_public_ip }}'
    
    # basic provisioning example vpc network
    - name: basic provisioning example
      hosts: localhost
      vars:
        acs_access_key: XXXXXXXXXXXXXX
        acs_secret_access_key: XXXXXXXXXXXXXX
        region: cn-beijing
        zone: cn-beijing
        image: ubuntu1404_64_40G_cloudinit_20160727.raw
        instance_type: ecs.n1.small
        vswitch_id: vsw-j6co2uknrmopj4ypgdnq4
        assign_public_ip: no
    
      tasks:
        - name: vpc network
          ecs:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            image: '{{ image }}'
            instance_type: '{{ instance_type }}'
            vswitch_id: '{{ vswitch_id }}'
            assign_public_ip: '{{ assign_public_ip }}'
    
    
    # advanced example with tagging and host name password
    - name: advanced provisioning example
      hosts: localhost
      vars:
        acs_access_key: XXXXXXXXXXXXXX
        acs_secret_access_key: XXXXXXXXXXXXXX
        region: cn-beijing
        zone: cn-beijing
        image: ubuntu1404_64_40G_cloudinit_20160727.raw
        instance_type: ecs.n1.small
        group_id: sg-25y6ag32b
        host_name: myhost
        password: mypassword
      tasks:
        - name: tagging and host name password
          ecs:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            image: '{{ image }}'
            instance_type: '{{ instance_type }}'
            assign_public_ip: yes
            group_id: '{{ group_id }}'
            instance_tags:
                - tag_key : postgress
                  tag_value: 1
            host_name: '{{ host_name }}'
            password: '{{ password }}'
            wait: yes
            wait_timeout: 500
    
    # single instance with internet data configuration and instance details
    - name: advanced provisioning example
      hosts: localhost
      vars:
        acs_access_key: XXXXXXXXXXXXXX
        acs_secret_access_key: XXXXXXXXXXXXXX
        region: cn-beijing
        zone: cn-beijing
        image: ubuntu1404_64_40G_cloudinit_20160727.raw
        instance_type: ecs.n1.small
        group_id: sg-25y6ag32b
        instance_name: myinstance
        description: my description
      tasks:
        - name: internet data configuration and instance details
          ecs:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            image: '{{ image }}'
            instance_type: '{{ instance_type }}'
            group_id: '{{ group_id }}'
            instance_name: '{{ instance_name }}'
            description: '{{ description }}'
            internet_data:
                charge_type: PayByBandwidth
                max_bandwidth_in: 200
                max_bandwidth_out: 50
    
    
    # single instance with additional volume from snapshot and volume delete on termination
    - name: advanced provisioning example
      hosts: localhost
      vars:
        acs_access_key: XXXXXXXXXXXXXX
        acs_secret_access_key: XXXXXXXXXXXXXX
        region: cn-beijing
        zone: cn-beijing
        image: ubuntu1404_64_40G_cloudinit_20160727.raw
        instance_type: ecs.n1.small
      tasks:
        - name: additional volume
          ecs:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            image: '{{ image }}'
            instance_type: '{{ instance_type }}'
            assign_public_ip: yes
            volumes:
              - disk_name: /dev/sdb
                snapshot_id: snap-abcdef12
                disk_category: cloud_efficiency
                disk_size: 100
                delete_on_termination: true
    
    # example with system disk configuration and IO optimized
    - name: advanced provisioning example
      hosts: localhost
      vars:
        acs_access_key: XXXXXXXXXXXXXX
        acs_secret_access_key: XXXXXXXXXXXXXX
        region: cn-beijing
        zone: cn-beijing
        image: ubuntu1404_64_40G_cloudinit_20160727.raw
        instance_type: ecs.n1.small
      tasks:
        - name: additional volume
          ecs:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            image: '{{ image }}'
            instance_type: '{{ instance_type }}'
            io_optimized: yes
            system_disk:
                disk_category: cloud
                disk_size: 50
                disk_name: DiskName
                disk_description: Invalid System Disk Size
    
    # example with prepaid internet charge type configuration
    - name: advanced provisioning example
      hosts: localhost
      vars:
        acs_access_key: XXXXXXXXXXXXXX
        acs_secret_access_key: XXXXXXXXXXXXXX
        region: cn-beijing
        image: ubuntu1404_64_40G_cloudinit_20160727.raw
        instance_type: ecs.n1.small
      tasks:
        - name: prepaid internet charge type configuration
          ecs:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            image: '{{ image }}'
            instance_type: '{{ instance_type }}'
            assign_public_ip: yes
            instance_charge_type: PrePaid
            period: 1
            auto_renew: yes
            auto_renew_period: 3
    
    #
    # modifying attributes of ecs instance
    #
    - name: modify attribute example
      hosts: localhost
      vars:
        acs_access_key: XXXXXXXXXXXXXX
        acs_secret_access_key: XXXXXXXXXXXXXX
        region: cn-beijing
      tasks:
        - name: modify attribute of multiple instances
          ecs:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            attributes:
                - id:  i-rj9be6tlwmae1995uq5t
                  name: InstanceName1
                  description: volume attribute1
                  password: mypassword1
                  host_name: hostName1
                - id:  i-rj9be6tlwmdfsfsd3543
                  name: InstanceName2
                  description: volume attribute2
                  password: mypassword2
                  host_name: hostcomes2
    
    #
    # querying instance status
    #
    - name: query instance status
      hosts: localhost
      vars:
        acs_access_key: XXXXXXXXXXXXXX
        acs_secret_access_key: XXXXXXXXXXXXXX
        region: cn-beijing
        zone: cn-beijing
        status: getstatus
        pagenumber: 1
        pagesize: 10
      tasks:
        - name: query instance status from the particular region
          ecs:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            zone: '{{ zone }}'
            status: '{{ status }}'
            pagenumber: '{{ pagenumber }}'
            pagesize: '{{ pagesize }}'
    
    #
    # start or terminate instance
    #
    - name: start or terminate instance
      hosts: localhost
      vars:
        acs_access_key: XXXXXXXXXXXXXX
        acs_secret_access_key: XXXXXXXXXXXXXX
        region: cn-shenzhen
        instance_ids: i-94dehop6n
        instance_tags:
        - tag_key: xz_test
          tag_value: '1.20'
        state: running
      tasks:
        - name: start instance
          ecs_model:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            instance_ids: '{{ instance_ids }}'
            instance_tags: '{{ instance_tags }}'
            state: '{{ state }}'
    
    #
    # stop or restarted instance
    #
    - name: start stop restart instance
      hosts: localhost
      vars:
        acs_access_key: XXXXXXXXXXXXXX
        acs_secret_access_key: XXXXXXXXXXXXXX
        region: cn-shenzhen
        instance_ids: i-94dehop6n
        instance_tags:
        - tag_key: xz_test
          tag_value: '1.20'
        force: False
        state: restarted
      tasks:
        - name: Restart instance
          ecs_model:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            instance_ids: '{{ instance_ids }}'
            instance_tags: '{{ instance_tags }}'
            state: '{{ state }}'
    
    #
    # add an instance to security group
    #
    - name: Add an instance to security group
      hosts: localhost
      vars:
        acs_access_key: XXXXXXXXXXXXXX
        acs_secret_access_key: XXXXXXXXXXXXXX
        region: cn-shenzhen
        instance_id: i-94dehop6n
        group_id: sg-25y6ag32b
        sg_action: join
      tasks:
        - name: Add an instance to security group
          ecs_model:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            instance_id: '{{ instance_id }}'
            group_id: '{{ group_id }}'
            sg_action: '{{ sg_action }}'
    
    #
    # remove instance from security group
    #
    - name: Remove an instance from security group
      hosts: localhost
      vars:
        acs_access_key: XXXXXXXXXXXXXX
        acs_secret_access_key: XXXXXXXXXXXXXX
        region: cn-shenzhen
        instance_id: i-94dehop6n
        group_id: sg-25y6ag32b
        sg_action: leave
      tasks:
        - name: Remove an instance from security group
          ecs_model:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            instance_id: '{{ instance_id }}'
            group_id: '{{ group_id }}'
            sg_action: '{{ sg_action }}'
    


Notes
-----

.. note:: If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence ``ACS_ACCESS_KEY_ID`` or ``ACS_ACCESS_KEY`` or ``ECS_ACCESS_KEY``, ``ACS_SECRET_ACCESS_KEY`` or ``ACS_SECRET_KEY`` or ``ECS_SECRET_KEY``, ``ACS_REGION`` or ``ACS_DEFAULT_REGION`` or ``ECS_REGION``



Status
~~~~~~

This module is flagged as **stableinterface** which means that the maintainers for this module guarantee that the no backward incompatible interface changes will be made.


Support
~~~~~~~

This module is maintained by those with core commit privileges





