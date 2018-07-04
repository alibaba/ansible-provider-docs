:source: pipe.py


.. _pipe_lookup:


pipe - read output from a command
+++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Run a command and return the output




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
                                                                        <div>command(s) to run</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - Like all lookups this runs on the Ansible controller and is unaffected by other keywords, such as become, so if you need to different permissions you must change the command or run Ansible as another user.
    - Alternatively you can use a shell/command task that runs against localhost and registers the result.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: raw result of running date command"
      debug: msg="{{ lookup('pipe','date') }}"

    - name: Always use quote filter to make sure your variables are safe to use with shell
      debug: msg="{{ lookup('pipe','getent ' + myuser|quote ) }}"




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
                    <b>_string</b>
                    <br/><div style="font-size: small; color: red"></div>
                                    </td>
                <td></td>
                <td>
                                                                        <div>stdout from command</div>
                                                                <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- Daniel Hokka Zakrisson <daniel@hozac.com>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/pipe.py>`_ to improve it.
