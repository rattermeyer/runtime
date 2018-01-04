Role Name
=========

A brief description of the role goes here.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

# defaults file for ansible-role-nomad

| Variable                          | Default                                                                         | Description |
|:----------------------------------|:--------------------------------------------------------------------------------|:------------|
| nomad_version                     | 0.5.2                                                                           |             |
| nomad_sha256sum                   | 7f23aa44686b2ae505ecfc5364a43f87c2a029ea03f6ab050384f2a2b32ac648                |             |
| nomad_client                      | true                                                                            |             |
| nomad_server                      | false                                                                           |             |
| nomad_telemetry                   | false                                                                           |             |
| nomad_iface                       | eth0                                                                            |             |
| nomad_region                      | "global"                                                                        |             |
| nomad_datacenter                  | "dc1"                                                                           |             |
| nomad_name                        | ''                                                                              |             |
| nomad_log_level                   | "INFO"                                                                          |             |
| nomad_bind_addr                   | "{{ hostvars[inventory_hostname]['ansible_'+nomad_iface]['ipv4']['address'] }}" |             |
| nomad_enable_debug                | false                                                                           |             |
| nomad_ports_http                  | 4646                                                                            |             |
| nomad_ports_rpc                   | 4647                                                                            |             |
| nomad_ports_serf                  | 4648                                                                            |             |
| nomad_addresses_http              | "{{ nomad_bind_addr }}"                                                         |             |
| nomad_addresses_rpc               | "{{ nomad_bind_addr }}"                                                         |             |
| nomad_addresses_serf              | "{{ nomad_bind_addr }}"                                                         |             |
| nomad_advertise_rpc               | "{{ nomad_bind_addr }}"                                                         |             |
| nomad_advertise_serf              | "{{ nomad_bind_addr }}"                                                         |             |
| nomad_leave_on_interrupt          | false                                                                           |             |
| nomad_leave_on_terminate          | false                                                                           |             |
| nomad_enable_syslog               | false                                                                           |             |
| nomad_syslog_facility             | "LOCAL0"                                                                        |             |
| nomad_disable_update_check        | false                                                                           |             |
| nomad_disable_anonymous_signature | false                                                                           |             |
| nomad_telemetry_statsite_address  | ''                                                                              |             |
| nomad_telemetry_statsd_address    | ''                                                                              |             |
| nomad_telemetry_disable_hostname  | false                                                                           |             |
| nomad_server_bootstrap_expect     | 3                                                                               |             |
| nomad_server_data_dir             | "{{ nomad_data_dir }}/server"                                                   |             |
| nomad_server_protocol_version     | ''                                                                              |             |
| nomad_server_num_schedulers       | "{{ ansible_processor_cores }}"                                                 |             |
| nomad_server_enabled_schedulers   | []                                                                              |             |
| nomad_server_node_gc_threshold    | ''                                                                              |             |
| nomad_server_rejoin_after_leave   | ''                                                                              |             |
| nomad_server_retry_join           | []                                                                              |             |
| nomad_server_retry_interval       | 30s                                                                             |             |
| nomad_server_retry_max            | 0                                                                               |             |
| nomad_server_start_join           | []                                                                              |             |
| nomad_client_state_dir            | "{{ nomad_data_dir }}/client"                                                   |             |
| nomad_client_alloc_dir            | "{{ nomad_data_dir }}/alloc"                                                    |             |
| nomad_client_servers              | []                                                                              |             |
| nomad_client_node_id              | ''                                                                              |             |
| nomad_client_node_class           | ''                                                                              |             |
| nomad_client_meta                 | {}                                                                              |             |


Example Playbook
----------------

    - hosts: nomadhosts
      become: True
      roles:
        - role: rattermeyer.nomad
          nomad_iface: 'enp0s8'

License
-------

MIT
