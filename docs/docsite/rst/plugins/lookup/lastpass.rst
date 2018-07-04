:source: lastpass.py


.. _lastpass_lookup:


lastpass - fetch data from lastpass
+++++++++++++++++++++++++++++++++++

.. versionadded:: 2.3

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- use the lpass command line utility to fetch specific fields from lastpass



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this lookup.

- lpass (command line utility)
- must have already logged into lastpass


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
                                                                        <div>key from which you want to retrieve the field</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>field</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">password</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>field to return from lastpass</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    - name: get 'custom_field' from lastpass entry 'entry-name'
      debug:
        msg: "{{ lookup('lastpass', 'entry-name', field='custom_field') }}"




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

- Andrew Zenk <azenk@umn.edu>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/lastpass.py>`_ to improve it.
