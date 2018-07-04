:source: chroot.py


.. _chroot_connection:


chroot - Interact with local chroot
+++++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Run commands or put/fetch files to an existing chroot on the Ansible controller.




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
                    <b>executable</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>executable = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_EXECUTABLE</div>
                                                                                                                                        <div>var: ansible_executable</div>
                                                                        </td>
                                                <td>
                                                                        <div>User specified executable shell</div>
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
                                                                        </td>
                                                <td>
                                                                        <div>The path of the chroot you want to access.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>







Status
------




Author
~~~~~~

- Maykel Moya <mmoya@speedyrails.com>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/connection/chroot.py>`_ to improve it.
