# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.box_check_update = false
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--usb", "on"]
    vb.customize ["modifyvm", :id, "--usbehci", "off"]
    vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
    vb.customize ["modifyvm", :id, "--nicpromisc3", "allow-all"]
    vb.customize ["modifyvm", :id, "--nicpromisc4", "allow-all"]
    vb.customize ["modifyvm", :id, "--nicpromisc5", "allow-all"]
    vb.cpus = 1
  end
   config.vm.define "switch" do |switch|
     switch.vm.box = "ubuntu/bionic64"
     switch.vm.hostname = "switch"
     switch.vm.network "private_network", virtualbox__intnet: true, auto_config: false
     switch.vm.provision "shell", path: "switch.sh"
     switch.vm.provider "virtualbox" do |v|
       v.name = "switch"
     end
   end 
# The following line is inserted by the gui.py file

    config.vm.define "pc#{i}" do |pc|
      pc.vm.box = "ubuntu/bionic64"
      pc.vm.hostname = "pc#{i}"
      pc.vm.network "private_network", virtualbox__intnet: true, auto_config: false 
      pc.vm.provision "shell", path: "pc#{i}.sh"
      pc.vm.provider "virtualbox" do |v|
        v.name = "pc#{i}"
      end
    end
  end

end
