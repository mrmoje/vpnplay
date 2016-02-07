# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    config.vm.box = "ubuntu/trusty64"

    config.vm.define "vpnserv" do |machine|
        machine.vm.network :private_network, ip: "10.0.0.2",
            :netmask => "255.255.255.0"
        machine.vm.hostname = "vpnserv"
        machine.vm.provider :virtualbox do |v, o|
            o.vm.provision "shell", inline: "sudo apt-get update; sudo apt-get --yes install avahi-daemon"
            o.ssh.insert_key = false
            o.vm.hostname = "vpnserv.local"
            v.customize ["modifyvm", :id, "--memory", 1024]
        end
    end
end
