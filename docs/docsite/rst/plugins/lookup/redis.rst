:source: redis.py


.. _redis_lookup:


redis - fetch data from Redis
+++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This lookup returns a list of results from a Redis DB corresponding to a list of items given to it



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this lookup.

- redis (python library https://github.com/andymccurdy/redis-py/)


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
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>list of keys to query</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>host</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">127.0.0.1</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[lookup_redis ]<br>host = 127.0.0.1</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_REDIS_HOST</div>
                                                                                                </td>
                                                <td>
                                                                        <div>location of Redis host</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>port</b>
                    <br/><div style="font-size: small; color: red">int</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">6379A</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[lookup_redis ]<br>port = 6379A</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_REDIS_PORT</div>
                                                                                                </td>
                                                <td>
                                                                        <div>port on which Redis is listening on</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>socket</b>
                    <br/><div style="font-size: small; color: red">path</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[lookup_redis ]<br>socket = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_REDIS_SOCKET</div>
                                                                                                </td>
                                                <td>
                                                                        <div>path to socket on which to query Redis, this option overrides host and port options when set.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    - name: query redis for somekey (default or configured settings used)
      debug: msg="{{ lookup('redis', 'somekey'}}"

    - name: query redis for list of keys and non-default host and port
      debug: msg="{{ lookup('redis', item, host='myredis.internal.com', port=2121) }}"
      loop: '{{list_of_redis_keys}}'

    - name: use list directly
      debug: msg="{{ lookup('redis', 'key1', 'key2', 'key3') }}"

    - name: use list directly with a socket
      debug: msg="{{ lookup('redis', 'key1', 'key2', socket='/var/tmp/redis.sock') }}"





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
                                            <div>value(s) stored in Redis</div>
                                        <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- Jan-Piet Mens (@jpmens) <jpmens(at)gmail.com>
- Ansible Core


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/redis.py>`_ to improve it.
