:source: jabber.py


.. _jabber_callback:


jabber - post task events to a jabber server
++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.2

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- The chatty part of ChatOps with a Hipchat server as a target
- This callback plugin sends status updates to a HipChat channel during playbook execution.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this callback.

- xmpp (python lib https://github.com/ArchipelProject/xmpppy)


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
                    <b>password</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                            <div>env:JABBER_PASS</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Password for the user to the jabber server</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>server</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                            <div>env:JABBER_SERV</div>
                                                                                                </td>
                                                <td>
                                                                        <div>connection info to jabber server</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>to</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                            <div>env:JABBER_TO</div>
                                                                                                </td>
                                                <td>
                                                                        <div>chat identifier that will recieve the message</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>user</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                            <div>env:JABBER_USER</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Jabber user to authenticate as</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/callback/jabber.py>`_ to improve it.
