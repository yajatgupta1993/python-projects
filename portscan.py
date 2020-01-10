# Author: Mystik Developed
#
# Date: 12/28/2019 
#
# Functionality: This python script is a simple
# port scanner for a provided host IP address arg
# It's functionality is limited but was to give
# an idea of what needs to be incorporated into
# netscan.py to achieve port scanning. 
# 
# Hard coded to scan ports 1 - 1000, could be edited 
# to accept a port range argument.
#
#!/usr/bin/env python

import sys
import socket

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("No IP to scan provided.")
    print("Use python3 portscan.py <ip>")

try:
    print("-" * 40)
    print("\tScanning 1000 ports\n   Closed ports will not be verbosed")
    print("-" * 40)
    
    for port in range(1,1001):
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
