:source: paramiko_ssh.py


.. _paramiko_ssh_connection:


paramiko_ssh - Run tasks via python ssh (paramiko)
++++++++++++++++++++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Use the python ssh implementation (Paramiko) to connect to targets
- The paramiko transport is provided because many distributions, in particular EL6 and before do not support ControlPersist in their SSH implementations.
- This is needed on the Ansible control machine to be reasonably efficient with connections. Thus paramiko is faster for most users on these platforms. Users with ControlPersist capability can consider using -c ssh or configuring the transport in the configuration file.
- This plugin also borrows a lot of settings from the ssh plugin as they both cover the same protocol.




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
                    <b>host_key_auto_add</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[paramiko_connection ]<br>host_key_auto_add = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_PARAMIKO_HOST_KEY_AUTO_ADD</div>
                                                                                                </td>
                                                <td>
                                                                        <div>TODO: write it</div>
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
                                                            <div>env:ANSIBLE_PARAMIKO_HOST_KEY_CHECKING</div>
                                                                                                                                        <div>var: ansible_host_key_checking</div>
                                                            <div>var: ansible_ssh_host_key_checking</div>
                                                            <div>var: ansible_paramiko_host_key_checking</div>
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
                    <b>password</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                                                    <div>var: ansible_password</div>
                                                            <div>var: ansible_ssh_pass</div>
                                                            <div>var: ansible_paramiko_pass</div>
                                                                        </td>
                                                <td>
                                                                        <div>Secret used to either login the ssh server or as a passphrase for ssh keys that require it</div>
                                                    <div>Can be set from the CLI via the <code>--ask-pass</code> option.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>proxy_command</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue"></div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[paramiko_connection ]<br>proxy_command = </p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_PARAMIKO_PROXY_COMMAND</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Proxy information for running the connection via a jumphost</div>
                                                    <div>Also this plugin will scan 'ssh_args', 'ssh_extra_args' and 'ssh_common_args' from the 'ssh' plugin settings for proxy information if set.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>pty</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[paramiko_connection ]<br>pty = yes</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_PARAMIKO_PTY</div>
                                                                                                </td>
                                                <td>
                                                                        <div>TODO: write it</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>record_host_keys</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[paramiko_connection ]<br>record_host_keys = yes</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_PARAMIKO_RECORD_HOST_KEYS</div>
                                                                                                </td>
                                                <td>
                                                                        <div>TODO: write it</div>
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
                                                            <div>var: ansible_ssh_host</div>
                                                            <div>var: ansible_paramiko_host</div>
                                                                        </td>
                                                <td>
                                                                        <div>Address of the remote target</div>
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
                                                                    <p>[paramiko_connection ]<br>remote_user = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_REMOTE_USER</div>
                                                            <div>env:ANSIBLE_PARAMIKO_REMOTE_USER</div>
                                                                                                                                        <div>var: ansible_user</div>
                                                            <div>var: ansible_ssh_user</div>
                                                            <div>var: ansible_paramiko_user</div>
                                                                        </td>
                                                <td>
                                                                        <div>User to login/authenticate as</div>
                                                    <div>Can be set from the CLI via the <code>--user</code> or <code>-u</code> options.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>use_persistent_connections</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>use_persistent_connections = no</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_USE_PERSISTENT_CONNECTIONS</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Toggles the use of persistence for connections</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/connection/paramiko_ssh.py>`_ to improve it.
