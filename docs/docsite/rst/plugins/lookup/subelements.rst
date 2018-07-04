:source: subelements.py


.. _subelements_lookup:


subelements - traverse nested key from a list of dictionaries
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.4

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Subelements walks a list of hashes (aka dictionaries) and then traverses a list with a given (nested sub-)key inside of those records.




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
                                                                        <div>tuple of list of dictionaries and dictionary key to extract</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>skip_missing</b>
                                                                            </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>If set to True, the lookup plugin will skip the lists items that do not contain the given subkey. If False, the plugin will yield an error and complain about the missing subkey.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    - name: show var structure as it is needed for example to make sense
      hosts: all
      vars:
        users:
          - name: alice
            authorized:
              - /tmp/alice/onekey.pub
              - /tmp/alice/twokey.pub
            mysql:
                password: mysql-password
                hosts:
                  - "%"
                  - "127.0.0.1"
                  - "::1"
                  - "localhost"
                privs:
                  - "*.*:SELECT"
                  - "DB1.*:ALL"
            groups:
              - wheel
          - name: bob
            authorized:
              - /tmp/bob/id_rsa.pub
            mysql:
                password: other-mysql-password
                hosts:
                  - "db1"
                privs:
                  - "*.*:SELECT"
                  - "DB2.*:ALL"
      tasks:
        - name: Set authorized ssh key, extracting just that data from 'users'
          authorized_key:
            user: "{{ item.0.name }}"
            key: "{{ lookup('file', item.1) }}"
          with_subelements:
             - "{{ users }}"
             - authorized

        - name: Setup MySQL users, given the mysql hosts and privs subkey lists
          mysql_user:
            name: "{{ item.0.name }}"
            password: "{{ item.0.mysql.password }}"
            host: "{{ item.1 }}"
            priv: "{{ item.0.mysql.privs | join('/') }}"
          with_subelements:
            - "{{ users }}"
            - mysql.hosts

        - name: list groups for user that have them, dont error if they don't
          debug: var=item
          with_list: "{{lookup('subelements', users, 'groups', 'skip_missing=True')}}"




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
                                            <div>list of subelements extracted</div>
                                        <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- Serge van Ginderachter <serge@vanginderachter.be>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/subelements.py>`_ to improve it.
