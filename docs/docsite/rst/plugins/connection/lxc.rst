:source: lxc.py


.. _lxc_connection:


lxc - Run tasks in lxc containers via lxc python library
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Run commands or put/fetch files to an existing lxc container using lxc python library




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
                                                            <div>var: ansible_lxc_executable</div>
                                                                        </td>
                                                <td>
                                                                        <div>Shell executable</div>
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
                                                            <div>var: ansible_lxc_host</div>
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

- Joerg Thalheim <joerg@higgsboson.tk>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/connection/lxc.py>`_ to improve it.
