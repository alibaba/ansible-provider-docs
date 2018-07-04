:source: random_choice.py


.. _random_choice_lookup:


random_choice - return random element from list
+++++++++++++++++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- The 'random_choice' feature can be used to pick something at random. While it's not a load balancer (there are modules for those), it can somewhat be used as a poor man's load balancer in a MacGyver like situation.
- At a more basic level, they can be used to add chaos and excitement to otherwise predictable automation environments.






Examples
--------

.. code-block:: yaml+jinja

    
    - name: Magic 8 ball for MUDs
      debug:
        msg: "{{ item }}"
      with_random_choice:
         - "go through the door"
         - "drink from the goblet"
         - "press the red button"
         - "do nothing"




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
                                                                        <div>random item</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/random_choice.py>`_ to improve it.
