:source: auto.py


.. _auto_inventory:


auto - Loads and executes an inventory plugin specified in a YAML config
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- By whitelisting ``auto`` as the final inventory plugin, any YAML inventory config file with a ``plugin`` key at its root will automatically cause the named plugin to be loaded and executed with that config. This effectively provides automatic whitelisting of all installed/accessible inventory plugins.
- To disable this behavior, remove ``auto`` from the ``INVENTORY_ENABLED`` config element.






Examples
--------

.. code-block:: yaml+jinja

    
    # This plugin is not intended for direct use; it is a fallback mechanism for automatic whitelisting of
    # all installed inventory plugins.





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/inventory/auto.py>`_ to improve it.
