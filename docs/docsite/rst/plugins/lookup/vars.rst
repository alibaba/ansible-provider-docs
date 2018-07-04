:source: vars.py


.. _vars_lookup:


vars - Lookup templated value of variables
++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Retrieves the value of an Ansible variable.




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
                                                                        <div>The variable names to look up.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>default</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>What to return if a variable is undefined.</div>
                                                    <div>If no default is set, it will result in an error if any of the variables is undefined.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    - name: Show value of 'variablename'
      debug: msg="{{ lookup('vars', 'variabl' + myvar)}}"
      vars:
        variablename: hello
        myvar: ename

    - name: Show default empty since i dont have 'variablnotename'
      debug: msg="{{ lookup('vars', 'variabl' + myvar, default='')}}"
      vars:
        variablename: hello
        myvar: notename

    - name: Produce an error since i dont have 'variablnotename'
      debug: msg="{{ lookup('vars', 'variabl' + myvar)}}"
      ignore_errors: True
      vars:
        variablename: hello
        myvar: notename

    - name: find several related variables
      debug: msg="{{ lookup('vars', 'ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all') }}"

    - name: alternate way to find some 'prefixed vars' in loop
      debug: msg="{{ lookup('vars', 'ansible_play_' + item) }}"
      loop:
        - hosts
        - batch
        - hosts_all




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
                    <b>_value</b>
                    <br/><div style="font-size: small; color: red"></div>
                                    </td>
                <td></td>
                <td>
                                                                        <div>value of the variables requested.</div>
                                                                <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- Ansible Core


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/vars.py>`_ to improve it.
