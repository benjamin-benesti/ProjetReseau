import createTun from iftun
import rwPacket from iftun


tun = createTun()
subprocess.check_call("sh configure-tun.sh",shell=True)
rwPacket(tun)
