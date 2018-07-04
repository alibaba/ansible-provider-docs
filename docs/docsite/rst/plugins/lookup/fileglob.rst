:source: fileglob.py


.. _fileglob_lookup:


fileglob - list files matching a pattern
++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.4

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Matches all files in a single directory, non-recursively, that match a pattern. It calls Python's "glob" library.




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
                                                                        <div>path(s) of files to read</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - Patterns are only supported on files, not directory/paths.
    - Matching is against local system files.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: display content of all .txt files in dir
      debug: msg={{lookup('fileglob', '/my/path/*.txt')}}

    - name: Copy each file over that matches the given pattern
      copy:
        src: "{{ item }}"
        dest: "/etc/fooapp/"
        owner: "root"
        mode: 0600
      with_fileglob:
        - "/playbooks/files/fooapp/*"




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
                                                                        <div>content of file(s)</div>
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


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/fileglob.py>`_ to improve it.
