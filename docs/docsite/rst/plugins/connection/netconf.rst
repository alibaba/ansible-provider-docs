:source: netconf.py


.. _netconf_connection:


netconf - Provides a persistent connection using the netconf protocol
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.3

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This connection plugin provides a connection to remote devices over the SSH NETCONF subsystem.  This connection plugin is typically used by network devices for sending and receiving RPC calls over NETCONF.
- Note this connection plugin requires ncclient to be installed on the local Ansible controller.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this connection.

- ncclient


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
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ ]<br> = no</p>
                                                                    <p>[ ]<br> = no</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_HOST_KEY_AUTO_ADD</div>
                                                                                                </td>
                                                <td>
                                                                        <div>By default, Ansible will prompt the user before adding SSH keys to the known hosts file.  Enabling this option, unknown host keys will automatically be added to the known hosts file.</div>
                                                    <div>Be sure to fully understand the security implications of enabling this option on production systems as it could create a security vulnerability.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>host_key_checking</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>host_key_checking = yes</p>
                                                                    <p>[paramiko_connection ]<br>host_key_checking = yes</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_HOST_KEY_CHECKING</div>
                                                            <div>env:ANSIBLE_SSH_HOST_KEY_CHECKING</div>
                                                            <div>env:ANSIBLE_NETCONF_HOST_KEY_CHECKING</div>
                                                                                                                                        <div>var: ansible_host_key_checking</div>
                                                            <div>var: ansible_ssh_host_key_checking</div>
                                                            <div>var: ansible_netconf_host_key_checking</div>
                                                                        </td>
                                                <td>
                                                                        <div>Set this to &quot;False&quot; if you want to avoid host key checking by the underlying tools Ansible uses to connect to the host</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>look_for_keys</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[paramiko_connection ]<br>look_for_keys = yes</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_PARAMIKO_LOOK_FOR_KEYS</div>
                                                                                                </td>
                                                <td>
                                                                        <div>TODO: write it</div>
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
                                                                        <div>Configures the device platform network operating system.  This value is used to load a device specific netconf plugin.  If this option is not configured, then the default netconf plugin will be used.</div>
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
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">830</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>remote_port = 830</p>
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
                                                                        <div>Sets the connection time for the communicating with the remote device. This timeout is used as the default timeout value when awaiting a response after issuing a call to a RPC.  If the RPC does not return in timeout seconds, an error is generated.</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/connection/netconf.py>`_ to improve it.
