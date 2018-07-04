:source: password.py


.. _password_lookup:


password - retrieve or generate a random password, stored in a file
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Generates a random plaintext password and stores it in a file at a given filepath.
- If the file exists previously, it will retrieve its contents, behaving just like with_file.
- Usage of variables like ``"{{ inventory_hostname }}"`` in the filepath can be used to set up random passwords per host, which simplifies password management in ``"host_vars"`` variables.
- A special case is using /dev/null as a path. The password lookup will generate a new random password each time, but will not write it to /dev/null. This can be used when you need a password without storing it on the controller.




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
                                                                        <div>path to the file that stores/will store the passwords</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>chars</b>
                    <br/><div style="font-size: small; color: red">string</div>                                        <br/><div style="font-size: small; color: darkgreen">(added in 1.4)</div>                </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Define comma separated list of names that compose a custom character set in the generated passwords.</div>
                                                    <div>By default generated passwords contain a random mix of upper and lowercase ASCII letters, the numbers 0-9 and punctuation (&quot;. , : - _&quot;).</div>
                                                    <div>They can be either parts of Python's string module attributes (ascii_letters,digits, etc) or are used literally ( :, -).</div>
                                                    <div>To enter comma use two commas ',,' somewhere - preferably at the end. Quotes and double quotes are not supported.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>encrypt</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Whether the user requests that this password is returned encrypted or in plain text.</div>
                                                    <div>Note that the password is always stored as plain text.</div>
                                                    <div>Encrypt also forces saving the salt value for idempotence.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>length</b>
                    <br/><div style="font-size: small; color: red">integer</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">20</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>The length of the generated password.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - A great alternative to the password lookup plugin, if you don't need to generate random passwords on a per-host basis, would be to use Vault in playbooks. Read the documentation there and consider using it first, it will be more desirable for most applications.
    - If the file already exists, no data will be written to it. If the file has contents, those contents will be read in as the password. Empty files cause the password to return as an empty string.
    - As all lookups, this runs on the Ansible host as the user running the playbook, and "become" does not apply, the target file must be readable by the playbook user, or, if it does not exist, the playbook user must have sufficient privileges to create it. (So, for example, attempts to write into areas such as /etc will fail unless the entire playbook is being run as root).


Examples
--------

.. code-block:: yaml+jinja

    
    - name: create a mysql user with a random password
      mysql_user:
        name: "{{ client }}"
        password: "{{ lookup('password', 'credentials/' + client + '/' + tier + '/' + role + '/mysqlpassword length=15') }}"
        priv: "{{ client }}_{{ tier }}_{{ role }}.*:ALL"

    - name: create a mysql user with a random password using only ascii letters
      mysql_user: name={{ client }} password="{{ lookup('password', '/tmp/passwordfile chars=ascii_letters') }}" priv='{{ client }}_{{ tier }}_{{ role }}.*:ALL'

    - name: create a mysql user with a random password using only digits
      mysql_user:
        name: "{{ client }}"
        password: "{{ lookup('password', '/tmp/passwordfile chars=digits') }}"
        priv: "{{ client }}_{{ tier }}_{{ role }}.*:ALL"

    - name: create a mysql user with a random password using many different char sets
      mysql_user:
        name: "{{ client }}"
        password: "{{ lookup('password', '/tmp/passwordfile chars=ascii_letters,digits,hexdigits,punctuation') }}"
        priv: "{{ client }}_{{ tier }}_{{ role }}.*:ALL"




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
                                                                        <div>a password</div>
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
- Javier Candeira <javier@candeira.com>
- Maykel Moya <mmoya@speedyrails.com>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/password.py>`_ to improve it.
