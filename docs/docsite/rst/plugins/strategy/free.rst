:source: free.py


.. _free_strategy:


free - Executes tasks on each host independently
++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.0

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Task execution is as fast as possible per host in batch as defined by ``serial`` (default all). Ansible will not wait for other hosts to finish the current task before queuing the next task for a host that has finished. Once a host is done with the play, it opens it's slot to a new host that was waiting to start.










Status
------




Author
~~~~~~

- Ansible Core Team


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/strategy/free.py>`_ to improve it.
