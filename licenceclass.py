# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
import re,uuid
import os
class licenceclass(QtCore.QObject):
    def __init__(self):
        pass

    def getserial():
        # Extract serial from cpuinfo file
        cpuserial = "0000000000000000"
        try:
            f = open('/proc/cpuinfo','r')
            for line in f:
                if line[0:6]=='Serial':
                    cpuserial = line[10:26]
            f.close()

        except:
            cpuserial = "ERROR000000000"
        return cpuserial

    def getmac():
        mykey=re.findall('..', '%012x' % uuid.getnode())
        data=""
        for mydata in mykey:
            data=data+mydata
        return data

    '''os.system("echo '1' | sudo -S shutdown -h now")'''

    def generatelicense():
        try:
           #print('Key Generate')
           cpu=licenceclass.getserial()
           etho=licenceclass.getmac()
           os.system("echo '1' | sudo -S chmod 777 /usr/local/sltlic/sltapp_lic.lic")
           state=False
           with open('/usr/local/sltlic/sltapp_lic.lic', 'r') as file:
               content = file.read().strip()
               file.close()
               #print(content)  # Dis
               #print(len(content))
               if len(content) == 17 :
                  if content=='00000000000000000':
                     #print('data read')
                     with open('/usr/local/sltlic/sltapp_lic.lic', 'w') as wfile:
                         wfile.write(cpu+'|'+etho)
                         content = wfile.read().strip()
                         wfile.close()
               if len(content) == 29 :
                  if content!='':
                      #print('data read')
                      lic=content.split('|')
                      if lic[0] == cpu:
                          if lic[1] == etho:
                              state=True
                          else:
                              state=False
           return state
        except Exception as e:
            print(e)

