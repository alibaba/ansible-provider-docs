:source: etcd.py


.. _etcd_lookup:


etcd - get info from an etcd server
+++++++++++++++++++++++++++++++++++

.. versionadded:: 2.1

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Retrieves data from an etcd server




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
                    <b>_terms</b>
                    <br/><div style="font-size: small; color: red">list</div>                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>the list of keys to lookup on the etcd server</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>url</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">http://127.0.0.1:4001</div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:ANSIBLE_ETCD_URL</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Environment variable with the url for the etcd server</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>validate_certs</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>toggle checking that the ssl certificates are valid, you normally only want to turn this off with self-signed certs.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>version</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">v1</div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:ANSIBLE_ETCD_VERSION</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Environment variable with the etcd protocol version</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
        - name: "a value from a locally running etcd"
          debug: msg={{ lookup('etcd', 'foo/bar') }}

        - name: "values from multiple folders on a locally running etcd"
          debug: msg={{ lookup('etcd', 'foo', 'bar', 'baz') }}

        - name: "since Ansible 2.5 you can set server options inline"
          debug: msg="{{ lookup('etcd', 'foo', version='v2', url='http://192.168.0.27:4001') }}"




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
                    <br/><div style="font-size: small; color: red">list</div>
                                    </td>
                <td></td>
                <td>
                                                                        <div>list of values associated with input keys</div>
                                                                <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- Jan-Piet Mens (@jpmens)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/etcd.py>`_ to improve it.
