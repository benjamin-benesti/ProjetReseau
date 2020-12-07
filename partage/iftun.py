#!/usr/bin/env python
import fcntl
import os
import struct
import subprocess
import socket
import sys

def createTun():
    print("Creation de tun0")
    TUNSETIFF = 0x400454ca
    IFF_TUN = 0x0001
    IFF_TAP = 0x0002
    IFF_NO_PI = 0x1000

    tun = open('/dev/net/tun', 'r+b')
    ifr = struct.pack('16sH', 'tun0', IFF_TUN )
    fcntl.ioctl(tun, TUNSETIFF, ifr)
    return tun;

def rwPacket(tuna):
    ficsrc  = os.fdopen(tun.fileno(),"r")
    ficdest = os.fdopen(1,"w")
    while(1):
        recopie = ficsrc.read(200)
        ficdest.write(recopie)
