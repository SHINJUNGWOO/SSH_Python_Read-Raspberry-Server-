import paramiko
from class_dir import commandline
from Mouse_Macro import *
import sys

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.0.21', username='pi', password='0000')
order=commandline()
print("--------------connected----------------")
Mode=1
#Mode ==0 just read mode
#Mode ==1 read giro data
while Mode==0:
    order.command_input()
    stdin, stdout, stderr = ssh.exec_command(order.file_read())
    temp_dir=[]
    for line in stdout:
        temp_dir.append(line[:-1])
    order.dir=temp_dir
    #dir Testing and class get list of dir
    stdin, stdout, stderr = ssh.exec_command(order.command)

    for line in stdout:
        print(line[:-1])



while Mode==1:
    stdin, stdout, stderr = ssh.exec_command("cd giro/RTIMULib/Linux/python/tests;python Fusion10.py")
    #"cd giro/RTIMULib/Linux/python/tests;python Fusion10.py" is directory of Fusion10.py

    for line in stdout:
        if(line[0]=='r'):
            r_location=line.find('r')
            p_location = line.find('p')
            y_location = line.find('y')
            r=float(line[r_location+3:p_location-1])
            p=float(line[p_location+3:y_location-1])
            y=float(line[y_location+3:-1])
            print(r,p,y)

        else:
            print(line[-1])

ssh.close()

