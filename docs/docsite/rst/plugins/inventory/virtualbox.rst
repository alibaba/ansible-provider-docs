:source: virtualbox.py


.. _virtualbox_inventory:


virtualbox - virtualbox inventory source
++++++++++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Get inventory hosts from the local virtualbox installation.
- Uses a <name>.vbox.yaml (or .vbox.yml) YAML configuration file.
- The inventory_hostname is always the 'Name' of the virtualbox instance.




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
                    <b>network_info_path</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">/VirtualBox/GuestInfo/Net/0/V4/IP</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>property path to query for network information (ansible_host)</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>query</b>
                    <br/><div style="font-size: small; color: red">dictionary</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{}</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>create vars from virtualbox properties</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>running_only</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>toggles showing all vms vs only those currently running</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>settings_password_file</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>provide a file containing the settings password (equivalent to --settingspwfile)</div>
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
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    # file must be named vbox.yaml or vbox.yml
    simple_config_file:
        plugin: virtualbox
        settings_password_file: /etc/virtulbox/secrets
        query:
          logged_in_users: /VirtualBox/GuestInfo/OS/LoggedInUsersList
        compose:
          ansible_connection: ('indows' in vbox_Guest_OS)|ternary('winrm', 'ssh')





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/inventory/virtualbox.py>`_ to improve it.
