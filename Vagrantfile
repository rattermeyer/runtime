# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant vagranturation is done below. The "2" in Vagrant.vagranture
# vagrantures the vagranturation version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|

  # Fuer vagrant script Ausgaben
  ui = Vagrant::UI::Colored.new
  default_mem = 2560
  default_cpu = 1

  # The most common vagranturation options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.
  # VirtualBox Configuration

  machines = {
               :server1     => {:ip => '192.168.56.21', :box => 'geerlingguy/ubuntu1804', :mem => '4096', :cpu => 2 },
               :server2     => {:ip => '192.168.56.22', :box => 'geerlingguy/ubuntu1804', :mem => '4096', :cpu => 2 },
               :server3     => {:ip => '192.168.56.23', :box => 'geerlingguy/ubuntu1804', :mem => '4096', :cpu => 2 },
               :worker1     => {:ip => '192.168.56.24', :box => 'geerlingguy/ubuntu1804', :mem => '2048', :cpu => 1 },
               :worker2     => {:ip => '192.168.56.25', :box => 'geerlingguy/ubuntu1804', :mem => '2048', :cpu => 1 },
             }

  machines.each do |machine_name, machine_details|
   config.vm.define machine_name do |machine_config|
     machine_ip = machine_details[:ip]
     ui.info("Handling vm with hostname [#{machine_name.to_s}] and IP [#{machine_ip}]")
     machine_config.vm.box_check_update = false
     machine_config.vm.box = machine_details[:box]
     machine_config.vm.network :private_network, ip: machine_ip
     machine_config.vm.hostname = machine_name.to_s
     machine_config.vm.provider :virtualbox do |vb|
       reserved_mem = machine_details[:mem] || default_mem
       reserved_cpu = machine_details[:cpu] || default_cpu
       vb.name = machine_name.to_s
       vb.customize ["modifyvm", :id, "--groups", "/opendp"]
       vb.customize ["modifyvm", :id, "--memory", reserved_mem]
       vb.customize ["modifyvm", :id, "--cpus", reserved_cpu]
       vb.gui = false
     end #vb
     machine_config.vm.provision "shell", inline: "apt-get install python2.7"
   end # machine_config
  end # machines

  config.vm.define "controller", autostart: true do |vm_config|
    vm_config.vm.box = "geerlingguy/ubuntu1804"
    vm_config.vm.box_check_update = false
    vm_config.vm.hostname = "controller"
    vm_config.vm.synced_folder ".", "/vagrant"
    vm_config.vm.synced_folder "./.vagrant", "/vagrant/.vagrant", mount_options: ["dmode=700,fmode=600"]
    vm_config.vm.synced_folder "~/ansible/roles", "/etc/ansible/roles"
    vm_config.vm.network :private_network, ip: "192.168.56.10"
    vm_config.vm.provider :virtualbox do |vb|
      vb.name = "controller"
      vb.customize ["modifyvm", :id, "--groups", "/opendp"]
      vb.customize ["modifyvm", :id, "--memory", 512]
      vb.customize ["modifyvm", :id, "--cpus", 1]
      vb.gui = false
    end
    vm_config.vm.provision "shell", path: "scripts/ansible.sh"
  end

end
