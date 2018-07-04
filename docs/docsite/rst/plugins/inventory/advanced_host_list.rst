:source: advanced_host_list.py


.. _advanced_host_list_inventory:


advanced_host_list - Parses a 'host list' with ranges
+++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Parses a host list string as a comma separated values of hosts and supports host ranges.
- This plugin only applies to inventory sources that are not paths and contain at least one comma.






Examples
--------

.. code-block:: yaml+jinja

    
        # simple range
        # ansible -i 'host[1:10],' -m ping

        # still supports w/o ranges also
        # ansible-playbook -i 'localhost,' play.yml





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/inventory/advanced_host_list.py>`_ to improve it.
