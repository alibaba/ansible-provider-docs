:source: list.py


.. _list_lookup:


list - simply returns what it is given.
+++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- this is mostly a noop, to be used as a with_list loop when you dont want the content transformed in any way.






Examples
--------

.. code-block:: yaml+jinja

    
    - name: unlike with_items you will get 3 items from this loop, the 2nd one being a list
      debug: var=item
      with_list:
        - 1
        - [2,3]
        - 4




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
                    <b>_list</b>
                    <br/><div style="font-size: small; color: red"></div>
                                    </td>
                <td></td>
                <td>
                                            <div>basically the same as you fed in</div>
                                        <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- Ansible core team


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/list.py>`_ to improve it.
