:source: cyberarkpassword.py


.. _cyberarkpassword_lookup:


cyberarkpassword - get secrets from CyberArk AIM
++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Get secrets from CyberArk AIM.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this lookup.

- CyberArk AIM tool installed


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
                    <b>_command</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">/opt/CARKaim/sdk/clipasswordsdk</div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:AIM_CLIPASSWORDSDK_CMD</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Cyberark CLI utility.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>_extra</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>for extra_parms values please check parameters for clipasswordsdk in CyberArk's &quot;Credential Provider and ASCP Implementation Guide&quot;</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>appid</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Defines the unique ID of the application that is issuing the password request.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>output</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">password</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Specifies the desired output fields separated by commas.</div>
                                                    <div>They could be: Password, PassProps.&lt;property&gt;, PasswordChangeInProcess</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>query</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Describes the filter criteria for the password retrieval.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
      - name: passing options to the lookup
        debug: msg={{ lookup("cyberarkpassword", cyquery)}}
        vars:
          cyquery:
            appid: "app_ansible"
            query": "safe=CyberArk_Passwords;folder=root;object=AdminPass"
            output: "Password,PassProps.UserName,PassProps.Address,PasswordChangeInProcess"


      - name: used in a loop
        debug: msg={{item}}
        with_cyberarkpassword:
            appid: 'app_ansible'
            query: 'safe=CyberArk_Passwords;folder=root;object=AdminPass'
            output: 'Password,PassProps.UserName,PassProps.Address,PasswordChangeInProcess'




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
                    <b>passprops</b>
                    <br/><div style="font-size: small; color: red">dictionary</div>
                                    </td>
                <td></td>
                <td>
                                            <div>properties assigned to the entry</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <b>password</b>
                    <br/><div style="font-size: small; color: red"></div>
                                    </td>
                <td></td>
                <td>
                                                                        <div>The actual value stored</div>
                                                                <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <b>passwordchangeinprocess</b>
                    <br/><div style="font-size: small; color: red"></div>
                                    </td>
                <td></td>
                <td>
                                            <div>did the password change?</div>
                                        <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/cyberarkpassword.py>`_ to improve it.
