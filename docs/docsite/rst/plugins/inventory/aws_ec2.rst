:source: aws_ec2.py


.. _aws_ec2_inventory:


aws_ec2 - ec2 inventory source
++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Get inventory hosts from Amazon Web Services EC2.
- Uses a <name>.aws_ec2.yaml (or <name>.aws_ec2.yml) YAML configuration file.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                            <th>Configuration</th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <b>aws_access_key_id</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                            <div>env:AWS_ACCESS_KEY_ID</div>
                                                            <div>env:AWS_ACCESS_KEY</div>
                                                            <div>env:EC2_ACCESS_KEY</div>
                                                                                                </td>
                                                <td>
                                                                        <div>The AWS access key to use. If you have specified a profile, you don't need to provide an access key/secret key/session token.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>aws_secret_access_key</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                            <div>env:AWS_SECRET_ACCESS_KEY</div>
                                                            <div>env:AWS_SECRET_KEY</div>
                                                            <div>env:EC2_SECRET_KEY</div>
                                                                                                </td>
                                                <td>
                                                                        <div>The AWS secret key that corresponds to the access key. If you have specified a profile, you don't need to provide an access key/secret key/session token.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>aws_security_token</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                            <div>env:AWS_SECURITY_TOKEN</div>
                                                            <div>env:AWS_SESSION_TOKEN</div>
                                                            <div>env:EC2_SECURITY_TOKEN</div>
                                                                                                </td>
                                                <td>
                                                                        <div>The AWS security token if using temporary access and secret keys.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>boto_profile</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                            <div>env:AWS_PROFILE</div>
                                                            <div>env:AWS_DEFAULT_PROFILE</div>
                                                                                                </td>
                                                <td>
                                                                        <div>The boto profile to use.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>cache</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[inventory ]<br>cache = no</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_INVENTORY_CACHE</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Toggle to enable/disable the caching of the inventory's source data, requires a cache plugin setup to work.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>cache_connection</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[inventory ]<br>cache_connection = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_INVENTORY_CACHE_CONNECTION</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Cache connection data or path, read cache plugin documentation for specifics.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>cache_plugin</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[inventory ]<br>cache_plugin = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_INVENTORY_CACHE_PLUGIN</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Cache plugin to use for the inventory's source data.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>cache_timeout</b>
                    <br/><div style="font-size: small; color: red">integer</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">3600</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[inventory ]<br>cache_timeout = 3600</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_INVENTORY_CACHE_TIMEOUT</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Cache duration in seconds</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>compose</b>
                    <br/><div style="font-size: small; color: red">dictionary</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{}</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>create vars from jinja2 expressions</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>filters</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>A dictionary of filter value pairs. Available filters are listed here <a href='http://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html#options'>http://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html#options</a></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>groups</b>
                    <br/><div style="font-size: small; color: red">dictionary</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{}</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>add hosts to group based on Jinja2 conditionals</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>hostnames</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>A list in order of precedence for hostname variables. You can use the options specified in <a href='http://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html#options'>http://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html#options</a>. To use tags as hostnames use the syntax tag:Name=Value to use the hostname Name_Value, or tag:Name to use the value of the Name tag.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>keyed_groups</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[]</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>add hosts to group based on the values of a variable</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>regions</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>A list of regions in which to describe EC2 instances. By default this is all regions except us-gov-west-1 and cn-north-1.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>strict</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>If true make invalid entries a fatal error, otherwise skip and continue</div>
                                                    <div>Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>strict_permissions</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>By default if a 403 (Forbidden) is encountered this plugin will fail. You can set strict_permissions to False in the inventory config file which will allow 403 errors to be gracefully skipped.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    

    # Minimal example using environment vars or instance role credentials
    # Fetch all hosts in us-east-1, the hostname is the public DNS if it exists, otherwise the private IP address
    plugin: aws_ec2
    regions:
      - us-east-1

    # Example using filters, ignoring permission errors, and specifying the hostname precedence
    plugin: aws_ec2
    boto_profile: aws_profile
    regions: # populate inventory with instances in these regions
      - us-east-1
      - us-east-2
    filters:
      # all instances with their `Environment` tag set to `dev`
      tag:Environment: dev
      # all dev and QA hosts
      tag:Environment:
        - dev
        - qa
      instance.group-id: sg-xxxxxxxx
    # ignores 403 errors rather than failing
    strict_permissions: False
    # note: I(hostnames) sets the inventory_hostname. To modify ansible_host without modifying
    # inventory_hostname use compose (see example below).
    hostnames:
      - tag:Name=Tag1,Name=Tag2  # return specific hosts only
      - tag:CustomDNSName
      - dns-name
      - private-ip-address

    # Example using constructed features to create groups and set ansible_host
    plugin: aws_ec2
    regions:
      - us-east-1
      - us-west-1
    # keyed_groups may be used to create custom groups
    strict: False
    keyed_groups:
      # add e.g. x86_64 hosts to an arch_x86_64 group
      - prefix: arch
        key: 'architecture'
      # add hosts to tag_Name_Value groups for each Name/Value tag pair
      - prefix: tag
        key: tags
      # add hosts to e.g. instance_type_z3_tiny
      - prefix: instance_type
        key: instance_type
      # create security_groups_sg_abcd1234 group for each SG
      - key: 'security_groups|json_query("[].group_id")'
        prefix: 'security_groups'
      # create a group for each value of the Application tag
      - key: tags.Application
        separator: ''
      # create a group per region e.g. aws_region_us_east_2
      - key: placement.region
        prefix: aws_region
    # set individual variables with compose
    compose:
      # use the private IP address to connect to the host
      # (note: this does not modify inventory_hostname, which is set via I(hostnames))
      ansible_host: private_ip_address





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/inventory/aws_ec2.py>`_ to improve it.
