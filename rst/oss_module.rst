.. _oss:


oss - Create/Delete Bucket and Objects/Folder. Upload Files in OSS
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



.. contents::
   :local:
   :depth: 2


Synopsis
--------

* This module allows the user to manage OSS buckets and the objects within them. Includes support for creating and deleting both objects and buckets, retrieving object keys. This module has a dependency on footmark and ossutils.




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
    <td>bucket<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Bucket name.</div></br>
        <div style="font-size: small;">aliases: bucket_name, name<div></td></tr>
            <tr>
    <td>encrypt<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>When set for PUT mode, asks for server-side encryption</div></td></tr>
            <tr>
    <td>expiration<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>600</td>
        <td><ul></ul></td>
        <td><div>Time limit (in seconds) for the URL generated and returned by OSS/Walrus when performing a mode=put or mode=geturl operation.</div></td></tr>
            <tr>
    <td>file_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Name to file after uploaded to bucket</div></td></tr>
            <tr>
    <td>folder_name<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>name of the folder to create</div></td></tr>
            <tr>
    <td>headers<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Custom headers for PUT operation, as a dictionary of 'key=value' and 'key=value,key=value'.</div></td></tr>
            <tr>
    <td>marker<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Specifies the key to start with when using list mode. Object keys are returned in alphabetical order, starting with key after the marker in order</div></td></tr>
            <tr>
    <td>max_keys<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>1000</td>
        <td><ul></ul></td>
        <td><div>Max number of results to return in list mode, set this if you want to retrieve fewer than the default 1000 keys.</div></td></tr>
            <tr>
    <td>metadata<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Metadata for PUT operation, as a dictionary of 'key=value' and 'key=value,key=value'.</div></td></tr>
            <tr>
    <td>mode<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul><li>create</li><li>delete</li><li>put</li><li>put_folder</li><li>list</li><li>delobj</li></ul></td>
        <td><div>Switches the module behaviour between create (bucket), delete (bucket), put (upload), put_folder (create folder), list (list keys) and delobj (delete object).</div></td></tr>
            <tr>
    <td>object_list<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>Specify list of objects to delete from a bucket</div></td></tr>
            <tr>
    <td>overwrite<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>always</td>
        <td><ul></ul></td>
        <td><div>Force overwrite either locally on the filesystem or remotely with the object/key. Used with PUT and GET operations. Boolean or one of [always, never, different], true is equal to 'always' and false is equal to 'never'.</div></td></tr>
            <tr>
    <td>permission<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>private</td>
        <td><ul><li>private</li><li>public-read</li><li>public-read-write</li></ul></td>
        <td><div>This option lets the user set the canned permissions on the bucket that are created. The permissions that can be set are 'private', 'public-read', 'public-read-write'. Multiple permissions can be specified as a list.</div></td></tr>
            <tr>
    <td>region<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>cn-hangzhou</td>
        <td><ul></ul></td>
        <td><div>The Aliyun Cloud region to use. If not specified then the value of the `ACS_REGION`, `ACS_DEFAULT_REGION` or `ECS_REGION` environment variable, if any, is used.</div></br>
        <div style="font-size: small;">aliases: acs_region, ecs_region<div></td></tr>
            <tr>
    <td>src<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul></ul></td>
        <td><div>The source file path when performing a PUT operation.</div></td></tr>
        </table>
    </br>



Examples
--------

 ::

    #
    # provisioning new oss bucket
    #
    
    # basic provisioning example to create bucket
    - name: create oss bucket
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hangzhou
        mode: create
        bucket: bucketname
        permission: public-read-write    
      tasks:
        - name: create oss bucket
          oss:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            mode: '{{ mode }}'
            bucket: '{{ bucket }}'
            permission: '{{ permission }}'        
          register: result
        - debug: var=result
    
    # basic provisioning example to delete bucket
    - name: delete oss bucket
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hangzhou
        mode: delete
        bucket: bucketname    
      tasks:
        - name: delete oss bucket
          oss:
            acs_access_key_id: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            mode: '{{ mode }}'
            bucket: '{{ bucket }}'        
          register: result
        - debug: var=result
    
    # basic provisioning example to upload a file
    - name: simple upload to bucket
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hangzhou
        mode: put
        bucket: bucketname
        src: 'local_file.txt'
        file_name: 'remote_file.txt'
        headers:
          Content-Type: 'text/html'
          Content-Encoding: md5
        metadata:
          x-oss-meta-key: value
        expiration: 30    
      tasks:
        - name: simple upload to bucket
          oss:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            mode: '{{ mode }}'
            bucket: '{{ bucket }}'
            src: '{{ src }}'
            file_name: '{{ file_name }}'
            headers: '{{ headers }}'
            metadata: '{{ metadata }}'
            expiration: '{{ expiration }}'       
          register: result
        - debug: var=result
    
    # basic provisioning example to create a folder in bucket
    - name: create folder in a bucket
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hangzhou
        mode: put_folder
        bucket: bucketname
        folder_name: MeetingDocs
      tasks:
        - name: create bucket folder
          oss:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            mode: '{{ mode }}'
            bucket: '{{ bucket }}'
            folder_name: '{{ folder_name }}'
          register: folder_result
        - debug: var=folder_result
    
    # basic provisioning example to list bucket objects
    - name: list bucket objects
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hangzhou
        mode: list
        bucket: bucketname
        marker: xxxx
        max_keys: 150    
      tasks:
        - name: list bucket objects
          oss:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            mode: '{{ mode }}'
            bucket: '{{ bucket }}'
            marker: '{{ marker }}'
            max_keys: '{{ max_keys }}'
          register: list_result
        - debug: var=list_result
    
    # basic provisioning example to delete bucket objects
    - name: delete bucket objects
      hosts: localhost
      connection: local
      vars:
        acs_access_key: xxxxxxxxxx
        acs_secret_access_key: xxxxxxxxxx
        region: cn-hangzhou
        mode: delobj
        bucket: bucketname
        object_list:
          - objectname
          - objectname    
      tasks:
        - name: delete bucket objects
          oss:
            acs_access_key: '{{ acs_access_key }}'
            acs_secret_access_key: '{{ acs_secret_access_key }}'
            region: '{{ region }}'
            mode: '{{ mode }}'
            bucket: '{{ bucket }}'
            object_list: '{{ object_list }}'
          register: delete_objects_result
        - debug: var=delete_objects_result
    





Status
~~~~~~

This module is flagged as **stableinterface** which means that the maintainers for this module guarantee that the no backward incompatible interface changes will be made.


Support
~~~~~~~

This module is maintained by those with core commit privileges





