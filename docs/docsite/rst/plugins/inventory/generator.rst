:source: generator.py


.. _generator_inventory:


generator - Uses Jinja2 to construct hosts and groups from patterns
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.6

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Uses a YAML configuration file with a valid YAML or ``.config`` extension to define var expressions and group conditionals
- Create a template pattern that describes each host, and then use independent configuration layers
- Every element of every layer is combined to create a host for every layer combination
- Parent groups can be defined with reference to hosts and other groups using the same template variables




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
                    <b>hosts</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>The <code>name</code> key is a template used to generate hostnames based on the <code>layers</code> option. Each variable in the name is expanded to create a cartesian product of all possible layer combinations.</div>
                                                    <div>The <code>parents</code> are a list of parent groups that the host belongs to. Each <code>parent</code> item contains a <code>name</code> key, again expanded from the template, and an optional <code>parents</code> key that lists its parents.</div>
                                                    <div>Parents can also contain <code>vars</code>, which is a dictionary of vars that is then always set for that variable. This can provide easy access to the group name. E.g set an <code>application</code> variable that is set to the value of the <code>application</code> layer name.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>layers</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>A dictionary of layers, with the key being the layer name, used as a variable name in the <code>host</code> <code>name</code> and <code>parents</code> keys. Each layer value is a list of possible values for that layer.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
        # inventory.config file in YAML format
        plugin: generator
        strict: False
        hosts:
            name: "{{ operation }}-{{ application }}-{{ environment }}-runner"
            parents:
              - name: "{{ operation }}-{{ application }}-{{ environment }}"
                parents:
                  - name: "{{ operation }}-{{ application }}"
                    parents:
                      - name: "{{ operation }}"
                      - name: "{{ application }}"
                  - name: "{{ application }}-{{ environment }}"
                    parents:
                      - name: "{{ application }}"
                        vars:
                          application: "{{ application }}"
                      - name: "{{ environment }}"
                        vars:
                          environment: "{{ environment }}"
              - name: runner
        layers:
            operation:
                - build
                - launch
            environment:
                - dev
                - test
                - prod
            application:
                - web
                - api





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/inventory/generator.py>`_ to improve it.
