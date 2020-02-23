import yaml
import os
import re
import subprocess

def put_file(path, body, mode):
    path = os.path.expanduser(path)
    with open(path, "w") as f:
        f.write(body)
    os.chmod(path, mode)

def set_env(edict):
    path = os.path.expanduser("~/.bashrc")
    with open(path, "r") as f:
        content = f.read()
    for key in edict:
        value = edict[key]
        content = re.sub("^export {}=.+\n".format(key), "", 
                content, flags=re.MULTILINE)
        s = "export {}={}\n".format(key, value)
        content += s
    with open(path, "w") as f:
        f.write(content)

def handle_secrets(yml):
    edict = dict()
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
        put_file("~/.crypt-file/key.txt", \
                yml["crypt-file-key.txt"], \
                0o600)
    if "AWS_ACCESS_KEY_ID" in yml:
        edict["AWS_ACCESS_KEY_ID"] = yml["AWS_ACCESS_KEY_ID"]
    if "AWS_SECRET_ACCESS_KEY" in yml:
        edict["AWS_SECRET_ACCESS_KEY"] = yml["AWS_SECRET_ACCESS_KEY"]
    if "git_user_name" in yml:
        name = yml["git_user_name"]
        subprocess.run(["git", "config", "--global", "user.name", name])
    if "git_user_email" in yml:
        email = yml["git_user_email"]
        subprocess.run(["git", "config", "--global", "user.email", email])
    for k in ["MYCLINIC_DB_ADMIN_USER", "MYCLINIC_DB_ADMIN_PASS", \
        "MYCLINIC_DB_USER", "MYCLINIC_DB_PASS"]:
        if k in yml:
            edict[k] = yml[k]
    print(edict)
    set_env(edict)

if __name__ == '__main__':
    path = os.path.expanduser("~/myclinic-secrets.yml")
    with open(path) as src:
        yml = yaml.load(src)
        handle_secrets(yml)

