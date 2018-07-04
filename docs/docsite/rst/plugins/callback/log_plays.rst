:source: log_plays.py


.. _log_plays_callback:


log_plays - write playbook output to log file
+++++++++++++++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This callback writes playbook output to a file per host in the `/var/log/ansible/hosts` directory
- TODO: make this configurable



Requirements
~~~~~~~~~~~~
The below requirements are needed on the local master node that executes this callback.

- Whitelist in configuration
- A writeable /var/log/ansible/hosts directory by the user executing Ansible on the controller








Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/callback/log_plays.py>`_ to improve it.
