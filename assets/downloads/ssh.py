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
device.exec_command("command1")
device.exec_command("command2")
device.exec_command("command3")
# ...
iproxy.terminate() # terminate iproxy ssesion
iproxy.kill() # kill iproxy