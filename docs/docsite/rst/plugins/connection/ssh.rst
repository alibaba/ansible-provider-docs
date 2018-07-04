:source: ssh.py


.. _ssh_connection:


ssh - connect via ssh client binary
+++++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This connection plugin allows ansible to communicate to the target machines via normal ssh command line.
- Ansible does not expose a channel to allow communication between the user and the ssh process to accept a password manually to decrypt an ssh key when using this connection plugin (which is the default). The use of ``ssh-agent`` is highly recommended.




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
                    <b>control_path</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ssh_connection ]<br>control_path = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_SSH_CONTROL_PATH</div>
                                                                                                                                        <div>var: ansible_control_path</div>
                                                                        </td>
                                                <td>
                                                                        <div>This is the location to save ssh's ControlPath sockets, it uses ssh's variable substitution.</div>
                                                    <div>Since 2.3, if null, ansible will generate a unique hash. Use `%(directory)s` to indicate where to use the control dir path setting.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>control_path_dir</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">~/.ansible/cp</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ssh_connection ]<br>control_path_dir = ~/.ansible/cp</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_SSH_CONTROL_PATH_DIR</div>
                                                                                                                                        <div>var: ansible_control_path_dir</div>
                                                                        </td>
                                                <td>
                                                                        <div>This sets the directory to use for ssh control path if the control path setting is null.</div>
                                                    <div>Also, provides the `%(directory)s` variable for the control path setting.</div>
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
                                                            <div>var: ansible_ssh_host</div>
                                                                        </td>
                                                <td>
                                                                        <div>Hostname/ip to connect to.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>host_key_checking</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>host_key_checking = VALUE</p>
                                                                    <p>[ssh_connection ]<br>host_key_checking = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_HOST_KEY_CHECKING</div>
                                                            <div>env:ANSIBLE_SSH_HOST_KEY_CHECKING</div>
                                                                                                                                        <div>var: ansible_host_key_checking</div>
                                                            <div>var: ansible_ssh_host_key_checking</div>
                                                                        </td>
                                                <td>
                                                                        <div>Determines if ssh should check host keys</div>
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
                                                                        <div>Authentication password for the <code>remote_user</code>. Can be supplied as CLI option.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>pipelining</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">ANSIBLE_PIPELINING</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>pipelining = ANSIBLE_PIPELINING</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_PIPELINING</div>
                                                                                                                                        <div>var: ansible_pipelining</div>
                                                            <div>var: ansible_ssh_pipelining</div>
                                                                        </td>
                                                <td>
                                                                        <div>Pipelining reduces the number of SSH operations required to execute a module on the remote server, by executing many Ansible modules without actual file transfer.</div>
                                                    <div>This can result in a very significant performance improvement when enabled.</div>
                                                    <div>However this conflicts with privilege escalation (become). For example, when using sudo operations you must first disable 'requiretty' in the sudoers file for the target hosts, which is why this feature is disabled by default.</div>
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
                                                            <div>var: ansible_ssh_port</div>
                                                                        </td>
                                                <td>
                                                                        <div>Remote port to connect to.</div>
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
                                                                    <p>[defaults ]<br>private_key_file = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_PRIVATE_KEY_FILE</div>
                                                                                                                                        <div>var: ansible_private_key_file</div>
                                                            <div>var: ansible_ssh_private_key_file</div>
                                                                        </td>
                                                <td>
                                                                        <div>Path to private key file to use for authentication</div>
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
                                                            <div>var: ansible_ssh_user</div>
                                                                        </td>
                                                <td>
                                                                        <div>User name with which to login to the remote server, normally set by the remote_user keyword.</div>
                                                    <div>If no user is supplied, Ansible will let the ssh client binary choose the user as it normally</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>retries</b>
                    <br/><div style="font-size: small; color: red">integer</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">3</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[connection ]<br>retries = 3</p>
                                                                    <p>[ssh_connection ]<br>retries = 3</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_SSH_RETRIES</div>
                                                                                                                                        <div>var: ansible_ssh_retries</div>
                                                                        </td>
                                                <td>
                                                                        <div>Number of attempts to connect.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>scp_executable</b>
                                                            <br/><div style="font-size: small; color: darkgreen">(added in 2.6)</div>                </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">scp</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ssh_connection ]<br>scp_executable = scp</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_SCP_EXECUTABLE</div>
                                                                                                                                        <div>var: ansible_scp_executable</div>
                                                                        </td>
                                                <td>
                                                                        <div>This defines the location of the scp binary. It defaults to `scp` which will use the first binary available in $PATH.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>scp_extra_args</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ssh_connection ]<br>scp_extra_args = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_SCP_EXTRA_ARGS</div>
                                                                                                                                        <div>var: ansible_scp_extra_args</div>
                                                                        </td>
                                                <td>
                                                                        <div>Extra exclusive to the ``scp`` CLI</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>scp_if_ssh</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">smart</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ssh_connection ]<br>scp_if_ssh = smart</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_SCP_IF_SSH</div>
                                                                                                                                        <div>var: ansible_scp_if_ssh</div>
                                                                        </td>
                                                <td>
                                                                        <div>Prefered method to use when transfering files over ssh</div>
                                                    <div>When set to smart, Ansible will try them until one succeeds or they all fail</div>
                                                    <div>If set to True, it will force 'scp', if False it will use 'sftp'</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sftp_batch_mode</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ssh_connection ]<br>sftp_batch_mode = yes</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_SFTP_BATCH_MODE</div>
                                                                                                                                        <div>var: ansible_sftp_batch_mode</div>
                                                                        </td>
                                                <td>
                                                                        <div>TODO: write it</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sftp_executable</b>
                                                            <br/><div style="font-size: small; color: darkgreen">(added in 2.6)</div>                </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">sftp</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ssh_connection ]<br>sftp_executable = sftp</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_SFTP_EXECUTABLE</div>
                                                                                                                                        <div>var: ansible_sftp_executable</div>
                                                                        </td>
                                                <td>
                                                                        <div>This defines the location of the sftp binary. It defaults to ``sftp`` which will use the first binary available in $PATH.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sftp_extra_args</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ssh_connection ]<br>sftp_extra_args = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_SFTP_EXTRA_ARGS</div>
                                                                                                                                        <div>var: ansible_sftp_extra_args</div>
                                                                        </td>
                                                <td>
                                                                        <div>Extra exclusive to the ``sftp`` CLI</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>ssh_args</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">-C -o ControlMaster=auto -o ControlPersist=60s</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ssh_connection ]<br>ssh_args = -C -o ControlMaster=auto -o ControlPersist=60s</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_SSH_ARGS</div>
                                                                                                                                        <div>var: ansible_ssh_args</div>
                                                                        </td>
                                                <td>
                                                                        <div>Arguments to pass to all ssh cli tools</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>ssh_common_args</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ssh_connection ]<br>ssh_common_args = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_SSH_COMMON_ARGS</div>
                                                                                                                                        <div>var: ansible_ssh_common_args</div>
                                                                        </td>
                                                <td>
                                                                        <div>Common extra args for all ssh CLI tools</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>ssh_executable</b>
                                                            <br/><div style="font-size: small; color: darkgreen">(added in 2.2)</div>                </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">ssh</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ssh_connection ]<br>ssh_executable = ssh</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_SSH_EXECUTABLE</div>
                                                                                                                                        <div>var: ansible_ssh_executable</div>
                                                                        </td>
                                                <td>
                                                                        <div>This defines the location of the ssh binary. It defaults to ``ssh`` which will use the first ssh binary available in $PATH.</div>
                                                    <div>This option is usually not required, it might be useful when access to system ssh is restricted, or when using ssh wrappers to connect to remote hosts.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>ssh_extra_args</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ssh_connection ]<br>ssh_extra_args = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_SSH_EXTRA_ARGS</div>
                                                                                                                                        <div>var: ansible_ssh_extra_args</div>
                                                                        </td>
                                                <td>
                                                                        <div>Extra exclusive to the 'ssh' CLI</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>use_tty</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.5)</div>                </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[ssh_connection ]<br>usetty = yes</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_SSH_USETTY</div>
                                                                                                                                        <div>var: ansible_ssh_use_tty</div>
                                                                        </td>
                                                <td>
                                                                        <div>add -tt to ssh commands to force tty allocation</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>







Status
------




Author
~~~~~~

- ansible (@core)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/connection/ssh.py>`_ to improve it.
