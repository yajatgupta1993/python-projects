# Author: Mystik Developed
#
# Date: 1/4/2019 
#
# Functionality: This python script is used to
# edit a network interface MAC address with a 
# user supplied interface and MAC address
#
#!/usr/bin/env python
#import requirements
import subprocess

#get user input for interface and mac to change to
interface = input("Interface > ")
usrMAC = input("MAC Address > ")

#notify user 
print("[+] Changing MAC Address for interface " + interface + " to MAC " +
      usrMAC)

#call subprocess to execute ifconfig in shell to take wlan0 down
subprocess.call(["ifconfig", interface, "down"])

#edit mac address of interface
subprocess.call(["ifconfig", interface, "hw", "ether", usrMAC])

#bring wlan0 back online 
subprocess.call(["ifconfig", interface, "up"])
