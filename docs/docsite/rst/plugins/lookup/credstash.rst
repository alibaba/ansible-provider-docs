:source: credstash.py


.. _credstash_lookup:


credstash - retrieve secrets from Credstash on AWS
++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Credstash is a small utility for managing secrets using AWS's KMS and DynamoDB: https://github.com/fugue/credstash



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this lookup.

- credstash (python library)


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
                    <br/><div style="font-size: small; color: red">list</div>                    <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>term or list of terms to lookup in the credit store</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>aws_access_key_id</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                            <div>env:AWS_ACCESS_KEY_ID</div>
                                                                                                </td>
                                                <td>
                                                                        <div>AWS access key ID</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>aws_secret_access_key</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                            <div>env:AWS_SECRET_ACCESS_KEY</div>
                                                                                                </td>
                                                <td>
                                                                        <div>AWS access key</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>aws_session_token</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                            <div>env:AWS_SESSION_TOKEN</div>
                                                                                                </td>
                                                <td>
                                                                        <div>AWS session token</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>profile_name</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                            <div>env:AWS_PROFILE</div>
                                                                                                </td>
                                                <td>
                                                                        <div>AWS profile to use for authentication</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>region</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>AWS region</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>table</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">credential-store</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>name of the credstash table to query</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>version</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Credstash version</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    - name: first use credstash to store your secrets
      shell: credstash put my-github-password secure123

    - name: "Test credstash lookup plugin -- get my github password"
      debug: msg="Credstash lookup! {{ lookup('credstash', 'my-github-password') }}"

    - name: "Test credstash lookup plugin -- get my other password from us-west-1"
      debug: msg="Credstash lookup! {{ lookup('credstash', 'my-other-password', region='us-west-1') }}"

    - name: "Test credstash lookup plugin -- get the company's github password"
      debug: msg="Credstash lookup! {{ lookup('credstash', 'company-github-password', table='company-passwords') }}"

    - name: Example play using the 'context' feature
      hosts: localhost
      vars:
        context:
          app: my_app
          environment: production
      tasks:

      - name: "Test credstash lookup plugin -- get the password with a context passed as a variable"
        debug: msg="{{ lookup('credstash', 'some-password', context=context) }}"

      - name: "Test credstash lookup plugin -- get the password with a context defined here"
        debug: msg="{{ lookup('credstash', 'some-password', context=dict(app='my_app', environment='production')) }}"




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
                                                                        <div>value(s) stored in Credstash</div>
                                                                <br/>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/credstash.py>`_ to improve it.
