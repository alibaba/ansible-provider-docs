:source: csh.py


.. _csh_shell:


csh - C shell (/bin/csh)
++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- When you have no other option than to use csh




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
                    <b>admin_users</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[u&#39;root&#39;, u&#39;toor&#39;]</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>admin_users = [u'root', u'toor']</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_ADMIN_USERS</div>
                                                                                                                                        <div>var: ansible_admin_users</div>
                                                                        </td>
                                                <td>
                                                                        <div>list of users to be expected to have admin privileges. This is used by the controller to determine how to share temporary files between the remote user and the become user.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>async_dir</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">~/.ansible_async</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>async_dir = ~/.ansible_async</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_ASYNC_DIR</div>
                                                                                                                                        <div>var: ansible_async_dir</div>
                                                                        </td>
                                                <td>
                                                                        <div>Directory in which ansible will keep async job inforamtion</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>environment</b>
                    <br/><div style="font-size: small; color: red">dict</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{}</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>dictionary of environment variables and their values to use when executing commands.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>remote_tmp</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">~/.ansible/tmp</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>remote_tmp = ~/.ansible/tmp</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_REMOTE_TEMP</div>
                                                            <div>env:ANSIBLE_REMOTE_TMP</div>
                                                                                                                                        <div>var: ansible_remote_tmp</div>
                                                                        </td>
                                                <td>
                                                                        <div>Temporary directory to use on targets when executing tasks.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>system_tmpdirs</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[u&#39;/var/tmp&#39;, u&#39;/tmp&#39;]</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>system_tmpdirs = [u'/var/tmp', u'/tmp']</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_SYSTEM_TMPDIRS</div>
                                                                                                                                        <div>var: ansible_system_tmpdirs</div>
                                                                        </td>
                                                <td>
                                                                        <div>List of valid system temporary directories for Ansible to choose when it cannot use ``remote_tmp``, normally due to permission issues.  These must be world readable, writable, and executable.</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/shell/csh.py>`_ to improve it.
