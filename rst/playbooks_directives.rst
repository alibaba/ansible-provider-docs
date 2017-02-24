Directives Glossary
===================

Here we list the common playbook objects and their directives.
Note that not all directives affect the object itself and might just be there to be inherited by other contained objects.
Aliases for the directives are not reflected here, nor are mutable ones, for example `action` in task can be substituted by the name of any module plugin.

.. contents::
   :local:
   :depth: 1


Play
----
  * accelerate
  * accelerate_ipv6
  * accelerate_port
  * always_run
  * any_errors_fatal
  * become
  * become_flags
  * become_method
  * become_user
  * check_mode
  * connection
  * environment
  * force_handlers
  * gather_facts
  * gather_subset
  * gather_timeout
  * handlers
  * hosts
  * ignore_errors
  * max_fail_percentage
  * name
  * no_log
  * port
  * post_tasks
  * pre_tasks
  * remote_user
  * roles
  * run_once
  * serial
  * strategy
  * tags
  * tasks
  * vars
  * vars_files
  * vars_prompt
  * vault_password


Role
----
  * always_run
  * become
  * become_flags
  * become_method
  * become_user
  * check_mode
  * connection
  * delegate_facts
  * delegate_to
  * environment
  * ignore_errors
  * no_log
  * port
  * remote_user
  * run_once
  * tags
  * vars
  * when


Block
-----
  * always
  * always_run
  * any_errors_fatal
  * become
  * become_flags
  * become_method
  * become_user
  * block
  * check_mode
  * connection
  * delegate_facts
  * delegate_to
  * environment
  * ignore_errors
  * name
  * no_log
  * port
  * remote_user
  * rescue
  * run_once
  * tags
  * vars
  * when


Task
----
  * action
  * always_run
  * any_errors_fatal
  * args
  * async
  * become
  * become_flags
  * become_method
  * become_user
  * changed_when
  * check_mode
  * connection
  * delay
  * delegate_facts
  * delegate_to
  * environment
  * failed_when
  * ignore_errors
  * local_action
  * loop
  * loop_args
  * loop_control
  * name
  * no_log
  * notify
  * poll
  * port
  * register
  * remote_user
  * retries
  * run_once
  * tags
  * until
  * vars
  * when
  * with_<lookup_plugin>

