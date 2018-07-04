:source: splunk.py


.. _splunk_callback:


splunk - Sends task result events to Splunk HTTP Event Collector
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.7

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This callback plugin will send task results as JSON formatted events to a Splunk HTTP collector.
- The companion Splunk Monitoring & Diagnostics App is available here "https://splunkbase.splunk.com/app/4023/"
- Credit to "Ryan Currah (@ryancurrah)" for original source upon which this is based.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this callback.

- Whitelisting this callback plugin
- Create a HTTP Event Collector in Splunk
- Define the url and token in ansible.cfg


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
                    <b>authtoken</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_splunk ]<br>authtoken = VALUE</p>
                                                            </div>
                                                                                                            <div>env:SPLUNK_AUTHTOKEN</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Token to authenticate the connection to the Splunk HTTP collector</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>url</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_splunk ]<br>url = VALUE</p>
                                                            </div>
                                                                                                            <div>env:SPLUNK_URL</div>
                                                                                                </td>
                                                <td>
                                                                        <div>URL to the Splunk HTTP collector source</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    examples: >
      To enable, add this to your ansible.cfg file in the defaults block
        [defaults]
        callback_whitelist = splunk
      Set the environment variable
        export SPLUNK_URL=http://mysplunkinstance.datapaas.io:8088/services/collector/event
        export SPLUNK_AUTHTOKEN=f23blad6-5965-4537-bf69-5b5a545blabla88
      Set the ansible.cfg variable in the callback_splunk block
        [callback_splunk]
        url = http://mysplunkinstance.datapaas.io:8088/services/collector/event
        authtoken = f23blad6-5965-4537-bf69-5b5a545blabla88





Status
------




Author
~~~~~~

- Stuart Hirst <support@convergingdata.com>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/callback/splunk.py>`_ to improve it.
