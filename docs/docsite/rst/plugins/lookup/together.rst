:source: together.py


.. _together_lookup:


together - merges lists into synchronized list
++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.3

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Creates a list with the iterated elements of the supplied lists
- To clarify with an example, [ 'a', 'b' ] and [ 1, 2 ] turn into [ ('a',1), ('b', 2) ]
- This is basically the same as the 'zip_longest' filter and Python function
- Any 'unbalanced' elements will be substituted with 'None'




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
                                                                        <div>list of lists to merge</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    - name: item.0 returns from the 'a' list, item.1 returns from the '1' list
      debug:
        msg: "{{ item.0 }} and {{ item.1 }}"
      with_together:
        - ['a', 'b', 'c', 'd']
        - [1, 2, 3, 4]




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
                                            <div>synchronized list</div>
                                        <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- Bradley Young <young.bradley@gmail.com>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/together.py>`_ to improve it.
