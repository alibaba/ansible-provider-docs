:source: flattened.py


.. _flattened_lookup:


flattened - return single list completely flattened
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.3

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- given one or more lists, this lookup will flatten any list elements found recursively until only 1 list is left.




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
                                                                        <div>lists to flatten</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - unlike 'items' which only flattens 1 level, this plugin will continue to flatten until it cannot find lists anymore.
    - aka highlander plugin, there can only be one (list).


Examples
--------

.. code-block:: yaml+jinja

    
    - name: "'unnest' all elements into single list"
      debug: msg="all in one list {{lookup('flattened', [1,2,3,[5,6]], [a,b,c], [[5,6,1,3], [34,a,b,c]])}}"




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
                                                                        <div>flattened list</div>
                                                                <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- Serge van Ginderachter <serge@vanginderachter.be>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/flattened.py>`_ to improve it.
