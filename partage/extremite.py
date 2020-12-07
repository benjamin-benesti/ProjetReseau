# coding: utf-8
import socket
import os
import time


def ext_out(adresse,port,tun):	
    sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #print(adresse)
    sc.bind((adresse,port))
    sc.listen(2)
    client,adresse = sc.accept()
    print("client" , adresse," connecté")
    fictun = os.fdopen(tun.fileno(),"w")
    while True:
        reponse = client.recv(255)
        os.write(tun.fileno(),reponse)
        print(reponse)
    client.close()
    sc.close()

def ext_in(adresse,port,tun):
    soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
    	soc.connect((adresse,port))
    	print("connecté")
    	tunfic = os.fdopen(tun.fileno(),"r")
    	while True:
        	transfert = tunfic.read(200)
        	soc.send(transfert)
    except socket.error:
    	print("tentative de nouvelle connexion")
    	time.sleep(5)
    	ext_in(adresse,port,tun)
