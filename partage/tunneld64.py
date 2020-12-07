import server_client as sc
import sys

def config(file):
    file = open(file, "r")
    line = file.readline()
    while line:
        if line.startswith("inip"):
            x = line.split("=")
            addrIn = x[1]
        elif line.startswith("inport"):
            x = line.split("=")
            portIn = int(x[1])
        elif line.startswith("outip"):
            x = line.split("=")
            addrOut = x[1]
        elif line.startswith("outport"):
            x = line.split("=")
            portOut = int(x[1])

        line = file.readline()
    file.close()

    sc.server_client(addrIn,portIn,addrOut,portOut,1)

config(sys.argv[1])
