:source: hipchat.py


.. _hipchat_callback:


hipchat - post task events to hipchat
+++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.6

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This callback plugin sends status updates to a HipChat channel during playbook execution.
- Before 2.4 only environment variables were available for configuring this plugin.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this callback.

- whitelist in configuration.
- prettytable (python lib)


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
                    <b>api_version</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">v1</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_hipchat ]<br> = v1</p>
                                                                    <p>[ ]<br>api_version = v1</p>
                                                            </div>
                                                                                                            <div>env:HIPCHAT_API_VERSION</div>
                                                                                                </td>
                                                <td>
                                                                        <div>HipChat API version, v1 or v2.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>from</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">ansible</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_hipchat ]<br> = ansible</p>
                                                                    <p>[ ]<br>from = ansible</p>
                                                            </div>
                                                                                                            <div>env:HIPCHAT_FROM</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Name to post as</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>notify</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_hipchat ]<br> = yes</p>
                                                                    <p>[ ]<br>notify = yes</p>
                                                            </div>
                                                                                                            <div>env:HIPCHAT_NOTIFY</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Add notify flag to important messages</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>room</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">ansible</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_hipchat ]<br> = ansible</p>
                                                                    <p>[ ]<br>room = ansible</p>
                                                            </div>
                                                                                                            <div>env:HIPCHAT_ROOM</div>
                                                                                                </td>
                                                <td>
                                                                        <div>HipChat room to post in.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>token</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_hipchat ]<br> = VALUE</p>
                                                                    <p>[ ]<br>token = VALUE</p>
                                                            </div>
                                                                                                            <div>env:HIPCHAT_TOKEN</div>
                                                                                                </td>
                                                <td>
                                                                        <div>HipChat API token for v1 or v2 API.</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/callback/hipchat.py>`_ to improve it.
