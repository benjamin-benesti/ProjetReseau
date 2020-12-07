import iftun as it
import extremite as ext
import sys
import subprocess

def client(adresse,tun):
    #tun = open('/dev/net/tun', 'r+b')#it.createTun()
    #subprocess.check_call("sh configure-tun.sh",shell=True)
    ext.ext_in(str(adresse),int(tun))



client(sys.argv[1],sys.argv[2])
