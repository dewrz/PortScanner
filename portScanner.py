from scapy.all import *
import ipaddress

ports = [22, 25, 80, 139, 443, 445, 8080]

host_address = []

with open("ip.txt") as ip_list:
    for ip in ip_list:
        ip = ip.strip()
        host_address.append(ip)

def SynScan(host_address):
    ans,unans = sr(IP(dst=host_address)
                   /TCP(sport=33333,dport=ports,
                        flag="S"),timeout=2,verbose=0)
    print("Open ports at %s:" % host_address)
    for (s,r,) in ans:
        if s[TCP].dport == r[TCP].flags=="SA":
            print(s[TCP].dport)

try:
    ipaddress.ip_address(host_address)
except:
    print("Invalid IP Address")
    exit(-1)

SynScan(host_address)
