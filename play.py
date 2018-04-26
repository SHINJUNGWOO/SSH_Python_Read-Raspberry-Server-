import paramiko
from class_dir import commandline
import sys

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.0.21', username='pi', password='0000')
order=commandline()
print("--------------connected----------------")
while True:
    order.command_input()
    stdin, stdout, stderr = ssh.exec_command(order.file_read())
    temp_dir=[]
    for line in stdout:
        temp_dir.append(line[:-1])
    order.dir=temp_dir
    #dir Testing and class get list of dir
    stdin, stdout, stderr = ssh.exec_command(order.command)

    for line in stdout:
        print(line)


ssh.close()
