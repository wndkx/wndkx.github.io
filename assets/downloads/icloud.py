#!/usr/bin/env python3
import subprocess
import paramiko


RPORT = 44
LPORT = 2222
password = "alpine"
iproxy = subprocess.Popen(["iproxy", str(LPORT), str(RPORT)], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
device = paramiko.SSHClient()
device.set_missing_host_key_policy(paramiko.AutoAddPolicy())

while True:
    try:
        device.connect('localhost', username='root', password=password, port=LPORT)
        break
    except:
        print("Error")
        continue
device.exec_command("mount -o rw,union,update /") # mount file system
device.exec_command('echo "" > /.mount_rw') # mount file system
device.exec_command("mv /Application/Setup.app /Application/Setup.app.backup") # Deletes Setup.app
device.exec_command("uicache --all") # clears uicache
device.exec_command("rm -rf /var/mobile/Library/Accounts/*") # removes Accounts folder
device.exec_command("killall backboardd")
device.exec_command("reboot") # reboot
iproxy.terminate() # terminate iproxy ssesion
iproxy.kill() # kill iproxy