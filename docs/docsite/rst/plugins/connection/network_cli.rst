:source: network_cli.py


.. _network_cli_connection:


network_cli - Use network_cli to run command on network appliances
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.3

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This connection plugin provides a connection to remote devices over the SSH and implements a CLI shell.  This connection plugin is typically used by network devices for sending and receiving CLi commands to network devices.




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
                                                                        <div>Specifies the remote device FQDN or IP address to establish the SSH connection to.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>host_key_auto_add</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ ]<br> = no</p>
                                                                    <p>[ ]<br> = no</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_HOST_KEY_AUTO_ADD</div>
                                                                                                </td>
                                                <td>
                                                                        <div>By default, Ansible will prompt the user before adding SSH keys to the known hosts file.  Since persistent connections such as network_cli run in background processes, the user will never be prompted.  By enabling this option, unknown host keys will automatically be added to the known hosts file.</div>
                                                    <div>Be sure to fully understand the security implications of enabling this option on production systems as it could create a security vulnerability.</div>
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
                                                                        <div>Configures the device platform network operating system.  This value is used to load the correct terminal and cliconf plugins to communicate with the remote device</div>
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
                                                            <div>var: ansible_ssh_pass</div>
                                                                        </td>
                                                <td>
                                                                        <div>Configures the user password used to authenticate to the remote device when first establishing the SSH connection.</div>
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
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">22</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>remote_port = 22</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_REMOTE_PORT</div>
                                                                                                                                        <div>var: ansible_port</div>
                                                                        </td>
                                                <td>
                                                                        <div>Specifies the port on the remote device to listening for connections when establishing the SSH connection.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>private_key_file</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ ]<br> = VALUE</p>
                                                                    <p>[ ]<br> = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_PRIVATE_KEY_FILE</div>
                                                                                                                                        <div>var: ansible_private_key_file</div>
                                                                        </td>
                                                <td>
                                                                        <div>The private SSH key or certificate file used to to authenticate to the remote device when first establishing the SSH connection.</div>
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
                                                                        <div>The username used to authenticate to the remote device when the SSH connection is first established.  If the remote_user is not specified, the connection will use the username of the logged in user.</div>
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
                        </table>
    <br/>







Status
------




Author
~~~~~~

- Ansible Networking Team


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/connection/network_cli.py>`_ to improve it.
