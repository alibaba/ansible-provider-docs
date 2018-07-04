:source: foreman.py


.. _foreman_inventory:


foreman - foreman inventory source
++++++++++++++++++++++++++++++++++

.. versionadded:: 2.6

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Get inventory hosts from the foreman service.




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
                    <b>group_prefix</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">foreman_</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>prefix to apply to foreman groups</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>password</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>forman authentication password</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>url</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">http://localhost:300</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>url to foreman</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>user</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>foreman authentication user</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>validate_certs</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>verify SSL certificate if using https</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>vars_prefix</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">foreman_</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>prefix to apply to host variables, does not include facts nor params</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>want_facts</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Toggle, if True the plugin will retrieve host facts from the server</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>want_params</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Toggle, if true the inventory will retrieve 'all_parameters' information as host vars</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>







Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/inventory/foreman.py>`_ to improve it.
