:source: kubectl.py


.. _kubectl_connection:


kubectl - Execute tasks in pods running on Kubernetes.
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Use the kubectl exec command to run tasks in, or put/fetch files to, pods running on the Kubernetes container platform.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this connection.

- kubectl (go binary)


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
                    <b>kubectl_cert_file</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue"></div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:K8S_AUTH_CERT_FILE</div>
                                                                                                                                        <div>var: ansible_kubectl_cert_file</div>
                                                                        </td>
                                                <td>
                                                                        <div>Path to a certificate used to authenticate with the API.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kubectl_container</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue"></div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:K8S_AUTH_CONTAINER</div>
                                                                                                                                        <div>var: ansible_kubectl_container</div>
                                                                        </td>
                                                <td>
                                                                        <div>Container name. Required when a pod contains more than one container.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kubectl_context</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue"></div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:k8S_AUTH_CONTEXT</div>
                                                                                                                                        <div>var: ansible_kubectl_context</div>
                                                                        </td>
                                                <td>
                                                                        <div>The name of a context found in the K8s config file.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kubectl_extra_args</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue"></div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:K8S_AUTH_EXTRA_ARGS</div>
                                                                                                                                        <div>var: ansible_kubectl_extra_args</div>
                                                                        </td>
                                                <td>
                                                                        <div>Extra arguments to pass to the kubectl command line.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kubectl_host</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue"></div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:K8S_AUTH_HOST</div>
                                                            <div>env:K8S_AUTH_SERVER</div>
                                                                                                                                        <div>var: ansible_kubectl_host</div>
                                                            <div>var: ansible_kubectl_server</div>
                                                                        </td>
                                                <td>
                                                                        <div>URL for accessing the API.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kubectl_key_file</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue"></div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:K8S_AUTH_KEY_FILE</div>
                                                                                                                                        <div>var: ansible_kubectl_key_file</div>
                                                                        </td>
                                                <td>
                                                                        <div>Path to a key file used to authenticate with the API.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kubectl_kubeconfig</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue"></div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:K8S_AUTH_KUBECONFIG</div>
                                                                                                                                        <div>var: ansible_kubectl_kubeconfig</div>
                                                            <div>var: ansible_kubectl_config</div>
                                                                        </td>
                                                <td>
                                                                        <div>Path to a kubectl config file. Defaults to <em>~/.kube/conig</em></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kubectl_namespace</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue"></div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:K8S_AUTH_NAMESPACE</div>
                                                                                                                                        <div>var: ansible_kubectl_namespace</div>
                                                                        </td>
                                                <td>
                                                                        <div>The namespace of the pod</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kubectl_password</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue"></div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:K8S_AUTH_PASSWORD</div>
                                                                                                                                        <div>var: ansible_kubectl_password</div>
                                                                        </td>
                                                <td>
                                                                        <div>Provide a password for authenticating with the API.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kubectl_pod</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue"></div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:K8S_AUTH_POD</div>
                                                                                                                                        <div>var: ansible_kubectl_pod</div>
                                                                        </td>
                                                <td>
                                                                        <div>Pod name. Required when the host name does not match pod name.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kubectl_ssl_ca_cert</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue"></div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:K8S_AUTH_SSL_CA_CERT</div>
                                                                                                                                        <div>var: ansible_kubectl_cert_file</div>
                                                                        </td>
                                                <td>
                                                                        <div>Path to a CA certificate used to authenticate with the API.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kubectl_token</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                    <td>
                                                                                                            <div>env:K8S_AUTH_TOKEN</div>
                                                            <div>env:K8S_AUTH_API_KEY</div>
                                                                                                                                        <div>var: ansible_kubectl_token</div>
                                                            <div>var: ansible_kubectl_api_key</div>
                                                                        </td>
                                                <td>
                                                                        <div>API authentication bearer token.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kubectl_username</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue"></div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:K8S_AUTH_USERNAME</div>
                                                                                                                                        <div>var: ansible_kubectl_username</div>
                                                                        </td>
                                                <td>
                                                                        <div>Provide a username for authenticating with the API.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kubectl_verify_ssl</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue"></div>
                                    </td>
                                                    <td>
                                                                                                            <div>env:K8s_AUTH_VERIFY_SSL</div>
                                                                                                                                        <div>var: ansible_kubectl_verify_ssl</div>
                                                                        </td>
                                                <td>
                                                                        <div>Whether or not to verify the API server's SSL certificate. Defaults to <em>true</em>.</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>







Status
------




Author
~~~~~~

- xuxinkun


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/connection/kubectl.py>`_ to improve it.
