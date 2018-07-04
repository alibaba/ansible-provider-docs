:source: mongodb.py


.. _mongodb_cache:


mongodb - Use MongoDB for caching
+++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This cache uses per host records saved in MongoDB.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this cache.

- pymongo>=3


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
                    <b>_prefix</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>fact_caching_prefix = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_CACHE_PLUGIN_PREFIX</div>
                                                                                                </td>
                                                <td>
                                                                        <div>User defined prefix to use when creating the DB entries</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>_timeout</b>
                    <br/><div style="font-size: small; color: red">integer</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">86400</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>fact_caching_timeout = 86400</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_CACHE_PLUGIN_TIMEOUT</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Expiration timeout in seconds for the cache plugin data</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>_uri</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>fact_caching_connection = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_CACHE_PLUGIN_CONNECTION</div>
                                                                                                </td>
                                                <td>
                                                                        <div>MongoDB Connection String URI</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>







Status
------



This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/cache/mongodb.py>`_ to improve it.
