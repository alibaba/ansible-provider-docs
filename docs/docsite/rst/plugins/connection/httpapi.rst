:source: httpapi.py


.. _httpapi_connection:


httpapi - Use httpapi to run command on network appliances
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.6

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This connection plugin provides a connection to remote devices over a HTTP(S)-based api.




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
                    <b>become</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ ]<br> = no</p>
                                                                    <p>[ ]<br> = no</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_BECOME</div>
                                                                                                                                        <div>var: ansible_become</div>
                                                                        </td>
                                                <td>
                                                                        <div>The become option will instruct the CLI session to attempt privilege escalation on platforms that support it.  Normally this means transitioning from user mode to <code>enable</code> mode in the CLI session. If become is set to True and the remote device does not support privilege escalation or the privilege has already been elevated, then this option is silently ignored</div>
                                                    <div>Can be configured form the CLI via the <code>--become</code> or <code>-b</code> options</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>become_method</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">sudo</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ ]<br> = sudo</p>
                                                                    <p>[ ]<br> = sudo</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_BECOME_METHOD</div>
                                                                                                                                        <div>var: ansible_become_method</div>
                                                                        </td>
                                                <td>
                                                                        <div>This option allows the become method to be specified in for handling privilege escalation.  Typically the become_method value is set to <code>enable</code> but could be defined as other values.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>host</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">inventory_hostname</div>
                                    </td>
                                                    <td>
                                                                                                                                    <div>var: ansible_host</div>
                                                                        </td>
                                                <td>
                                                                        <div>Specifies the remote device FQDN or IP address to establish the HTTP(S) connection to.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>network_os</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                                    <div>var: ansible_network_os</div>
                                                                        </td>
                                                <td>
                                                                        <div>Configures the device platform network operating system.  This value is used to load the correct httpapi and cliconf plugins to communicate with the remote device</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>password</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                                    <div>var: ansible_password</div>
                                                            <div>var: ansible_httpapi_pass</div>
                                                                        </td>
                                                <td>
                                                                        <div>Secret used to authenticate</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>persistent_command_timeout</b>
                    <br/><div style="font-size: small; color: red">int</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">10</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[persistent_connection ]<br>command_timeout = 10</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_PERSISTENT_COMMAND_TIMEOUT</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Configures, in seconds, the amount of time to wait for a command to return from the remote device.  If this timer is exceeded before the command returns, the connection plugin will raise an exception and close</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>persistent_connect_timeout</b>
                    <br/><div style="font-size: small; color: red">int</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">30</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[persistent_connection ]<br>connect_timeout = 30</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_PERSISTENT_CONNECT_TIMEOUT</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Configures, in seconds, the amount of time to wait when trying to initially establish a persistent connection.  If this value expires before the connection to the remote device is completed, the connection will fail</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>port</b>
                    <br/><div style="font-size: small; color: red">int</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>remote_port = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_REMOTE_PORT</div>
                                                                                                                                        <div>var: ansible_httpapi_port</div>
                                                                        </td>
                                                <td>
                                                                        <div>Specifies the port on the remote device to listening for connections when establishing the HTTP(S) connection. When unspecified, will pick 80 or 443 based on the value of use_ssl</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>remote_user</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>remote_user = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_REMOTE_USER</div>
                                                                                                                                        <div>var: ansible_user</div>
                                                                        </td>
                                                <td>
                                                                        <div>The username used to authenticate to the remote device when the API connection is first established.  If the remote_user is not specified, the connection will use the username of the logged in user.</div>
                                                    <div>Can be configured form the CLI via the <code>--user</code> or <code>-u</code> options</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>timeout</b>
                    <br/><div style="font-size: small; color: red">int</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">120</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Sets the connection time, in seconds, for the communicating with the remote device.  This timeout is used as the default timeout value for commands when issuing a command to the network CLI.  If the command does not return in timeout seconds, the an error is generated.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>use_ssl</b>
                                                                            </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                                                                                                    <div>var: ansible_httpapi_use_ssl</div>
                                                                        </td>
                                                <td>
                                                                        <div>Whether to connect using SSL (HTTPS) or not (HTTP)</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>validate_certs</b>
                                                            <br/><div style="font-size: small; color: darkgreen">(added in 2.7)</div>                </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                    <td>
                                                                                                                                    <div>var: ansible_httpapi_validate_certs</div>
                                                                        </td>
                                                <td>
                                                                        <div>Whether to validate SSL certificates</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>







Status
------




Author
~~~~~~

- Ansible Networking Team


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/connection/httpapi.py>`_ to improve it.
