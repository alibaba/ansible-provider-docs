:source: openshift.py


.. _openshift_inventory:


openshift - OpenShift inventory source
++++++++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Fetch containers, services and routes for one or more clusters
- Groups by cluster name, namespace, namespace_services, namespace_pods, namespace_routes, and labels
- Uses openshift.(yml|yaml) YAML configuration file to set parameter values.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this inventory.

- python >= 2.7
- openshift >= 0.6
- PyYAML >= 3.11


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
                    <b>connections</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Optional list of cluster connection settings. If no connections are provided, the default <em>~/.kube/config</em> and active context will be used, and objects will be returned for all namespaces the active user is authorized to access.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
    # File must be named openshift.yaml or openshift.yml

    # Authenticate with token, and return all pods and services for all namespaces
    plugin: openshift
    connections:
        host: https://192.168.64.4:8443
        token: xxxxxxxxxxxxxxxx
        ssl_verify: false

    # Use default config (~/.kube/config) file and active context, and return objects for a specific namespace
    plugin: openshift
    connections:
        namespaces:
        - testing

    # Use a custom config file, and a specific context.
    plugin: openshift
    connections:
      - kubeconfig: /path/to/config
        context: 'awx/192-168-64-4:8443/developer'





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/inventory/openshift.py>`_ to improve it.
