:source: consul_kv.py


.. _consul_kv_lookup:


consul_kv - Fetch  metadata from a Consul key value store.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.9

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Lookup metadata for a playbook from the key value store in a Consul cluster. Values can be easily set in the kv store with simple rest commands
- ``curl -X PUT -d 'some-value' http://localhost:8500/v1/kv/ansible/somedata``



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this lookup.

- python-consul python library https://python-consul.readthedocs.io/en/latest/#installation


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
                    <b>_raw</b>
                    <br/><div style="font-size: small; color: red">list</div>                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>List of key(s) to retrieve.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>host</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">localhost</div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:ANSIBLE_CONSUL_URL</div>
                                                                                                </td>
                                                <td>
                                                                        <div>The target to connect to, must be a resolvable address.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>index</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>If the key has a value with the specified index then this is returned allowing access to historical values.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>port</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">8500</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>The port of the target host to connect to.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>recurse</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>If true, will retrieve all the values that have the given key as prefix.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>token</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>The acl token to allow access to restricted values.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
      - debug:
          msg: 'key contains {{item}}'
        with_consul_kv:
          - 'key/to/retrieve'

      - name: Parameters can be provided after the key be more specific about what to retrieve
        debug:
          msg: 'key contains {{item}}'
        with_consul_kv:
          - 'key/to recurse=true token=E6C060A9-26FB-407A-B83E-12DDAFCB4D98'

      - name: retrieving a KV from a remote cluster on non default port
        debug:
          msg: "{{ lookup('consul_kv', 'my/key', host='10.10.10.10', port='2000') }}"




Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this lookup:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <b>_raw</b>
                    <br/><div style="font-size: small; color: red"></div>
                                    </td>
                <td></td>
                <td>
                                                                        <div>Value(s) stored in consul.</div>
                                                                <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/consul_kv.py>`_ to improve it.
