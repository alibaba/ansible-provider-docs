:source: host_list.py


.. _host_list_inventory:


host_list - Parses a 'host list' string
+++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Parses a host list string as a comma separated values of hosts
- This plugin only applies to inventory strings that are not paths and contain a comma.






Examples
--------

.. code-block:: yaml+jinja

    
        # define 2 hosts in command line
        # ansible -i '10.10.2.6, 10.10.2.4' -m ping all

        # DNS resolvable names
        # ansible -i 'host1.example.com, host2' -m user -a 'name=me state=absent' all

        # just use localhost
        # ansible-playbook -i 'localhost,' play.yml -c local





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/inventory/host_list.py>`_ to improve it.
