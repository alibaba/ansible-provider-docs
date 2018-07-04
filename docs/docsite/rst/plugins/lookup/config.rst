:source: config.py


.. _config_lookup:


config - Lookup current Ansible configuration values
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Retrieves the value of an Ansible configuration setting.
- You can use ``ansible-config list`` to see all available settings.




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
                    <b>_terms</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>The key(s) to look up</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>on_missing</b>
                    <br/><div style="font-size: small; color: red">string</div>                                                        </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>error</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>skip</li>
                                                                                                                                                                                                <li>warn</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>action to take if term is missing from config</div>
                                                    <div>Error will raise a fatal error</div>
                                                    <div>Skip will just ignore the term</div>
                                                    <div>Warn will skip over it but issue a warning</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
        - name: Show configured default become user
          debug: msg="{{ lookup('config', 'DEFAULT_BECOME_USER')}}"

        - name: print out role paths
          debug:
            msg: "These are the configured role paths: {{lookup('config', 'DEFAULT_ROLES_PATH')}}"

        - name: find retry files, skip if missing that key
          find:
            paths: "{{lookup('config', 'RETRY_FILES_SAVE_PATH')|default(playbook_dir, True)}}"
            patterns: "*.retry"

        - name: see the colors
          debug: msg="{{item}}"
          loop: "{{lookup('config', 'COLOR_OK', 'COLOR_CHANGED', 'COLOR_SKIP', wantlist=True)}}"

        - name: skip if bad value in var
          debug: msg="{{ lookup('config', config_in_var, on_missing='skip')}}"
          var:
            config_in_var: UNKNOWN




Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this lookup:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <b>_raw</b>
                    <br/><div style="font-size: small; color: red"></div>
                                    </td>
                <td></td>
                <td>
                                                                        <div>value(s) of the key(s) in the config</div>
                                                                <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- Ansible Core


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/config.py>`_ to improve it.
