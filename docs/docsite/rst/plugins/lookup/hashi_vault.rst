:source: hashi_vault.py


.. _hashi_vault_lookup:


hashi_vault - retrieve secrets from HashiCorp's vault
+++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- retrieve secrets from HashiCorp's vault



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this lookup.

- hvac (python library)


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
                    <b>auth_method</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>authentication method used</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>cacert</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>path to certificate to use for authentication</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>mount_point</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">ldap</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>vault mount point, only required if you have a custom mount point</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>password</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>authentication password</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>role_id</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                            <div>env:VAULT_ROLE_ID</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Role id for a vault AppRole auth</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>secret</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>query you are making</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>secret_id</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                            <div>env:VAULT_SECRET_ID</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Secret id for a vault AppRole auth</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>token</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                            <div>env:VAULT_TOKEN</div>
                                                                                                </td>
                                                <td>
                                                                        <div>vault token</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>url</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">http://127.0.0.1:8200</div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:VAULT_ADDR</div>
                                                                                                </td>
                                                <td>
                                                                        <div>url to vault service</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>username</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>authentication user name</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>validate_certs</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>controls verification and validation of SSL certificates, mostly you only want to turn off with self signed ones.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - Due to a current limitation in the HVAC library there won't necessarily be an error if a bad endpoint is specified.


Examples
--------

.. code-block:: yaml+jinja

    
    - debug:
        msg: "{{ lookup('hashi_vault', 'secret=secret/hello:value token=c975b780-d1be-8016-866b-01d0f9b688a5 url=http://myvault:8200')}}"

    - name: Return all secrets from a path
      debug:
        msg: "{{ lookup('hashi_vault', 'secret=secret/hello token=c975b780-d1be-8016-866b-01d0f9b688a5 url=http://myvault:8200')}}"

    - name: Vault that requires authentication via LDAP
      debug:
          msg: "{{ lookup('hashi_vault', 'secret=secret/hello:value auth_method=ldap mount_point=ldap username=myuser password=mypas url=http://myvault:8200')}}"

    - name: Using an ssl vault
      debug:
          msg: "{{ lookup('hashi_vault', 'secret=secret/hola:value token=c975b780-d1be-8016-866b-01d0f9b688a5 url=https://myvault:8200 validate_certs=False')}}"

    - name: using certificate auth
      debug:
          msg: "{{ lookup('hashi_vault', 'secret=secret/hi:value token=xxxx-xxx-xxx url=https://myvault:8200 validate_certs=True cacert=/cacert/path/ca.pem')}}"

    - name: authenticate with a Vault app role
      debug:
          msg: "{{ lookup('hashi_vault', 'secret=secret/hello:value auth_method=approle role_id=myroleid secret_id=mysecretid url=http://myvault:8200')}}"




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
                                                                        <div>secrets(s) requested</div>
                                                                <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- Jonathan Davila <jdavila(at)ansible.com>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/hashi_vault.py>`_ to improve it.
