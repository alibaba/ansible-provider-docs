:source: ini.py


.. _ini_inventory:


ini - Uses an Ansible INI file as inventory source.
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- INI file based inventory, sections are groups or group related with special `:modifiers`.
- Entries in sections ``[group_1]`` are hosts, members of the group.
- Hosts can have variables defined inline as key/value pairs separated by ``=``.
- The ``children`` modifier indicates that the section contains groups.
- The ``vars`` modifier indicates that the section contains variables assigned to members of the group.
- Anything found outside a section is considered an 'ungrouped' host.
- Values passed in using the ``key=value`` syntax are interpreted as Python literal structure (strings, numbers, tuples, lists, dicts, booleans, None), alternatively as string. For example ``var=FALSE`` would create a string equal to 'FALSE'. Do not rely on types set during definition, always make sure you specify type with a filter when needed when consuming the variable.





Notes
-----

.. note::
    - It takes the place of the previously hardcoded INI inventory.
    - To function it requires being whitelisted in configuration.
    - Variable values are processed by Python's ast.literal_eval function (https://docs.python.org/2/library/ast.html#ast.literal_eval) which could cause the value to change in some cases. See the Examples for proper quoting to prevent changes. Another option would be to use the yaml format for inventory source which processes the values correctly.


Examples
--------

.. code-block:: yaml+jinja

    
      example1: |
          # example cfg file
          [web]
          host1
          host2 ansible_port=222

          [web:vars]
          http_port=8080 # all members of 'web' will inherit these
          myvar=23

          [web:children] # child groups will automatically add their hosts to partent group
          apache
          nginx

          [apache]
          tomcat1
          tomcat2 myvar=34 # host specific vars override group vars
          tomcat3 mysecret="'03#pa33w0rd'" # proper quoting to prevent value changes

          [nginx]
          jenkins1

          [nginx:vars]
          has_java = True # vars in child groups override same in parent

          [all:vars]
          has_java = False # 'all' is 'top' parent

      example2: |
          # other example config
          host1 # this is 'ungrouped'

          # both hosts have same IP but diff ports, also 'ungrouped'
          host2 ansible_host=127.0.0.1 ansible_port=44
          host3 ansible_host=127.0.0.1 ansible_port=45

          [g1]
          host4

          [g2]
          host4 # same host as above, but member of 2 groups, will inherit vars from both
                # inventory hostnames are unique





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/plugins/inventory/ini.py>`_ to improve it.
