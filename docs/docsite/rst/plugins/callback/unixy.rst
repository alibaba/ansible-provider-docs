:source: unixy.py


.. _unixy_callback:


unixy - condensed Ansible output
++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Consolidated Ansible output in the style of LINUX/UNIX startup logs.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this callback.

- set as stdout in configuration


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
                    <b>display_failed_stderr</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.7)</div>                </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>display_failed_stderr = no</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_DISPLAY_FAILED_STDERR</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Toggle to control whether failed tasks are displayed to STDERR (vs. STDOUT)</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>display_ok_hosts</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.7)</div>                </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>display_ok_hosts = yes</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_DISPLAY_OK_HOSTS</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Toggle to control displaying 'ok' task/host results in a task</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>display_skipped_hosts</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>display_skipped_hosts = yes</p>
                                                            </div>
                                                                                                            <div>env:DISPLAY_SKIPPED_HOSTS</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Toggle to control displaying skipped task/host results in a task</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>show_custom_stats</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>show_custom_stats = no</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_SHOW_CUSTOM_STATS</div>
                                                                                                </td>
                                                <td>
                                                                        <div>This adds the custom stats set via the set_stats plugin to the play recap</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>







Status
------




Author
~~~~~~

- Allyson Bowles <@akatch>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/callback/unixy.py>`_ to improve it.
