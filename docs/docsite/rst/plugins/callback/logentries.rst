:source: logentries.py


.. _logentries_callback:


logentries - Sends events to Logentries
+++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This callback plugin will generate JSON objects and send them to Logentries via TCP for auditing/debugging purposes.
- Before 2.4, if you wanted to use an ini configuration, the file must be placed in the same directory as this plugin and named logentries.ini
- In 2.4 and above you can just put it in the main Ansible configuration file.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this callback.

- whitelisting in configuration
- certifi (python library)
- flatdict (pytnon library), if you want to use the 'flatten' option


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
                    <b>api</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">data.logentries.com</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_logentries ]<br>api = data.logentries.com</p>
                                                            </div>
                                                                                                            <div>env:LOGENTRIES_API</div>
                                                                                                </td>
                                                <td>
                                                                        <div>URI to the Logentries API</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>flatten</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_logentries ]<br>flatten = no</p>
                                                            </div>
                                                                                                            <div>env:LOGENTRIES_FLATTEN</div>
                                                                                                </td>
                                                <td>
                                                                        <div>flatten complex data structures into a single dictionary with complex keys</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>port</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">80</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_logentries ]<br>port = 80</p>
                                                            </div>
                                                                                                            <div>env:LOGENTRIES_PORT</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Http port to use when connecting to the API</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>tls_port</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">443</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_logentries ]<br>tls_port = 443</p>
                                                            </div>
                                                                                                            <div>env:LOGENTRIES_TLS_PORT</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Port to use when connecting to the API when TLS is enabled</div>
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
                                                                    <p>[callback_logentries ]<br>token = VALUE</p>
                                                            </div>
                                                                                                            <div>env:LOGENTRIES_ANSIBLE_TOKEN</div>
                                                                                                </td>
                                                <td>
                                                                        <div>The logentries &quot;TCP token&quot;</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>use_tls</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_logentries ]<br>use_tls = no</p>
                                                            </div>
                                                                                                            <div>env:LOGENTRIES_USE_TLS</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Toggle to decidewhether to use TLS to encrypt the communications with the API server</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    examples: >
      To enable, add this to your ansible.cfg file in the defaults block

        [defaults]
        callback_whitelist = logentries

      Either set the environment variables
        export LOGENTRIES_API=data.logentries.com
        export LOGENTRIES_PORT=10000
        export LOGENTRIES_ANSIBLE_TOKEN=dd21fc88-f00a-43ff-b977-e3a4233c53af

      Or in the main Ansible config file
        [callback_logentries]
        api = data.logentries.com
        port = 10000
        tls_port = 20000
        use_tls = no
        token = dd21fc88-f00a-43ff-b977-e3a4233c53af
        flatten = False





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/callback/logentries.py>`_ to improve it.
