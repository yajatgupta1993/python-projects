# Author: Mystik Developed
#
# Date: 12/28/2019 
#
# Functionality: This python script is used to
# generate a random mac address for a given interface
# supplied by the user and change the mac address
#
#!/usr/bin/env python

#Requirements
import random
import subprocess
import argparse
import re


#Validate args on execution
def getArgs():
    parser = argparse.ArgumentParser()  #argparse intialize

    #Obtain interface
    parser.add_argument(
        "-i",
        "--interface",
        dest="interface",
        help="Interface for MAC Address Change - e.g. wlan0")

    options = parser.parse_args()

    #verify arguments
    if not options.interface:
        parser.error("[-] No interface supplied. See --help for more info")

    return options


#Generate random valid MAC
def hex(length):  #Validate HEX
    return ''.join(random.choice('0123456789ABCDEF') for _ in range(length))


def genMAC():  #Generates the MAC address
    print("[+] Generating Random MAC Address")
    rnd_mac = '00' + ':' + hex(2) + ':' + hex(2) + ':' + hex(2) + ':' + hex(
        2) + ':' + hex(2)
    print("[+] Random MAC is:  " + rnd_mac)
    return rnd_mac


#Changing interface MAC address
def chgMAC(interface):
        print("[+] Changing MAC Address for interface " + interface +
              " to randomly generated MAC: " + rnd_mac)
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", rnd_mac])
        subprocess.call(["ifconfig", interface, "up"])


#Get current mac address
def getCurrentMAC(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface]).decode()
    mac_verify = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)

    if mac_verify:
        return mac_verify.group(0)
    else:
        print("[-] Could not read MAC address")
        return

#Exec program, verify args exist, and display current MAC address
options = getArgs()
currentMAC = getCurrentMAC(options.interface)
print("[+] Current MAC Address = " + str(currentMAC))
rnd_mac = genMAC()

#Call MAC address change
chgMAC(options.interface)

#Verify MAC changed successfully
changedMAC = getCurrentMAC(options.interface)
if changedMAC.lower() == rnd_mac.lower():
    print("[+] MAC Address successfully changed!")
else:
    print("[-] MAC Address was not changed.")
