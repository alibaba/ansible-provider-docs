:source: scaleway.py


.. _scaleway_inventory:


scaleway - Scaleway inventory source
++++++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Get inventory hosts from Scaleway




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
                    <b>oauth_token</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                            <div>env:SCW_TOKEN</div>
                                                            <div>env:SCW_API_KEY</div>
                                                            <div>env:SCW_OAUTH_TOKEN</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Scaleway OAuth token.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>regions</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[u&#39;ams1&#39;, u&#39;par1&#39;]</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Filter results on a specific Scaleway region</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>tags</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Filter results on a specific tag</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    # scaleway_inventory.yml file in YAML format
    # Example command line: ansible-inventory --list -i scaleway_inventory.yml

    plugin: scaleway
    regions:
      - ams1
      - par1
    tags:
      - foobar





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/inventory/scaleway.py>`_ to improve it.
