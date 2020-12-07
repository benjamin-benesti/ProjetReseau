import extremite as ext
import iftun as it
import subprocess
import sys
from multiprocessing import Process




def server_client(adresse1,port1,adresse2,port2,mode):
    tun = it.createTun()
    subprocess.check_call("sh configure-tun.sh",shell=True)
    if(int(mode) == 1):
    	Thread1 = Process(target=ext.ext_out,args=(adresse1,int(port1),tun))
    	Thread2 = Process(target=ext.ext_in,args=(adresse2,int(port2),tun))
    	Thread1.start()
    	Thread2.start()
    	Thread1.join()
    	Thread2.join()
    else:
    	Thread1 = Process(target=ext.ext_out,args=(str(adresse2),int(port2),tun))
    	Thread2 = Process(target=ext.ext_in,args=(str(adresse1),int(port1),tun))
    	Thread1.start()
    	Thread2.start()
    	Thread1.join()
    	Thread2.join()
    	

#server_client(sys.argv[1],sys.argv[2],sys.argv[4],sys.argv[5],sys.argv[6])
