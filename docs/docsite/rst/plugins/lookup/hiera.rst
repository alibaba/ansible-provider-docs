:source: hiera.py


.. _hiera_lookup:


hiera - get info from hiera data
++++++++++++++++++++++++++++++++

.. versionadded:: 2.4

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Retrieves data from an Puppetmaster node using Hiera as ENC



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this lookup.

- hiera (command line utility)


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
                    <b>_bin_file</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">/usr/bin/hiera</div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:ANSIBLE_HIERA_BIN</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Binary file to execute Hiera</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>_hiera_key</b>
                    <br/><div style="font-size: small; color: red">list</div>                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>The list of keys to lookup on the Puppetmaster</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>_hierarchy_file</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">/etc/hiera.yaml</div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:ANSIBLE_HIERA_CFG</div>
                                                                                                </td>
                                                <td>
                                                                        <div>File that describes the hierarchy of Hiera</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    # All this examples depends on hiera.yml that describes the hierarchy

    - name: "a value from Hiera 'DB'"
      debug: msg={{ lookup('hiera', 'foo') }}

    - name: "a value from a Hiera 'DB' on other environment"
      debug: msg={{ lookup('hiera', 'foo environment=production') }}

    - name: "a value from a Hiera 'DB' for a concrete node"
      debug: msg={{ lookup('hiera', 'foo fqdn=puppet01.localdomain') }}




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
                    <br/><div style="font-size: small; color: red">strings</div>
                                    </td>
                <td></td>
                <td>
                                                                        <div>a value associated with input key</div>
                                                                <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- Juan Manuel Parrilla (@jparrill)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/hiera.py>`_ to improve it.
