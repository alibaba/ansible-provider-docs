:source: script.py


.. _script_inventory:


script - Executes an inventory script that returns JSON
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- The source provided must be an executable that returns Ansible inventory JSON
- The source must accept ``--list`` and ``--host <hostname>`` as arguments. ``--host`` will only be used if no ``_meta`` key is present. This is a performance optimization as the script would be called per host otherwise.




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
                    <b>always_show_stderr</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.5.1)</div>                </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[inventory_plugin_script ]<br>always_show_stderr = yes</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_INVENTORY_PLUGIN_SCRIPT_STDERR</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Toggle display of stderr even when script was successful</div>
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
                                                                    <p>[inventory_plugin_script ]<br>cache = no</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_INVENTORY_PLUGIN_SCRIPT_CACHE</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Toggle the usage of the configured Cache plugin.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - It takes the place of the previously hardcoded script inventory.
    - In order to function, it requires being whitelisted in configuration, which is true by default.






Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/inventory/script.py>`_ to improve it.
