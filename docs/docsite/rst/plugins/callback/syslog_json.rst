:source: syslog_json.py


.. _syslog_json_callback:


syslog_json - sends JSON events to syslog
+++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.9

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This plugin logs ansible-playbook and ansible runs to a syslog server in JSON format
- Before 2.4 only environment variables were available for configuration



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this callback.

- whitelist in configuration


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
                    <b>facility</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">user</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_syslog_json ]<br>syslog_facility = user</p>
                                                            </div>
                                                                                                            <div>env:SYSLOG_FACILITY</div>
                                                                                                </td>
                                                <td>
                                                                        <div>syslog facility to log as</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>port</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">514</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_syslog_json ]<br>syslog_port = 514</p>
                                                            </div>
                                                                                                            <div>env:SYSLOG_PORT</div>
                                                                                                </td>
                                                <td>
                                                                        <div>port on which the syslog server is listening</div>
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
                                                    <div> ini entries:
                                                                    <p>[callback_syslog_json ]<br>syslog_server = localhost</p>
                                                            </div>
                                                                                                            <div>env:SYSLOG_SERVER</div>
                                                                                                </td>
                                                <td>
                                                                        <div>syslog server that will receive the event</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/callback/syslog_json.py>`_ to improve it.
