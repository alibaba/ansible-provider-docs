:source: nios.py


.. _nios_lookup:


nios - Query Infoblox NIOS objects
++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Uses the Infoblox WAPI API to fetch NIOS specified objects.  This lookup supports adding additional keywords to filter the return data and specify the desired set of returned fields.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this lookup.

- infoblox_client


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                            <th>Configuration</th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
                    <b>_terms</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>The name of the object to return from NIOS</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>extattrs</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>a dict object that is used to filter on extattrs</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>filter</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>a dict object that is used to filter the return objects</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>provider</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>A dict object containing connection details.</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>username</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Configures the username to use to authenticate the connection to the remote instance of NIOS.</div>
                                                    <div>Value can also be specified using <code>INFOBLOX_USERNAME</code> environment variable.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>http_request_timeout</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">10</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>The amount of time before to wait before receiving a response</div>
                                                    <div>Value can also be specified using <code>INFOBLOX_HTTP_REQUEST_TIMEOUT</code> environment variable.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>max_retries</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">3</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Configures the number of attempted retries before the connection is declared usable</div>
                                                    <div>Value can also be specified using <code>INFOBLOX_MAX_RETRIES</code> environment variable.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>wapi_version</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">1.4</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Specifies the version of WAPI to use</div>
                                                    <div>Value can also be specified using <code>INFOBLOX_WAP_VERSION</code> environment variable.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>ssl_verify</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Boolean value to enable or disable verifying SSL certificates</div>
                                                    <div>Value can also be specified using <code>INFOBLOX_SSL_VERIFY</code> environment variable.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>max_results</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">1000</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Specifies the maximum number of objects to be returned, if set to a negative number the appliance will return an error when the number of returned objects would exceed the setting.</div>
                                                    <div>Value can also be specified using <code>INFOBLOX_MAX_RESULTS</code> environment variable.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>host</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Specifies the DNS host name or address for connecting to the remote instance of NIOS WAPI over REST</div>
                                                    <div>Value can also be specified using <code>INFOBLOX_HOST</code> environment variable.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>password</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Specifies the password to use to authenticate the connection to the remote instance of NIOS.</div>
                                                    <div>Value can also be specified using <code>INFOBLOX_PASSWORD</code> environment variable.</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>return_fields</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>The list of field names to return for the specified object.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - This module must be run locally, which can be achieved by specifying ``connection: local``.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: fetch all networkview objects
      set_fact:
        networkviews: "{{ lookup('nios', 'networkview', provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"

    - name: fetch the default dns view
      set_fact:
        dns_views: "{{ lookup('nios', 'view', filter={'name': 'default'}, provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"

    # all of the examples below use credentials that are  set using env variables
    # export INFOBLOX_HOST=nios01
    # export INFOBLOX_USERNAME=admin
    # export INFOBLOX_PASSWORD=admin

    - name: fetch all host records and include extended attributes
      set_fact:
        host_records: "{{ lookup('nios', 'record:host', return_fields=['extattrs', 'name', 'view', 'comment']}) }}"


    - name: use env variables to pass credentials
      set_fact:
        networkviews: "{{ lookup('nios', 'networkview') }}"

    - name: get a host record
      set_fact:
        host: "{{ lookup('nios', 'record:host', filter={'name': 'hostname.ansible.com'}) }}"

    - name: get the authoritative zone from a non default dns view
      set_fact:
        host: "{{ lookup('nios', 'zone_auth', filter={'fqdn': 'ansible.com', 'view': 'ansible-dns'}) }}"




Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this lookup:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="2">
                    <b>obj_type</b>
                    <br/><div style="font-size: small; color: red">complex</div>
                                    </td>
                <td>always</td>
                <td>
                                                                        <div>The object type specified in the terms argument</div>
                                                                <br/>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>obj_field</b>
                    <br/><div style="font-size: small; color: red"></div>
                                    </td>
                <td></td>
                <td>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/nios.py>`_ to improve it.
