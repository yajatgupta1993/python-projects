# Author: Mystik Developed
#
# Date: 1/2/2019 
#
# Program: Mystik Developed netscan.py
#
# Language: python
#
# Functionality: This python script is used to
# scan a network for a given IP range and subnet
# and locate any hosts on the network - returning
# the values in a table displaying IP and MAC
# address of any host found on the network
#
#!/usr/bin/env python

#requirements
import scapy.all as scapy
import argparse
import sys
import socket

def getArgs():
    parser = argparse.ArgumentParser()  #argparse intialize

    #Obtain target range to scan
    parser.add_argument(
        "-t",
        "--target",
        dest="target",
        help="Target IP Range to scan. Example: 192.168.12.1/24"    )

    options = parser.parse_args()


    #verify arguments
    if not options.target:
        parser.error("[-] No starting IP address provided. See --help for more info")
    else:
      return options

    return options


def scan(ip):
  arp_request = scapy.ARP(pdst=ip)
  broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
  arp_broadcast = broadcast/arp_request
  ans_list, unans_list = scapy.srp(arp_broadcast, timeout=1, verbose=False)

  hosts_list = []

  for answer in ans_list:
    hosts_dict = {"ip": answer[1].psrc, "mac": answer[1].hwsrc}
    hosts_list.append(hosts_dict)

  return hosts_list

def port_scan(results_list):
  print('-' * 65)
  print("\t\tBeginning port scan on found hosts")
  print('-' * 65)

  # for host in results_list:
  #   ports_results_list = []
  #   for port in range(1,21):
        
  #       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  #       socket.setdefaulttimeout(1)
  #       result = s.connect_ex((host,port))
        
  #       if result == 0:
  #           print("Port {} is open".format(port))
  #           ports_dict = {"ip": host, "port": port}
  #           ports_results_list.append(ports_dict)
  #           s.close()
  #           return ports_results_list


def host_results(results_list):
  print('-' * 65)
  print("\tResponding IP\t\t\tResponding MAC Address")
  print('-' * 65)

  for host in results_list:
    print("\t" + host["ip"] + "\t\t\t" + host["mac"])
  
def ports_results(portresults_list):
  for port in portresults_list:
    print("Ports Open on IP")
  

options = getArgs()
scan_result = scan(options.target)
host_results(scan_result)
port_scan(scan_result)
