:source: onepassword_raw.py


.. _onepassword_raw_lookup:


onepassword_raw - fetch raw json data from 1Password
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.6

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- onepassword_raw wraps ``op`` command line utility to fetch an entire item from 1Password



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this lookup.

- ``op`` 1Password command line utility. See https://support.1password.com/command-line/
- must have already logged into 1Password using op CLI


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
                                                                        <div>identifier(s) (UUID, name, or domain; case-insensitive) of item(s) to retrieve</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>vault</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">None</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>vault containing the item to retrieve (case-insensitive); if absent will search all vaults</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    - name: "retrieve all data about Wintermute"
      debug:
        msg: "{{ lookup('onepassword_raw', 'Wintermute') }}"




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
                                            <div>field data requested</div>
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

- Scott Buchanan <sbuchanan@ri.pn>
- Andrew Zenk <azenk@umn.edu>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/onepassword_raw.py>`_ to improve it.
