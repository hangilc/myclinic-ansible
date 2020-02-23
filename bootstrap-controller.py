import yaml
import os
import re

def put_file(path, body, mode):
    path = os.path.expanduser(path)
    with open(path, "w") as f:
        f.write(body)
    os.chmod(path, mode)

def set_env(key, value):
    path = os.path.expanduser("~/.bashrc")
    with open(path, "r") as f:
        content = f.read()
    content = re.sub("^export {}=.+\n".format(key), "", 
            content, flags=re.MULTILINE)
    s = "export {}={}\n".format(key, value)
    content += s
    with open(path, "w") as f:
        f.write(content)

def handle_secrets(yml):
    if "id_vm.pub" in yml:
        put_file("~/.ssh/id_vm.pub", yml["id_vm.pub"], 0o644)
        put_file("~/.ssh/authorized_keys", yml["id_vm.pub"], 0o600)
    if "id_vm" in yml:
        put_file("~/.ssh/id_vm", yml["id_vm"], 0o600)
    if "vault-password.txt" in yml:
        put_file("~/.ansible/vault-password.txt", 
                yml["vault-password.txt"],
                0o600)
    if "crypt-file-key.txt" in yml:
        put_file("~/.crypt-file/key.txt",
                yml["crypt-file-key.txt"],
                0o600)
    if "AWS_ACCESS_KEY_ID" in yml:
        set_env("AWS_ACCESS_KEY_ID", yml["AWS_ACCESS_KEY_ID"])
    if "AWS_SECRET_ACCESS_KEY" in yml:
        set_env("AWS_SECRET_ACCESS_KEY", yml["AWS_SECRET_ACCESS_KEY"])

if __name__ == '__main__':
    with open("myclinic-secrets.yml") as src:
        yml = yaml.load(src)
        handle_secrets(yml)

