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

##Configuration de VM3

##LAN2
eth1:
  network.managed:
    - enabled: True
    - type: eth
    - proto: none
    - enable_ipv4: true
    - ipv6proto: static
    - enable_ipv6: false
    - ipv6_autoconf: no
    - ipaddr: 172.16.2.163
    - netmask: 28


##LAN4-6
eth2:
  network.managed:
    - enabled: True
    - type: eth
    - proto: none
    - enable_ipv4: false
    - ipv6proto: static
    - enable_ipv6: true
    - ipv6_autoconf: no
    - ipv6ipaddr: fc00:1234:4::3
    - ipv6netmask: 64    

## Configuration de la route vers LAN2 via VM2
routes1:
  network.routes:
    - name: eth1
    - routes:
      - name: LAN2
        ipaddr: 172.16.2.128/28    
        gateway: 172.16.2.162

routes2:
  network.routes:
    - name: eth2
    - routes:
      - name: LAN2-6
        ipaddr: fc00:1234:2::/64
        gateway: fc00:1234:4::36
      - name: LAN1-6
        ipaddr: fc00:1234:1::/64
        gateway: fc00:1234:4::36
      - name: LAN3-6
        ipaddr: fc00:1234:3::/64
        gateway: fc00:1234:4::36


