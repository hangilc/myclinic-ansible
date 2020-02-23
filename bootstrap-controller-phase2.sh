#!/bin/bash

# setup PATH

if cat ~/.bashrc | grep -q "export PATH=~/bin:"; then
	: #nop
else
	echo 'export PATH=~/bin:~/.local/bin:~/go/bin:$PATH' >> ~/.bashrc
fi

# apt install

sudo apt install -y software-properties-common python3-pip python3-venv
sudo -H pip3 install ansible pyyaml

# install secrets

if [ ! -d ~/.ssh ]; then
    mkdir ~/.ssh
    chmod 700 ~/.ssh
fi

if [ ! -f ~/.ssh/config ]; then
	echo "IdentityFile ~/.ssh/id_vm" >> ~/.ssh/config
    chmod 600 ~/.ssh/config
fi

if [ ! -d ~/.ansible ]; then
	mkdir ~/.ansible
	chmod 700 ~/.ansible
fi

if [ ! -d ~/.crypt-file ]; then
	mkdir ~/.crypt-file
	chmod 700 ~/.crypt-file
fi

read -p "Put ~/myclinic-secrets.yml, then hit ENTER"
if [ -f ~/myclinic-secrets.yml ]; then
	python3 bootstrap-controller.py
fi

echo "Logout, login, and proceed to phase 3."

