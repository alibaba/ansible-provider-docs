:source: junit.py


.. _junit_callback:


junit - write playbook output to a JUnit file.
++++++++++++++++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This callback writes playbook output to a JUnit formatted XML file.
- Tasks show up in the report as follows: 'ok': pass 'failed' with 'EXPECTED FAILURE' in the task name: pass 'failed' with 'TOGGLE RESULT' in the task name: pass 'ok' with 'TOGGLE RESULT' in the task name: failure 'failed' due to an exception: error 'failed' for other reasons: failure 'skipped': skipped



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this callback.

- whitelist in configuration
- junit_xml (python lib)


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
                    <b>fail_on_change</b>
                                                                            </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:JUNIT_FAIL_ON_CHANGE</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Consider any tasks reporting &quot;changed&quot; as a junit test failure</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>fail_on_ignore</b>
                                                                            </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:JUNIT_FAIL_ON_IGNORE</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Consider failed tasks as a junit test failure even if ignore_on_error is set</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>include_setup_tasks_in_report</b>
                                                                            </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Should the setup tasks be included in the final report</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>output_dir</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">~/.ansible.log</div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:JUNIT_OUTPUT_DIR</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Directory to write XML files to.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>task_class</b>
                                                                            </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:JUNIT_TASK_CLASS</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Configure the output to be one class per yaml file</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/callback/junit.py>`_ to improve it.
