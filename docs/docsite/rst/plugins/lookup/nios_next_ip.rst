:source: nios_next_ip.py


.. _nios_next_ip_lookup:


nios_next_ip - Return the next available IP address for a network
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Uses the Infoblox WAPI API to return the next available IP addresses for a given network CIDR



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
                                                                        <div>The CIDR network to retrieve the next addresses from</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>num</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">1</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>The number of IP addresses to return</div>
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
                    
                                        </table>
    <br/>


Notes
-----

.. note::
    - This module must be run locally, which can be achieved by specifying ``connection: local``.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: return next available IP address for network 192.168.10.0/24
      set_fact:
        ipaddr: "{{ lookup('nios_next_ip', '192.168.10.0/24', provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"

    - name: return the next 3 available IP addresses for network 192.168.10.0/24
      set_fact:
        ipaddr: "{{ lookup('nios_next_ip', '192.168.10.0/24', num=3, provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"




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
                    <br/><div style="font-size: small; color: red">list</div>
                                    </td>
                <td>always</td>
                <td>
                                                                        <div>The list of next IP addresses available</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/nios_next_ip.py>`_ to improve it.
