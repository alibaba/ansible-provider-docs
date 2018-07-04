:source: powershell.py


.. _powershell_shell:


powershell - Windows Powershell
+++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- The only option when using 'winrm' as a connection plugin




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
                    <b>environment</b>
                    <br/><div style="font-size: small; color: red">dict</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{}</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Dictionary of environment variables and their values to use when executing commands.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>remote_tmp</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">%TEMP%</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[powershell ]<br>remote_tmp = %TEMP%</p>
                                                            </div>
                                                                                                                                    <div>var: ansible_remote_tmp</div>
                                                                        </td>
                                                <td>
                                                                        <div>Temporary directory to use on targets when copying files to the host.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>set_module_language</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Controls if we set the locale for moduels when executing on the target.</div>
                                                    <div>Windows only supports <code>no</code> as an option.</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/shell/powershell.py>`_ to improve it.
