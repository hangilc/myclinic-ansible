#!/bin/bash

# clone myclinic-ansible

if [ ! -d ~/myclinic-ansible ]; then
	GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no" git clone git@github.com:hangilc/myclinic-ansible.git ~/myclinic-ansible
fi

if [ ! -d /etc/ansible ]; then
    sudo mkdir /etc/ansible
    sudo chown root:$USER /etc/ansible
    sudo chmod 770 /etc/ansible
fi

if [ ! -f /etc/ansible/hosts ]; then
    sudo touch /etc/ansible/hosts
    sudo chown root:$USER /etc/ansible/hosts
	sudo chmod 660 /etc/ansible/hosts
fi

echo "Copy inventory.sample to /etc/ansible/hosts"

