import time
from wifi_class import Wifi

from terminal import *

nets=[]

print('WIFI BRUTEFORCER BLYAD')
print('type help to help or smthng idk')


docs=[x for x in open('doc.txt')]
while True:
    cmd=input()

    if cmd[:3]=='add':
        nets.append(add_net(cmd))

    if cmd=='exit':
        print('exiting the programm...')
        time.sleep(1)
        break

    if cmd=='disconnect':
        Wifi.disconnect()

    if cmd[:7] == 'connect':
        connect_net(cmd,nets)

    if cmd=='avilable':
        show_nets(nets)

    if cmd=='help':
        for x in docs:
            print(x)


    if cmd[:4]=='hack':
        hack(nets,cmd)












