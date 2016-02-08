# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    config.vm.box = "ubuntu/trusty64"

    config.vm.provider :virtualbox do |v, o|
      o.vm.provision "shell", inline: "sudo apt-get update; sudo apt-get --yes install avahi-daemon"
      o.ssh.insert_key = false
      v.customize ["modifyvm", :id, "--memory", 512]
    end

    config.vm.define "vpnserv-1" do |machine|
        machine.vm.network :private_network, ip: "10.0.0.2",
            :netmask => "255.255.255.0"
        machine.vm.hostname = "vpnserv-1"
        machine.vm.provider :virtualbox do |v, o|
            o.vm.hostname = "vpnserv-1.local"
        end
    end
    config.vm.define "vpnclient-debian-1" do |machine|
        machine.vm.network :private_network, ip: "10.0.0.3",
            :netmask => "255.255.255.0"
        machine.vm.hostname = "vpnclient-debian-1"
        machine.vm.provider :virtualbox do |v, o|
            o.vm.provision "shell", inline: "apt-get update; apt-get --yes install xinit xterm openbox chromium-browser"
            o.vm.hostname = "vpnclient-debian-1.local"
            v.gui = true
        end
    end
end
