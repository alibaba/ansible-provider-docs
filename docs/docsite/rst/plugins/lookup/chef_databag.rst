:source: chef_databag.py


.. _chef_databag_lookup:


chef_databag - fetches data from a Chef Databag
+++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.3

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This is a lookup plugin to provide access to chef data bags using the pychef package. It interfaces with the chef server api using the same methods to find a knife or chef-client config file to load parameters from, starting from either the given base path or the current working directory. The lookup order mirrors the one from Chef, all folders in the base path are walked back looking for the following configuration file in order : .chef/knife.rb, ~/.chef/knife.rb, /etc/chef/client.rb



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this lookup.

- pychef (python library https://pychef.readthedocs.io `pip install pychef`


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
                    <b>item</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Item to fetch</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>name</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Name of the databag</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
        - debug:
            msg: "{{ lookup('chef_databag', 'name=data_bag_name item=data_bag_item') }}"




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
                                                                        <div>The value from the databag</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/chef_databag.py>`_ to improve it.
