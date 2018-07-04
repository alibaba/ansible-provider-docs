:source: iocage.py


.. _iocage_connection:


iocage - Run tasks in iocage jails
++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Run commands or put/fetch files to an existing iocage jail




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
                    <b>remote_addr</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">The set user as per docker&#39;s configuration</div>
                                    </td>
                                                    <td>
                                                                                                                                    <div>var: ansible_host</div>
                                                            <div>var: ansible_iocage_host</div>
                                                                        </td>
                                                <td>
                                                                        <div>Path to the jail</div>
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
                                                            <div>var: ansible_iocage_user</div>
                                                                        </td>
                                                <td>
                                                                        <div>User to execute as inside the jail</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>







Status
------




Author
~~~~~~

- Stephan Lohse <dev-github@ploek.org>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/connection/iocage.py>`_ to improve it.
