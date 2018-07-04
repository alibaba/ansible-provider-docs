:source: openstack.py


.. _openstack_inventory:


openstack - OpenStack inventory source
++++++++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Get inventory hosts from OpenStack clouds
- Uses openstack.(yml|yaml) YAML configuration file to configure the inventory plugin
- Uses standard clouds.yaml YAML configuration file to configure cloud credentials




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
                    <b>clouds_yaml_path</b>
                    <br/><div style="font-size: small; color: red">string</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Override path to clouds.yaml file. If this value is given it
    will be searched first. The default path for the
    ansible inventory adds /etc/ansible/openstack.yaml and
    /etc/ansible/openstack.yml to the regular locations documented
    at https://docs.openstack.org/os-client-config/latest/user/configuration.html#config-files</div>
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
                                                                        <div>Create vars from jinja2 expressions.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>expand_hostvars</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Run extra commands on each host to fill in additional
    information about the host. May interrogate cinder and
    neutron and can be expensive for people with many hosts.
    (Note, the default value of this is opposite from the default
    old openstack.py inventory script's option expand_hostvars)</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>fail_on_errors</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Causes the inventory to fail and return no hosts if one cloud
    has failed (for example, bad credentials or being offline).
    When set to False, the inventory will return as many hosts as
    it can from as many clouds as it can contact. (Note, the
    default value of this is opposite from the old openstack.py
    inventory script's option fail_on_errors)</div>
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
                                                                        <div>Add hosts to group based on Jinja2 conditionals.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>inventory_hostname</b>
                    <br/><div style="font-size: small; color: red">string</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>name</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>uuid</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>What to register as the inventory hostname.
    If set to 'uuid' the uuid of the server will be used and a
    group will be created for the server name.
    If set to 'name' the name of the server will be used unless
    there are more than one server with the same name in which
    case the 'uuid' logic will be used.
    Default is to do 'name', which is the opposite of the old
    openstack.py inventory script's option use_hostnames)</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>only_clouds</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[]</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>List of clouds from clouds.yaml to use, instead of using
    the whole list.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>private</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Use the private interface of each server, if it has one, as
    the host's IP in the inventory. This can be useful if you are
    running ansible inside a server in the cloud and would rather
    communicate to your servers over the private network.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>show_all</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>toggles showing all vms vs only those with a working IP</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    # file must be named openstack.yaml or openstack.yml
    # Make the plugin behave like the default behavior of the old script
    plugin: openstack
    expand_hostvars: yes
    fail_on_errors: yes





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/inventory/openstack.py>`_ to improve it.
