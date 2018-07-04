:source: keyring.py


.. _keyring_lookup:


keyring - grab secrets from the OS keyring
++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.3

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Allows you to access data stored in the OS provided keyring/keychain.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this lookup.

- keyring (python library)




Examples
--------

.. code-block:: yaml+jinja

    
    - name : output secrets to screen (BAD IDEA)
      debug:
        msg: "Password: {{item}}"
      with_keyring:
        - 'servicename username'

    - name: access mysql with password from keyring
      mysql_db: login_password={{lookup('keyring','mysql joe')}} login_user=joe




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
                                            <div>secrets stored</div>
                                        <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- Samuel Boucher <boucher.samuel.c@gmail.com>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/keyring.py>`_ to improve it.
