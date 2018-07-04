:source: mongodb.py


.. _mongodb_lookup:


mongodb - lookup info from MongoDB
++++++++++++++++++++++++++++++++++

.. versionadded:: 2.3

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- The ``MongoDB`` lookup runs the *find()* command on a given *collection* on a given *MongoDB* server.
- The result is a list of jsons, so slightly different from what PyMongo returns. In particular, *timestamps* are converted to epoch integers.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this lookup.

- pymongo >= 2.4 (python library)


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
                    <b>collection</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Name of the collection which the query will be made</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>connect_string</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">mongodb://localhost/</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Can be any valid MongoDB connection string, supporting authentication, replicasets, etc.</div>
                                                    <div>More info at <a href='https://docs.mongodb.org/manual/reference/connection-string/'>https://docs.mongodb.org/manual/reference/connection-string/</a></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>database</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Name of the database which the query will be made</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>filter</b>
                    <br/><div style="font-size: small; color: red">dict</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{}</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Criteria of the output</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>limit</b>
                    <br/><div style="font-size: small; color: red">integer</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>How many results should be shown</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>projection</b>
                    <br/><div style="font-size: small; color: red">dict</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{}</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Fields you want returned</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>skip</b>
                    <br/><div style="font-size: small; color: red">integer</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>How many results should be skipped</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sort</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[]</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Sorting rules. Please notice the constats are replaced by strings.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - Please check https://api.mongodb.org/python/current/api/pymongo/collection.html?highlight=find#pymongo.collection.Collection.find for more details.


Examples
--------

.. code-block:: yaml+jinja

    
    - hosts: all
      gather_facts: false
      vars:
        mongodb_parameters:
          #mandatory parameters
          database: 'local'
          #optional
          collection: "startup_log"
          connection_string: "mongodb://localhost/"
          extra_connection_parameters: { "ssl" : True , "ssl_certfile": /etc/self_signed_certificate.pem" }
          #optional query  parameters, we accept any parameter from the normal mongodb query.
          filter:  { "hostname": "batman" }
          projection: { "pid": True    , "_id" : False , "hostname" : True }
          skip: 0
          limit: 1
          sort:  [ [ "startTime" , "ASCENDING" ] , [ "age", "DESCENDING" ] ]
      tasks:
        - debug: msg="Mongo has already started with the following PID [{{ item.pid }}]"
          with_mongodb: "{{mongodb_parameters}}"





Status
------




Author
~~~~~~

- Marcos Diez <marcos (at) unitron.com.br>


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/mongodb.py>`_ to improve it.
