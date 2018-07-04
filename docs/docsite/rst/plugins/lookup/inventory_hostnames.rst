:source: inventory_hostnames.py


.. _inventory_hostnames_lookup:


inventory_hostnames - list of inventory hosts matching a host pattern
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.3

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This lookup understands 'host patterns' as used by the `hosts:` keyword in plays and can return a list of matching hosts from inventory





Notes
-----

.. note::
    - this is only worth for 'hostname patterns' it is easier to loop over the group/group_names variables otherwise.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: show all the hosts matching the pattern, i.e. all but the group www
      debug:
        msg: "{{ item }}"
      with_inventory_hostnames:
        - all:!www




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
                    <b>_hostnames</b>
                    <br/><div style="font-size: small; color: red">list</div>
                                    </td>
                <td></td>
                <td>
                                            <div>list of hostnames that matched the host pattern in inventory</div>
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
- Steven Dossett <sdossett@panath.com>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/inventory_hostnames.py>`_ to improve it.
