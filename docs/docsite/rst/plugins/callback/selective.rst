:source: selective.py


.. _selective_callback:


selective - only print certain tasks
++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This callback only prints tasks that have been tagged with `print_action` or that have failed. This allows operators to focus on the tasks that provide value only.
- Tasks that are not printed are placed with a '.'.
- If you increase verbosity all tasks are printed.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this callback.

- set as main display callback


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
                    <b>nocolor</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br> = no</p>
                                                                    <p>[ ]<br>nocolor = no</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_NOCOLOR</div>
                                                            <div>env:ANSIBLE_SELECTIVE_DONT_COLORIZE</div>
                                                                                                </td>
                                                <td>
                                                                        <div>This setting allows suppressing colorizing output</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
      - debug: msg="This will not be printed"
      - debug: msg="But this will"
        tags: [print_action]





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/callback/selective.py>`_ to improve it.
