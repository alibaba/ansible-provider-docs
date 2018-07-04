:source: dict.py


.. _dict_lookup:


dict - returns key/value pair items from dictionaries
+++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.5

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Takes dictionaries as input and returns a list with each item in the list being a dictionary with 'key' and 'value' as keys to the previous dictionary's structure.




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
                                                                        <div>A list of dictionaries</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    vars:
      users:
        alice:
          name: Alice Appleworth
          telephone: 123-456-7890
        bob:
          name: Bob Bananarama
          telephone: 987-654-3210
    tasks:
      # with predefined vars
      - name: Print phone records
        debug:
          msg: "User {{ item.key }} is {{ item.value.name }} ({{ item.value.telephone }})"
        loop: "{{ lookup('dict', users) }}"
      # with inline dictionary
      - name: show dictionary
        debug:
          msg: "{{item.key}}: {{item.value}}"
        with_dict: {a: 1, b: 2, c: 3}




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
                    <br/><div style="font-size: small; color: red">list</div>
                                    </td>
                <td></td>
                <td>
                                                                        <div>list of composed dictonaries with key and value</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/dict.py>`_ to improve it.
