#!/bin/bash

# bootstrap ansible controller from freshly installed Ubuntu 18.04 desktop

# sudo without password

if sudo cat /etc/sudoers | grep -q "^$USER"; then
	: # nop
else
	echo "hangil ALL=(ALL) NOPASSWD:ALL" | sudo tee -a /etc/sudoers
fi

# install packages and ansible

sudo apt update
sudo apt -y upgrade
sudo apt install -y ssh vim

# install Guest Additions

read -p "Install VirtualBox Guest Addtions? [y/n]: " yn
if [ $yn == "y" ]; then
	sudo apt install -y gcc perl make
	echo "################"
	echo "Install guest additions, reboot, and move to phase2."
	read
fi
