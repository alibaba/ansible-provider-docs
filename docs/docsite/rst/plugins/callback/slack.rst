:source: slack.py


.. _slack_callback:


slack - Sends play events to a Slack channel
++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.1

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This is an ansible callback plugin that sends status updates to a Slack channel during playbook execution.
- Before 2.4 only environment variables were available for configuring this plugin



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this callback.

- whitelist in configuration
- prettytable (python library)


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
                    <b>channel</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">#ansible</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_slack ]<br>channel = #ansible</p>
                                                            </div>
                                                                                                            <div>env:SLACK_CHANNEL</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Slack room to post in.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>username</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">ansible</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_slack ]<br>username = ansible</p>
                                                            </div>
                                                                                                            <div>env:SLACK_USERNAME</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Username to post as.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>webhook_url</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_slack ]<br>webhook_url = VALUE</p>
                                                            </div>
                                                                                                            <div>env:SLACK_WEBHOOK_URL</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Slack Webhook URL</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/callback/slack.py>`_ to improve it.
