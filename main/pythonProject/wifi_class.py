import sys
import time
import os
import binascii
import socket


class Wifi:

    def __init__(self,ssid,key='00000000',valid=0):
        self.ssid=ssid
        self.__key=key
        self.valid=0
        self.createNewConnection(self.ssid,self.ssid,self.key)

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self,x):
        self.__key = x
        command = f'netsh wlan set profileparameter name="{self.ssid}" keyMaterial="' + x + '" >nul 2>&1'
        os.system(command)

    @classmethod
    def is_connected(cls):
        time.sleep(1)
        try:
            sock = socket.create_connection(('1.1.1.1', 80))
            if sock is not None:
                sock.close()
            return True
        except OSError:
            pass
        return False

    @classmethod
    def disconnect(cls):
        os.system("netsh wlan disconnect  >nul 2>&1")
        print('disconnected')

    def connect(self):
        command = f'netsh wlan connect name={self.ssid}' + ' >nul 2>&1'
        os.system(command)

    @classmethod
    def createNewConnection(cls,name, SSID, password='00000000'):
        t = bytes(name, "cp1251")
        config = """<?xml version=\"1.0\"?>
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>""" + name + """</name>
        <SSIDConfig>
            <SSID>
                <hex>""" + str(binascii.hexlify(t))[2:-1] + """</hex>
                <name>""" + SSID + """</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>manual</connectionMode>
        <MSM>
            <security>
                <authEncryption>
                    <authentication>WPA2PSK</authentication>
                    <encryption>AES</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>""" + password + """</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
    </WLANProfile>"""
        command = 'netsh wlan add profile filename="' + name + '.xml" user=all' + ' >nul 2>&1'
        with open(name + ".xml", 'w') as file:
            file.write(config)
        os.system(command)






