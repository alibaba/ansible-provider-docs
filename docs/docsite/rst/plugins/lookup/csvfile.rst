:source: csvfile.py


.. _csvfile_lookup:


csvfile - read data from a TSV or CSV file
++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.5

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- The csvfile lookup reads the contents of a file in CSV (comma-separated value) format. The lookup looks for the row where the first column matches keyname, and returns the value in the second column, unless a different column is specified.




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
                    <b>col</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">1</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>column to return (0 index).</div>
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
                                                                        <div>what to return if the value is not found in the file.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>delimiter</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">TAB</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>field separator in the file, for a tab you can specify &quot;TAB&quot; or &quot;t&quot;.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>encoding</b>
                                                            <br/><div style="font-size: small; color: darkgreen">(added in 2.1)</div>                </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">utf-8</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Encoding (character set) of the used CSV file.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>file</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">ansible.csv</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>name of the CSV/TSV file to open.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - The default is for TSV files (tab delimited) not CSV (comma delimited) ... yes the name is misleading.


Examples
--------

.. code-block:: yaml+jinja

    
    - name:  Match 'Li' on the first column, return the second column (0 based index)
      debug: msg="The atomic number of Lithium is {{ lookup('csvfile', 'Li file=elements.csv delimiter=,') }}"

    - name: msg="Match 'Li' on the first column, but return the 3rd column (columns start counting after the match)"
      debug: msg="The atomic mass of Lithium is {{ lookup('csvfile', 'Li file=elements.csv delimiter=, col=2') }}"




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
                                                                        <div>value(s) stored in file column</div>
                                                                <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- Jan-Piet Mens (@jpmens) <jpmens(at)gmail.com>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/csvfile.py>`_ to improve it.
