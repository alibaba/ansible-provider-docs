:source: profile_tasks.py


.. _profile_tasks_callback:


profile_tasks - adds time information to tasks
++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Ansible callback plugin for timing individual tasks and overall execution time.
- Mashup of 2 excellent original works: https://github.com/jlafon/ansible-profile, https://github.com/junaid18183/ansible_home/blob/master/ansible_plugins/callback_plugins/timestamp.py.old
- Format: ``<task start timestamp> (<length of previous task>`` <current elapsed playbook execution time>)
- It also lists the top/bottom time consuming tasks in the summary (configurable)
- Before 2.4 only the environment variables were available for configuration.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this callback.

- whitelisting in configuration


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
                    <b>output_limit</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">20</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_profile_tasks ]<br>task_output_limit = 20</p>
                                                            </div>
                                                                                                            <div>env:PROFILE_TASKS_TASK_OUTPUT_LIMIT</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Number of tasks to display in the summary</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sort_order</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>descending</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>ascending</li>
                                                                                                                                                                                                <li>none</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_profile_tasks ]<br>sort_order = descending</p>
                                                            </div>
                                                                                                            <div>env:PROFILE_TASKS_SORT_ORDER</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Adjust the sorting output of summary tasks</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    #
    #    TASK: [ensure messaging security group exists] ********************************
    #    Thursday 11 June 2017  22:50:53 +0100 (0:00:00.721)       0:00:05.322 *********
    #    ok: [localhost]
    #
    #    TASK: [ensure db security group exists] ***************************************
    #    Thursday 11 June 2017  22:50:54 +0100 (0:00:00.558)       0:00:05.880 *********
    #    changed: [localhost]
    #  '





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/callback/profile_tasks.py>`_ to improve it.
