:source: foreman.py


.. _foreman_callback:


foreman - Sends events to Foreman
+++++++++++++++++++++++++++++++++

.. versionadded:: 2.2

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This callback will report facts and task events to Foreman https://theforeman.org/
- Before 2.4, if you wanted to use an ini configuration, the file must be placed in the same directory as this plugin and named foreman.ini
- In 2.4 and above you can just put it in the main Ansible configuration file.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this callback.

- whitelisting in configuration
- requests (python library)


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
                    <b>ssl_cert</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">/etc/foreman/client_cert.pem</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_foreman ]<br>ssl_cert = /etc/foreman/client_cert.pem</p>
                                                            </div>
                                                                                                            <div>env:FOREMAN_SSL_CERT</div>
                                                                                                </td>
                                                <td>
                                                                        <div>X509 certificate to authenticate to Foreman if https is used</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>ssl_key</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">/etc/foreman/client_key.pem</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_foreman ]<br>ssl_key = /etc/foreman/client_key.pem</p>
                                                            </div>
                                                                                                            <div>env:FOREMAN_SSL_KEY</div>
                                                                                                </td>
                                                <td>
                                                                        <div>the corresponding private key</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>url</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">http://localhost:3000</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_foreman ]<br>url = http://localhost:3000</p>
                                                            </div>
                                                                                                            <div>env:FOREMAN_URL</div>
                                                                                                </td>
                                                <td>
                                                                        <div>URL to the Foreman server</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>verify_certs</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">1</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_foreman ]<br>verify_certs = 1</p>
                                                            </div>
                                                                                                            <div>env:FOREMAN_SSL_VERIFY</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Toggle to decidewhether to verify the Foreman certificate.</div>
                                                    <div>It can be set to '1' to verify SSL certificates using the installed CAs or to a path pointing to a CA bundle.</div>
                                                    <div>Set to '0' to disable certificate checking.</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/callback/foreman.py>`_ to improve it.
