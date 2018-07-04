:source: cgroup_memory_recap.py


.. _cgroup_memory_recap_callback:


cgroup_memory_recap - Profiles maximum memory usage of tasks and full execution using cgroups
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.6

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This is an ansible callback plugin that profiles maximum memory usage of ansible and individual tasks, and displays a recap at the end using cgroups



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this callback.

- whitelist in configuration
- cgroups


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
                    <b>cur_mem_file</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_cgroupmemrecap ]<br>cur_mem_file = VALUE</p>
                                                            </div>
                                                                                                            <div>env:CGROUP_CUR_MEM_FILE</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Path to <code>memory.usage_in_bytes</code> file. Example <code>/sys/fs/cgroup/memory/ansible_profile/memory.usage_in_bytes</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>max_mem_file</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_cgroupmemrecap ]<br>max_mem_file = VALUE</p>
                                                            </div>
                                                                                                            <div>env:CGROUP_MAX_MEM_FILE</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Path to cgroups <code>memory.max_usage_in_bytes</code> file. Example <code>/sys/fs/cgroup/memory/ansible_profile/memory.max_usage_in_bytes</code></div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - Requires ansible to be run from within a cgroup, such as with ``cgexec -g memory:ansible_profile ansible-playbook ...``
    - This cgroup should only be used by ansible to get accurate results
    - To create the cgroup, first use a command such as ``sudo cgcreate -a ec2-user:ec2-user -t ec2-user:ec2-user -g memory:ansible_profile``






Status
------



This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/callback/cgroup_memory_recap.py>`_ to improve it.
