#coding:utf-8
#author:liming
#desc:server register etcd info
#2017-03-01

import socket
import fcntl
import struct
import sys,os
import requests, json
import ConfigParser

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def readConfig(config_file_path):
    cf = ConfigParser.ConfigParser()
    cf.read(config_file_path)
    etcdHost = cf.get("etcdconf","ip")
    etcdPort = cf.get("etcdconf","port")
    serverPort = cf.get("serverconf","port")
    print etcdHost, etcdPort, serverPort

print get_ip_address('eth0')
print socket.gethostname()
readConfig("../etcd_config.ini")
