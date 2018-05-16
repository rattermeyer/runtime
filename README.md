## Development Setup

This is a short description of my current development setup.
Normally, I develop under Linux. But if required, I will use a cygwin
environment under windows as well.

So my setup is like this:

* ~/ansible/roles : for the following roles
  * rattermeyer.docker
  * rattermeyer.nomad
  * rattermeyer.vault
* seperate checkout for `nomad-cluster`

The repositories are all available on my github repo:

`git clone git@github.com:rattermeyer/nomad-cluster.git`

roles have to cloned like the following

`git@github.com:rattermeyer/ansible-role-vault.git rattermeyer.vault`

The location of roles is defined inside `ansible/ansible.cfg`

You also need to create a `vault_pwd.txt` inside at `ansible/vault_pwd.txt` subdirectory.
For development, the current standard password is `nomad1`

After this, you shoud be able to start the VMs using `vagrant up`.

After powering up of VMs is finished, log in into the `controller` machine, using
`vagrant ssh controller`.

The `controller` is a seperate VM, because [Windows](http://docs.ansible.com/ansible/latest/intro_windows.html#windows-support)
is not supported as an ansible controller

After logging in change to `/vagrant/ansible` and run

`ansible-playbook -v -i inventories/test/inventory.ini site.yml`

That should do the magic and provision a nomad cluster consisting of

* 3 nomad servers and 2 worker nodes
* 3 consul servers
* 2 vault servers
* prometheus / grafana
* elasticsearch, mongodb replica set and graylog (TODO: not finished yet)
* traefik

## Known Issues

* Upgrades of consul / vault are not yet supported
