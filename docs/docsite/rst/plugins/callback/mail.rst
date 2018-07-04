:source: mail.py


.. _mail_callback:


mail - Sends failure events via email
+++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This callback will report failures via email



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this callback.

- whitelisting in configuration


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
                    <b>bcc</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_mail ]<br>bcc = VALUE</p>
                                                            </div>
                                                                                            </td>
                                                <td>
                                                                        <div>BCC'd recipient</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>cc</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_mail ]<br>cc = VALUE</p>
                                                            </div>
                                                                                            </td>
                                                <td>
                                                                        <div>CC'd recipient</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>mta</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">localhost</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_mail ]<br>smtphost = localhost</p>
                                                            </div>
                                                                                                            <div>env:SMTPHOST</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Mail Transfer Agent, server that accepts SMTP</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>mtaport</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">25</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_mail ]<br>smtpport = 25</p>
                                                            </div>
                                                                                            </td>
                                                <td>
                                                                        <div>Mail Transfer Agent Port, port at which server SMTP</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sender</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_mail ]<br>sender = VALUE</p>
                                                            </div>
                                                                                            </td>
                                                <td>
                                                                        <div>Mail sender</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>to</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">root</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_mail ]<br>to = root</p>
                                                            </div>
                                                                                            </td>
                                                <td>
                                                                        <div>Mail recipient</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>







Status
------




Author
~~~~~~

- Dag Wieers (@dagwieers)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/callback/mail.py>`_ to improve it.
