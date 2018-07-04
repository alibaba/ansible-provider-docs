:source: ini.py


.. _ini_lookup:


ini - read data from a ini file
+++++++++++++++++++++++++++++++

.. versionadded:: 2.0

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- The ini lookup reads the contents of a file in INI format ``key1=value1``. This plugin retrieve the value on the right side after the equal sign ``'='`` of a given section ``[section]``.
- You can also read a property file which - in this case - does not contain section.




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
                                                                        <div>The key(s) to look up</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>default</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue"></div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>return value if the key is not in the ini file</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>encoding</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">utf-8</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Text encoding to use.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>file</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">ansible.ini</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Name of the file to load</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>re</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Flag to indicate if the key supplied is a regexp.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>section</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">global</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>section where to lookup for key.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>type</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>ini</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>properties</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>ini Type of the file. 'properties' refers to the Java properties files.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    - debug: msg="User in integration is {{ lookup('ini', 'user section=integration file=users.ini') }}"

    - debug: msg="User in production  is {{ lookup('ini', 'user section=production  file=users.ini') }}"

    - debug: msg="user.name is {{ lookup('ini', 'user.name type=properties file=user.properties') }}"

    - debug:
        msg: "{{ item }}"
      with_ini:
        - value[1-2]
        - section: section1
        - file: "lookup.ini"
        - re: true




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
                                                                        <div>value(s) of the key(s) in the ini file</div>
                                                                <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- Yannig Perre <yannig.perre(at)gmail.com>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/ini.py>`_ to improve it.
