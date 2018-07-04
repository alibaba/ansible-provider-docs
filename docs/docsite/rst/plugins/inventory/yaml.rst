:source: yaml.py


.. _yaml_inventory:


yaml - Uses a specific YAML file as an inventory source.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- YAML based inventory, starts with the 'all' group and has hosts/vars/children entries.
- Host entries can have sub-entries defined, which will be treated as variables.
- Vars entries are normal group vars.
- Children are 'child groups', which can also have their own vars/hosts/children and so on.
- File MUST have a valid extension, defined in configuration




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
                    <b>yaml_extensions</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[u&#39;.yaml&#39;, u&#39;.yml&#39;, u&#39;.json&#39;]</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[defaults ]<br>yaml_valid_extensions = [u'.yaml', u'.yml', u'.json']</p>
                                                                    <p>[inventory_plugin_yaml ]<br>yaml_valid_extensions = [u'.yaml', u'.yml', u'.json']</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_YAML_FILENAME_EXT</div>
                                                            <div>env:ANSIBLE_INVENTORY_PLUGIN_EXTS</div>
                                                                                                </td>
                                                <td>
                                                                        <div>list of 'valid' extensions for files containing YAML</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - It takes the place of the previously hardcoded YAML inventory.
    - To function it requires being whitelisted in configuration.


Examples
--------

.. code-block:: yaml+jinja

    
    all: # keys must be unique, i.e. only one 'hosts' per group
        hosts:
            test1:
            test2:
                var1: value1
        vars:
            group_var1: value2
        children:   # key order does not matter, indentation does
            other_group:
                children:
                    group_x:
                        hosts:
                            test5
                vars:
                    g2_var2: value3
                hosts:
                    test4:
                        ansible_host: 127.0.0.1
            last_group:
                hosts:
                    test1 # same host as above, additional group membership
                vars:
                    last_var: MYVALUE





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/inventory/yaml.py>`_ to improve it.
