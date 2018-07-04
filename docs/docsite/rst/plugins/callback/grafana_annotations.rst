:source: grafana_annotations.py


.. _grafana_annotations_callback:


grafana_annotations - send ansible events as annotations on charts to grafana over http api.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.6

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This callback will report start, failed and stats events to Grafana as annotations (https://grafana.com)



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
                    <b>grafana_api_key</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_grafana_annotations ]<br>grafana_api_key = VALUE</p>
                                                            </div>
                                                                                                            <div>env:GRAFANA_API_KEY</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Grafana API key, allowing to authenticate when posting on the HTTP API. If not provided, grafana_login and grafana_password will be required.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>grafana_dashboard_id</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_grafana_annotations ]<br>grafana_dashboard_id = VALUE</p>
                                                            </div>
                                                                                                            <div>env:GRAFANA_DASHBOARD_ID</div>
                                                                                                </td>
                                                <td>
                                                                        <div>The grafana dashboard id where the annotation shall be created.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>grafana_panel_id</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_grafana_annotations ]<br>grafana_panel_id = VALUE</p>
                                                            </div>
                                                                                                            <div>env:GRAFANA_PANEL_ID</div>
                                                                                                </td>
                                                <td>
                                                                        <div>The grafana panel id where the annotation shall be created.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>grafana_password</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">ansible</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_grafana_annotations ]<br>grafana_password = ansible</p>
                                                            </div>
                                                                                                            <div>env:GRAFANA_PASSWORD</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Grafana password used for authentication. Ignored if grafana_api_key is provided.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>grafana_url</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_grafana_annotations ]<br>grafana_url = VALUE</p>
                                                            </div>
                                                                                                            <div>env:GRAFANA_URL</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Grafana annotations api URL</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>grafana_user</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">ansible</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_grafana_annotations ]<br>grafana_user = ansible</p>
                                                            </div>
                                                                                                            <div>env:GRAFANA_USER</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Grafana user used for authentication. Ignored if grafana_api_key is provided.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>http_agent</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">Ansible (grafana_annotations callback)</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_grafana_annotations ]<br>http_agent = Ansible (grafana_annotations callback)</p>
                                                            </div>
                                                                                                            <div>env:HTTP_AGENT</div>
                                                                                                </td>
                                                <td>
                                                                        <div>The HTTP 'User-agent' value to set in HTTP requets.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>validate_grafana_certs</b>
                                                                            </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_grafana_annotations ]<br>validate_grafana_certs = yes</p>
                                                            </div>
                                                                                                            <div>env:GRAFANA_VALIDATE_CERT</div>
                                                                                                </td>
                                                <td>
                                                                        <div>(bool) validate the SSL certificate of the Grafana server. (For HTTPS url)</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>







Status
------




Author
~~~~~~

- Rémi REY (@rrey)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/callback/grafana_annotations.py>`_ to improve it.
