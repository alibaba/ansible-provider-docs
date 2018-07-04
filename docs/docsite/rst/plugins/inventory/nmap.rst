:source: nmap.py


.. _nmap_inventory:


nmap - Uses nmap to find hosts to target
++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.6

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Uses a YAML configuration file with a valid YAML extension.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this inventory.

- nmap CLI installed


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
                    <b>address</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Network IP or range of IPs to scan, you can use a simple range (10.2.2.15-25) or CIDR notation.</div>
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
                    <b>exclude</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>list of addresses to exclude</div>
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
                    <b>ipv4</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>use IPv4 type addresses</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>ipv6</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>use IPv6 type addresses</div>
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
                    <b>ports</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Enable/disable scanning for open ports</div>
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


Notes
-----

.. note::
    - At least one of ipv4 or ipv6 is required to be True, both can be True, but they cannot both be False.
    - TODO: add OS fingerprinting


Examples
--------

.. code-block:: yaml+jinja

    
        # inventory.config file in YAML format
        plugin: nmap
        strict: False
        network: 192.168.0.0/24





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/inventory/nmap.py>`_ to improve it.
