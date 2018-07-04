:source: items.py


.. _items_lookup:


items - list of items
+++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- this lookup returns a list of items given to it, if any of the top level items is also a list it will flatten it, but it will not recurse




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
                                                                        <div>list of items</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - this is the standard lookup used for loops in most examples
    - check out the 'flattened' lookup for recursive flattening
    - if you do not want flattening nor any other transformation look at the 'list' lookup.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: "loop through list"
      debug:
        msg: "An item: {{item}}"
      with_items:
        - 1
        - 2
        - 3

    - name: add several users
      user:
        name: "{{ item }}"
        groups: "wheel"
        state: present
      with_items:
         - testuser1
         - testuser2

    - name: "loop through list from a variable"
      debug:
        msg: "An item: {{item}}"
      with_items: "{{ somelist }}"

    - name: more complex items to add several users
      user:
        name: "{{ item.name }}"
        uid: "{{ item.uid }}"
        groups: "{{ item.groups }}"
        state: present
      with_items:
         - { name: testuser1, uid: 1002, groups: "wheel, staff" }
         - { name: testuser2, uid: 1003, groups: staff }





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
                    <br/><div style="font-size: small; color: red">list</div>
                                    </td>
                <td></td>
                <td>
                                                                        <div>once flattened list</div>
                                                                <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- Michael DeHaan <michael.dehaan@gmail.com>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/items.py>`_ to improve it.
