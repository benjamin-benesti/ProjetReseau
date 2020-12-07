# Configuration eth1
# RAPPEL: eth0 est à vagrant, ne pas y toucher

## Désactivation de network-manager
NetworkManager:
  service:
    - dead
    - enable: False
    
## Suppression de la passerelle par défaut
ip route del default:
  cmd:
   - run

##Configuration de VM2 LAN1
eth1:
  network.managed:
    - enabled: True
    - type: eth
    - proto: none
    - enable_ipv4: true
    - ipv6proto: static
    - enable_ipv6: false
    - ipv4_autoconf: no
    - ipaddr: 172.16.2.132
    - netmask: 28

##Configuration de VM2 LAN2
eth2:
  network.managed:
    - enabled: True
    - type: eth
    - proto: none
    - enable_ipv4: true
    - ipv6proto: static
    - enable_ipv6: false
    - ipv4_autoconf: no
    - ipaddr: 172.16.2.162
    - netmask: 28


net.ipv4.ip_forward:
  sysctl:
    - present
    - value: 1
