:source: host_group_vars.py


.. _host_group_vars_vars:


host_group_vars - In charge of loading group_vars and host_vars
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Loads YAML vars into corresponding groups/hosts in group_vars/ and host_vars/ directories.
- Files are restricted by extension to one of .yaml, .json, .yml or no extension.
- Hidden (starting with '.') and backup (ending with '~') files and directories are ignored.
- Only applies to inventory sources that are existing paths.




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
                    <b>_valid_extensions</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[u&#39;.yml&#39;, u&#39;.yaml&#39;, u&#39;.json&#39;]</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[yaml_valid_extensions ]<br>defaults = [u'.yml', u'.yaml', u'.json']</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_YAML_FILENAME_EXT</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Check all of these extensions when looking for 'variable' files which should be YAML or JSON or vaulted versions of these.</div>
                                                    <div>This affects vars_files, include_vars, inventory and vars plugins among others.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - It takes the place of the previously hardcoded group_vars/host_vars loading.






Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/vars/host_group_vars.py>`_ to improve it.
