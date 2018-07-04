:source: lxd.py


.. _lxd_connection:


lxd - Run tasks in lxc containers via lxc CLI
+++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Run commands or put/fetch files to an existing lxc container using lxc CLI




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
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">/bin/sh</div>
                                    </td>
                                                    <td>
                                                                                                                                    <div>var: ansible_executable</div>
                                                            <div>var: ansible_lxd_executable</div>
                                                                        </td>
                                                <td>
                                                                        <div>shell to use for execution inside container</div>
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
                                                            <div>var: ansible_lxd_host</div>
                                                                        </td>
                                                <td>
                                                                        <div>Container identifier</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>







Status
------




Author
~~~~~~

- Matt Clay <matt@mystile.com>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/connection/lxd.py>`_ to improve it.
