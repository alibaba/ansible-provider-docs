:source: pickle.py


.. _pickle_cache:


pickle - Pickle formatted files.
++++++++++++++++++++++++++++++++

.. versionadded:: 2.3

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This cache uses Python's pickle serialization format, in per host files, saved to the filesystem.




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
                                                                        <div>User defined prefix to use when creating the files</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>_timeout</b>
                                                                            </td>
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
                                                                        <div>Expiration timeout for the cache plugin data</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>_uri</b>
                    <br/><div style="font-size: small; color: red">list</div>                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>fact_caching_connection = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_CACHE_PLUGIN_CONNECTION</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Path in which the cache plugin will save the files</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>







Status
------




Author
~~~~~~

- Brian Coca (@bcoca)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/cache/pickle.py>`_ to improve it.
