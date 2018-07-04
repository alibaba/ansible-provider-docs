:source: gcp_compute.py


.. _gcp_compute_inventory:


gcp_compute - Google Cloud Compute Engine inventory source
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Get inventory hosts from Google Cloud Platform GCE.
- Uses a <name>.gcp.yaml (or <name>.gcp.yml) YAML configuration file.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this inventory.

- requests >= 2.18.4
- google-auth >= 1.3.0


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
                    <b>auth_kind</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>The type of credential used.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>cache</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[inventory ]<br>cache = no</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_INVENTORY_CACHE</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Toggle to enable/disable the caching of the inventory's source data, requires a cache plugin setup to work.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>cache_connection</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[inventory ]<br>cache_connection = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_INVENTORY_CACHE_CONNECTION</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Cache connection data or path, read cache plugin documentation for specifics.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>cache_plugin</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[inventory ]<br>cache_plugin = VALUE</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_INVENTORY_CACHE_PLUGIN</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Cache plugin to use for the inventory's source data.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>cache_timeout</b>
                    <br/><div style="font-size: small; color: red">integer</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">3600</div>
                                    </td>
                                                    <td>
                                                    <div> ini entries:
                                                                    <p>[inventory ]<br>cache_timeout = 3600</p>
                                                            </div>
                                                                                                            <div>env:ANSIBLE_INVENTORY_CACHE_TIMEOUT</div>
                                                                                                </td>
                                                <td>
                                                                        <div>Cache duration in seconds</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>compose</b>
                    <br/><div style="font-size: small; color: red">dictionary</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{}</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>create vars from jinja2 expressions</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>filters</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>A list of filter value pairs. Available filters are listed here <a href='https://cloud.google.com/compute/docs/reference/rest/v1/instances/list'>https://cloud.google.com/compute/docs/reference/rest/v1/instances/list</a>. Each additional filter in the list will act be added as an AND condition (filter1 and filter2)</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>groups</b>
                    <br/><div style="font-size: small; color: red">dictionary</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">{}</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>add hosts to group based on Jinja2 conditionals</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>hostnames</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[u&#39;public_ip&#39;, u&#39;private_ip&#39;, u&#39;name&#39;]</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>A list of options that describe the ordering for which hostnames should be assigned. Currently supported hostnames are 'public_ip', 'private_ip', or 'name'.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>keyed_groups</b>
                    <br/><div style="font-size: small; color: red">list</div>                                                        </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[]</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>add hosts to group based on the values of a variable</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>projects</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>A list of projects in which to describe GCE instances.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>service_account_email</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>An optional service account email address if machineaccount is selected and the user does not wish to use the default email.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>service_account_file</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>The path of a Service Account JSON file if serviceaccount is selected as type.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>strict</b>
                    <br/><div style="font-size: small; color: red">boolean</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                <b>Default:</b><br/><div style="color: blue">no</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>If true make invalid entries a fatal error, otherwise skip and continue</div>
                                                    <div>Since it is possible to use facts in the expressions they might not always be available and we ignore those errors by default.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>zones</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">all zones available to a given project</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>A list of regions in which to describe GCE instances.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    plugin: gcp_compute
    zones: # populate inventory with instances in these regions
      - us-east1-a
    projects:
      - gcp-prod-gke-100
      - gcp-cicd-101
    filters:
      - machineType = n1-standard-1
      - scheduling.automaticRestart = true AND machineType = n1-standard-1

    scopes:
      - https://www.googleapis.com/auth/compute
    service_account_file: /tmp/service_account.json
    auth_kind: serviceaccount





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/inventory/gcp_compute.py>`_ to improve it.
