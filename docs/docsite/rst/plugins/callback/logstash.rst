:source: logstash.py


.. _logstash_callback:


logstash - Sends events to Logstash
+++++++++++++++++++++++++++++++++++

.. versionadded:: 2.3

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This callback will report facts and task events to Logstash https://www.elastic.co/products/logstash



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this callback.

- whitelisting in configuration
- logstash (python library)


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
                    <b>port</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">5000</div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:LOGSTASH_PORT</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Port on which logstash is listening</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>server</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">localhost</div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:LOGSTASH_SERVER</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Address of the Logstash server</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>type</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">ansible</div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:LOGSTASH_TYPE</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Message type</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/callback/logstash.py>`_ to improve it.
