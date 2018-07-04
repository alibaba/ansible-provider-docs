:source: local.py


.. _local_connection:


local - execute on controller
+++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This connection plugin allows ansible to execute tasks on the Ansible 'controller' instead of on a remote host.





Notes
-----

.. note::
    - The remote user is ignored, the user with which the ansible CLI was executed is used instead.






Status
------




Author
~~~~~~

- ansible (@core)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/connection/local.py>`_ to improve it.
