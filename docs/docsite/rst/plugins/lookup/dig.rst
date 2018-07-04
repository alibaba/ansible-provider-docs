:source: dig.py


.. _dig_lookup:


dig - query DNS using the dnspython library
+++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.9

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- The dig lookup runs queries against DNS servers to retrieve DNS records for a specific name (FQDN - fully qualified domain name). It is possible to lookup any DNS record in this manner.
- There is a couple of different syntaxes that can be used to specify what record should be retrieved, and for which name. It is also possible to explicitly specify the DNS server(s) to use for lookups.
- In its simplest form, the dig lookup plugin can be used to retrieve an IPv4 address (DNS A record) associated with FQDN
- In addition to (default) A record, it is also possible to specify a different record type that should be queried. This can be done by either passing-in additional parameter of format qtype=TYPE to the dig lookup, or by appending /TYPE to the FQDN being queried.
- If multiple values are associated with the requested record, the results will be returned as a comma-separated list. In such cases you may want to pass option wantlist=True to the plugin, which will result in the record values being returned as a list over which you can iterate later on.
- By default, the lookup will rely on system-wide configured DNS servers for performing the query. It is also possible to explicitly specify DNS servers to query using the @DNS_SERVER_1,DNS_SERVER_2,...,DNS_SERVER_N notation. This needs to be passed-in as an additional parameter to the lookup



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this lookup.

- dnspython (python library, http://www.dnspython.org/)


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
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>domain(s) to query</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>flat</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">1</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>If 0 each record is returned as a dictionary, otherwise a string</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>qtype</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>A</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>ALL</li>
                                                                                                                                                                                                <li>AAAA</li>
                                                                                                                                                                                                <li>CNAME</li>
                                                                                                                                                                                                <li>DNAME</li>
                                                                                                                                                                                                <li>DLV</li>
                                                                                                                                                                                                <li>DNSKEY</li>
                                                                                                                                                                                                <li>DS</li>
                                                                                                                                                                                                <li>HINFO</li>
                                                                                                                                                                                                <li>LOC</li>
                                                                                                                                                                                                <li>MX</li>
                                                                                                                                                                                                <li>NAPTR</li>
                                                                                                                                                                                                <li>NS</li>
                                                                                                                                                                                                <li>NSEC3PARAM</li>
                                                                                                                                                                                                <li>PTR</li>
                                                                                                                                                                                                <li>RP</li>
                                                                                                                                                                                                <li>RRSIG</li>
                                                                                                                                                                                                <li>SOA</li>
                                                                                                                                                                                                <li>SPF</li>
                                                                                                                                                                                                <li>SRV</li>
                                                                                                                                                                                                <li>SSHFP</li>
                                                                                                                                                                                                <li>TLSA</li>
                                                                                                                                                                                                <li>TXT</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>record type to query</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - ALL is not a record per-se, merely the listed fields are available for any record results you retrieve in the form of a dictionary.
    - While the 'dig' lookup plugin supports anything which dnspython supports out of the box, only a subset can be converted into a dictionary.
    - If you need to obtain the AAAA record (IPv6 address), you must specify the record type explicitly. Syntax for specifying the record type is shown in the examples below.
    - The trailing dot in most of the examples listed is purely optional, but is specified for completeness/correctness sake.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Simple A record (IPV4 address) lookup for example.com
      debug: msg="{{ lookup('dig', 'example.com.')}}"

    - name: "The TXT record for example.org."
      debug: msg="{{ lookup('dig', 'example.org.', 'qtype=TXT') }}"

    - name: "The TXT record for example.org, alternative syntax."
      debug: msg="{{ lookup('dig', 'example.org./TXT') }}"

    - name: use in a loop
      debug: msg="MX record for gmail.com {{ item }}"
      with_items: "{{ lookup('dig', 'gmail.com./MX', wantlist=True) }}"

    - debug: msg="Reverse DNS for 192.0.2.5 is {{ lookup('dig', '192.0.2.5/PTR') }}"
    - debug: msg="Reverse DNS for 192.0.2.5 is {{ lookup('dig', '5.2.0.192.in-addr.arpa./PTR') }}"
    - debug: msg="Reverse DNS for 192.0.2.5 is {{ lookup('dig', '5.2.0.192.in-addr.arpa.', 'qtype=PTR') }}"
    - debug: msg="Querying 198.51.100.23 for IPv4 address for example.com. produces {{ lookup('dig', 'example.com', '@198.51.100.23') }}"

    - debug: msg="XMPP service for gmail.com. is available at {{ item.target }} on port {{ item.port }}"
      with_items: "{{ lookup('dig', '_xmpp-server._tcp.gmail.com./SRV', 'flat=0', wantlist=True) }}"




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
                                                                        <div>list of composed strings or dictonaries with key and value If a dictionary, fields shows the keys returned depending on query type</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/dig.py>`_ to improve it.
