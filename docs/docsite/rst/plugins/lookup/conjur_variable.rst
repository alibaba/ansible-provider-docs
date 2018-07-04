:source: conjur_variable.py


.. _conjur_variable_lookup:


conjur_variable - Fetch credentials from CyberArk Conjur.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Retrieves credentials from Conjur using the controlling host's Conjur identity. Conjur info: https://www.conjur.org/.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this lookup.

- The controlling host running Ansible has a Conjur identity. (More: https://developer.conjur.net/key_concepts/machine_identity.html)


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
                    <b>_term</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Variable path</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>config_file</b>
                    <br/><div style="font-size: small; color: red">path</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">/etc/conjur.conf</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[conjur, ]<br>config_file_path = /etc/conjur.conf</p>
                                                            </div>
                                                                                                            <div>env:CONJUR_CONFIG_FILE</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Path to the Conjur configuration file. The configuration file is a YAML file.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>identity_file</b>
                    <br/><div style="font-size: small; color: red">path</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">/etc/conjur.identity</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[conjur, ]<br>identity_file_path = /etc/conjur.identity</p>
                                                            </div>
                                                                                                            <div>env:CONJUR_IDENTITY_FILE</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Path to the Conjur identity file. The identity file follows the netrc file format convention.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
      - debug:
          msg: "{{ lookup('conjur_variable', '/path/to/secret') }}"




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
                                                                        <div>Value stored in Conjur.</div>
                                                                <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------



This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/conjur_variable.py>`_ to improve it.
