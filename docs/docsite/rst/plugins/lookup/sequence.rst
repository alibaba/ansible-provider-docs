:source: sequence.py


.. _sequence_lookup:


sequence - generate a list based on a number sequence
+++++++++++++++++++++++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- generates a sequence of items. You can specify a start value, an end value, an optional "stride" value that specifies the number of steps to increment the sequence, and an optional printf-style format string.
- Arguments can be specified as key=value pair strings or as a shortcut form of the arguments string is also accepted: [start-]end[/stride][:format].
- Numerical values can be specified in decimal, hexadecimal (0x3f8) or octal (0600).
- Starting at version 1.9.2, negative strides are allowed.




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
                    <b>count</b>
                    <br/><div style="font-size: small; color: red">number</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">0</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>number of elements in the sequence, this is not to be used with end</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>end</b>
                    <br/><div style="font-size: small; color: red">number</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">0</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>number at which to end the sequence, dont use this with count</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>format</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>return a string with the generated number formatted in</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>start</b>
                    <br/><div style="font-size: small; color: red">number</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">0</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>number at which to start the sequence</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>stride</b>
                    <br/><div style="font-size: small; color: red">number</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>increments between sequence numbers, the default is 1 unless the end is less than the start, then it is -1.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    - name: create some test users
      user:
        name: "{{ item }}"
        state: present
        groups: "evens"
      with_sequence: start=0 end=32 format=testuser%02x

    - name: create a series of directories with even numbers for some reason
      file:
        dest: "/var/stuff/{{ item }}"
        state: directory
      with_sequence: start=4 end=16 stride=2

    - name: a simpler way to use the sequence plugin create 4 groups
      group:
        name: "group{{ item }}"
        state: present
      with_sequence: count=4

    - name: the final countdown
      debug: msg={{item}} seconds to detonation
      with_sequence: end=0 start=10




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
                    <b>_list</b>
                    <br/><div style="font-size: small; color: red"></div>
                                    </td>
                <td></td>
                <td>
                                            <div>generated sequence of numbers or strings</div>
                                        <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- Jayson Vantuyl <jayson@aggressive.ly>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/sequence.py>`_ to improve it.
