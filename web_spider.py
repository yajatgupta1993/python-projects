# Author: Mystik Developed
#
# Date: 1/3/2019 
#
# Scan a target website
#
#!/usr/bin/env python

#reqs
import requests
import re
import urlparse
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

    # parser.add_argument(
    #   "-w",
    #   "--wordlist",
    #   dest="wordlist",
    #   help="Wordlist to use")

    options = parser.parse_args()

    # verify arguments
    if not options.target:
        parser.error("[-] No URL provided. See --help for more info")
    elif not options.wordlist:
        parser.error("[-] No wordlist provided. See --help for more info")
    else:
        return options


options = getArgs()
target_url = options.target
# wordlist = options.wordlist
target_links = []


def extract_links(url):
    res = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', res.content)

def crawl(url):
    href_links = extract_links(target_url)
    for link in href_links:
        link = urlparse.urljoin(target_url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)


crawl(target_url)

# #subdomain list
# subdom_list = []
#
# #check for subdomains
# def subdom_check(url):
#   try:
#     with open(wordlist, "r") as wordlist:
#       for line in wordlist:
#         word = line.strip()
#         test_subdom = word + "." + target_url
#         res = subdom_check(test_subdom)
#         if res:
#           subdom_dict = {"subdomain": test_subdom, "res": res}
#           print("[+] Subdomain --> " + test_subdom)
#           subdom_list.append(subdom_dict)
#   except requests.exceptions.ConnectionError:
#     pass
#
#
# def subdom_results(results_list):
#   print("\tSubdomain\t\t\tResponse Code\n-------------------------------------")
#
#   for domain in results_list:
#     print("\t" + domain["subdomain"] + "\t\t" + domain["res"])
