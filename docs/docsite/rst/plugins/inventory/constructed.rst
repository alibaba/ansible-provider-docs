:source: constructed.py


.. _constructed_inventory:


constructed - Uses Jinja2 to construct vars and groups based on existing inventory.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Uses a YAML configuration file with a valid YAML or ``.config`` extension to define var expressions and group conditionals
- The Jinja2 conditionals that qualify a host for membership.
- The JInja2 exprpessions are calculated and assigned to the variables
- Only variables already available from previous inventories or the fact cache can be used for templating.
- When *strict* is False, failed expressions will be ignored (assumes vars were missing).




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
                        </table>
    <br/>



Examples
--------

.. code-block:: yaml+jinja

    
        # inventory.config file in YAML format
        plugin: constructed
        strict: False
        compose:
            var_sum: var1 + var2

            # this variable will only be set if I have a persistent fact cache enabled (and have non expired facts)
            # `strict: False` will skip this instead of producing an error if it is missing facts.
            server_type: "ansible_hostname | regex_replace ('(.{6})(.{2}).*', '\\2')"
        groups:
            # simple name matching
            webservers: inventory_hostname.startswith('web')

            # using ec2 'tags' (assumes aws inventory)
            development: "'devel' in (ec2_tags|list)"

            # using other host properties populated in inventory
            private_only: not (public_dns_name is defined or ip_address is defined)

            # complex group membership
            multi_group: (group_names|intersection(['alpha', 'beta', 'omega']))|length >= 2

        keyed_groups:
            # this creates a group per distro (distro_CentOS, distro_Debian) and assigns the hosts that have matching values to it,
            # using the default separator "_"
            - prefix: distro
              key: ansible_distribution

            # this creates a group per ec2 architecture and assign hosts to the matching ones (arch_x86_64, arch_sparc, etc)
            - prefix: arch
              key: ec2_architecture





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/inventory/constructed.py>`_ to improve it.
