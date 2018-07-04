:source: sumologic.py


.. _sumologic_callback:


sumologic - Sends task result events to Sumologic
+++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.6

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This callback plugin will send task results as JSON formatted events to a Sumologic HTTP collector source



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this callback.

- Whitelisting this callback plugin
- Create a HTTP collector source in Sumologic and specify a custom timestamp format of ``yyyy-MM-dd HH:mm:ss ZZZZ`` and a custom timestamp locator of ``"timestamp": "(.*``")


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
                    <b>url</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[callback_sumologic ]<br>url = VALUE</p>
                                                            </div>
                                                                                                            <div>env:SUMOLOGIC_URL</div>
                                                                                                </td>
                                                <td>
                                                                        <div>URL to the Sumologic HTTP collector source</div>
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
        callback_whitelist = sumologic

      Set the environment variable
        export SUMOLOGIC_URL=https://endpoint1.collection.us2.sumologic.com/receiver/v1/http/R8moSv1d8EW9LAUFZJ6dbxCFxwLH6kfCdcBfddlfxCbLuL-BN5twcTpMk__pYy_cDmp==

      Set the ansible.cfg variable in the callback_sumologic block
        [callback_sumologic]
        url = https://endpoint1.collection.us2.sumologic.com/receiver/v1/http/R8moSv1d8EW9LAUFZJ6dbxCFxwLH6kfCdcBfddlfxCbLuL-BN5twcTpMk__pYy_cDmp==





Status
------




Author
~~~~~~

- Ryan Currah (@ryancurrah)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/callback/sumologic.py>`_ to improve it.
