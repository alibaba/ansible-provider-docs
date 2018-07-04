:source: indexed_items.py


.. _indexed_items_lookup:


indexed_items - rewrites lists to return 'indexed items'
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.3

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- use this lookup if you want to loop over an array and also get the numeric index of where you are in the array as you go
- any list given will be transformed with each resulting element having the it's previous position in item.0 and its value in item.1




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



Examples
--------

.. code-block:: yaml+jinja

    
    - name: indexed loop demo
      debug:
        msg: "at array position {{ item.0 }} there is a value {{ item.1 }}"
      with_indexed_items:
        - "{{ some_list }}"




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
                                                                        <div>list with each item.0 giving you the position and item.1 the value</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/indexed_items.py>`_ to improve it.
