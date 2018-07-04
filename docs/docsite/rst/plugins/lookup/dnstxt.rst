:source: dnstxt.py


.. _dnstxt_lookup:


dnstxt - query a domain(s)'s DNS txt fields
+++++++++++++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Uses a python library to return the DNS TXT record for a domain.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this lookup.

- dns/dns.resolver (python library)


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
                                                                        <div>domain or list of domains to query TXT records from</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    - name: show txt entry
      debug: msg="{{lookup('dnstxt', ['test.example.com'])}}"

    - name: iterate over txt entries
      debug: msg="{{item}}"
      with_dnstxt:
        - 'test.example.com'
        - 'other.example.com'
        - 'last.example.com'

    - name: iterate of a comma delimited DNS TXT entry
      debug: msg="{{item}}"
      with_dnstxt: "{{lookup('dnstxt', ['test.example.com']).split(',')}}"




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
                <td></td>
                <td>
                                                                        <div>values returned by the DNS TXT record.</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/dnstxt.py>`_ to improve it.
