:source: _openshift.py


.. _openshift_lookup:


openshift - Query the K8s API
+++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Uses the OpenShift Python client to fetch a specific object by name, all matching objects within a namespace, or all matching objects for all namespaces, as well as information about the cluster.
- Provides access the full range of K8s APIs.
- Enables authentication via config file, certificates, password or token.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this lookup.

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
                    <b>api_key</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>api_version</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">v1</div>
                                    </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Use to specify the API version. If <em>resource definition</em> is provided, the <em>apiVersion</em> from the <em>resource_definition</em> will override this option.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>cert_file</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>cluster_info</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Use to specify the type of cluster information you are attempting to retrieve. Will take priority over all the other options.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>context</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>field_selector</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Specific fields on which to query. Ignored when <em>resource_name</em> is provided.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>host</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>key_file</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_HOST environment variable.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kind</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Use to specify an object model. If <em>resource definition</em> is provided, the <em>kind</em> from a <em>resource_definition</em> will override this option.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kubeconfig</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the openshift client will attempt to load the default configuration file from <em>~/.kube/config.json</em>. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>label_selector</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Additional labels to include in the query. Ignored when <em>resource_name</em> is provided.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>namespace</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Limit the objects returned to a specific namespace. If <em>resource definition</em> is provided, the <em>metadata.namespace</em> value from the <em>resource_definition</em> will override this option.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>password</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>resource_definition</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Provide a YAML configuration for an object. NOTE: <em>kind</em>, <em>api_version</em>, <em>resource_name</em>, and <em>namespace</em> will be overwritten by corresponding values found in the provided <em>resource_definition</em>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>resource_name</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Fetch a specific object by name. If <em>resource definition</em> is provided, the <em>metadata.name</em> value from the <em>resource_definition</em> will override this option.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>src</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Provide a path to a file containing a valid YAML definition of an object dated. Mutually exclusive with <em>resource_definition</em>. NOTE: <em>kind</em>, <em>api_version</em>, <em>resource_name</em>, and <em>namespace</em> will be overwritten by corresponding values found in the configuration read in from the <em>src</em> file.</div>
                                                    <div>Reads from the local file system. To read from the Ansible controller's file system, use the file lookup plugin or template lookup plugin, combined with the from_yaml filter, and pass the result to <em>resource_definition</em>. See Examples below.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>ssl_ca_cert</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Path to a CA certificate used to authenticate with the API. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>username</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>verify_ssl</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                    <td>
                                                                                            </td>
                                                <td>
                                                                        <div>Whether or not to verify the API server's SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - The OpenShift Python client wraps the K8s Python client, providing full access to all of the APIS and models available on both platforms. For API version details and additional information visit https://github.com/openshift/openshift-restclient-python


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Fetch a list of namespaces
      set_fact:
        projects: "{{ lookup('k8s', api_version='v1', kind='Namespace') }}"

    - name: Fetch all deployments
      set_fact:
        deployments: "{{ lookup('k8s', kind='Deployment', namespace='testing') }}"

    - name: Fetch all deployments in a namespace
      set_fact:
        deployments: "{{ lookup('k8s', kind='Deployment', namespace='testing') }}"

    - name: Fetch a specific deployment by name
      set_fact:
        deployments: "{{ lookup('k8s', kind='Deployment', namespace='testing', resource_name='elastic') }}"

    - name: Fetch with label selector
      set_fact:
        service: "{{ lookup('k8s', kind='Service', label_selector='app=galaxy') }}"

    # Use parameters from a YAML config

    - name: Load config from the Ansible controller filesystem
      set_fact:
        config: "{{ lookup('file', 'service.yml') | from_yaml }}"

    - name: Using the config (loaded from a file in prior task), fetch the latest version of the object
      set_fact:
        service: "{{ lookup('k8s', resource_definition=config) }}"

    - name: Use a config from the local filesystem
      set_fact:
        service: "{{ lookup('k8s', src='service.yml') }}"




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
                    <b>_list</b>
                    <br/><div style="font-size: small; color: red">complex</div>
                                    </td>
                <td></td>
                <td>
                                                                        <div>One ore more object definitions returned from the API.</div>
                                                                <br/>
                                    </td>
            </tr>
                                                            <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>status</b>
                    <br/><div style="font-size: small; color: red">complex</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Current status details for the object.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>kind</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Represents the REST resource this object represents.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>spec</b>
                    <br/><div style="font-size: small; color: red">complex</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Specific attributes of the object. Will vary based on the <em>api_version</em> and <em>kind</em>.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>api_version</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>The versioned schema of this representation of an object.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                    <td class="elbow-placeholder">&nbsp;</td>
                                <td colspan="1">
                    <b>metadata</b>
                    <br/><div style="font-size: small; color: red">complex</div>
                                    </td>
                <td>success</td>
                <td>
                                            <div>Standard object metadata. Includes name, namespace, annotations, labels, etc.</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/lookup/_openshift.py>`_ to improve it.
