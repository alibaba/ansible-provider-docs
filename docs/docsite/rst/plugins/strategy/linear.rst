:source: linear.py


.. _linear_strategy:


linear - Executes tasks in a linear fashion
+++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Task execution is in lockstep per host batch as defined by ``serial`` (default all). Up to the fork limit of hosts will execute each task at the same time and then the next series of hosts until the batch is done, before going on to the next task.





Notes
-----

.. note::
    - This was the default Ansible behaviour before 'strategy plugins' were introduced in 2.0.






Status
------




Author
~~~~~~

- Ansible Core Team


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/strategy/linear.py>`_ to improve it.
