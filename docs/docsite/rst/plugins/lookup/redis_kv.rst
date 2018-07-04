:source: _redis_kv.py


.. _redis_kv_lookup:


redis_kv - fetch data from Redis
++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2

DEPRECATED
----------
:Removed in Ansible: version: 
:Why: This lookup uses options intermingled with terms which blurs the interface between settings and data
:Alternative: new 'redis' lookup



Synopsis
--------
- this lookup returns a list of items given to it, if any of the top level items is also a list it will flatten it, but it will not recurse



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
                                                                        <div>Two element comma separated strings composed of url of the Redis server and key to query</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    - name: query redis for somekey
      debug: msg="{{ lookup('redis_kv', 'redis://localhost:6379,somekey') }} is value in Redis for somekey"




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
                                            <div>values stored in Redis</div>
                                        <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------

This module is flagged as **deprecated** and will be removed in version . For more information see `DEPRECATED`_.


Author
~~~~~~

- Jan-Piet Mens <jpmens(at)gmail.com>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/_redis_kv.py>`_ to improve it.
