:source: winrm.py


.. _winrm_connection:


winrm - Run tasks over Microsoft's WinRM
++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Run commands or put/fetch on a target via WinRM
- This plugin allows extra arguments to be passed that are supported by the protocol but not explicitly defined here. They should take the form of variables declared with the following pattern `ansible_winrm_<option>`.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this connection.

- pywinrm (python library)


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
                    <b>connection_timeout</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                                    <div>var: ansible_winrm_connection_timeout</div>
                                                                        </td>
                                                <td>
                                                                        <div>Sets the operation and read timeout settings for the WinRM connection.</div>
                                                    <div>Corresponds to the <code>operation_timeout_sec</code> and <code>read_timeout_sec</code> args in pywinrm so avoid setting these vars with this one.</div>
                                                    <div>The default value is whatever is set in the installed version of pywinrm.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kerberos_command</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">kinit</div>
                                    </td>
                                                    <td>
                                                                                                                                    <div>var: ansible_winrm_kinit_cmd</div>
                                                                        </td>
                                                <td>
                                                                        <div>kerberos command to use to request a authentication ticket</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kerberos_mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>managed</li>
                                                                                                                                                                                                <li>manual</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                                                                    <div>var: ansible_winrm_kinit_mode</div>
                                                                        </td>
                                                <td>
                                                                        <div>kerberos usage mode.</div>
                                                    <div>The managed option means Ansible will obtain kerberos ticket.</div>
                                                    <div>While the manual one means a ticket must already have been obtained by the user.</div>
                                                    <div>If having issues with Ansible freezing when trying to obtain the Kerberos ticket, you can either set this to <code>manual</code> and obtain it outside Ansible or install <code>pexpect</code> through pip and try again.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>path</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">/wsman</div>
                                    </td>
                                                    <td>
                                                                                                                                    <div>var: ansible_winrm_path</div>
                                                                        </td>
                                                <td>
                                                                        <div>URI path to connect to</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>port</b>
                    <br/><div style="font-size: small; color: red">integer</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">5986</div>
                                    </td>
                                                    <td>
                                                                                                                                    <div>var: ansible_port</div>
                                                            <div>var: ansible_winrm_port</div>
                                                                        </td>
                                                <td>
                                                                        <div>port for winrm to connect on remote target</div>
                                                    <div>The default is the https (5986) port, if using http it should be 5985</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>remote_addr</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">inventory_hostname</div>
                                    </td>
                                                    <td>
                                                                                                                                    <div>var: ansible_host</div>
                                                            <div>var: ansible_winrm_host</div>
                                                                        </td>
                                                <td>
                                                                        <div>Address of the windows machine</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>remote_user</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                                    <div>var: ansible_user</div>
                                                            <div>var: ansible_winrm_user</div>
                                                                        </td>
                                                <td>
                                                                        <div>The user to log in as to the Windows machine</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>scheme</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>http</li>
                                                                                                                                                                                                <li>https</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                                                                    <div>var: ansible_winrm_scheme</div>
                                                                        </td>
                                                <td>
                                                                        <div>URI scheme to use</div>
                                                    <div>If not set, then will default to <code>https</code> or <code>http</code> if <em>port</em> is <code>5985</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>transport</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                                    <div>var: ansible_winrm_transport</div>
                                                                        </td>
                                                <td>
                                                                        <div>List of winrm transports to attempt to to use (ssl, plaintext, kerberos, etc)</div>
                                                    <div>If None (the default) the plugin will try to automatically guess the correct list</div>
                                                    <div>The choices avialable depend on your version of pywinrm</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>







Status
------




Author
~~~~~~

- Ansible Core Team


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/connection/winrm.py>`_ to improve it.
