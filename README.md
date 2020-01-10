# :snake: Python Programs :snake:
 > A list of python projects created while learning the language as it relates to ethical hacking and cyber security. Most tools work as is, some need to be converted to python3 and there is a full TODO list as well for each one. This list is not conclusive nor complete, and more projects will be added as I get them completed and operational.
---
## Contents
- [Python DNS Spoofer](#dns-spoofer)
- [Man in the Middle (MITM) File Interceptor](#interceptor)
- [MAC Address Changer](#mac-changer)
- [Network Scanner](#net-scanner)
- [Port Scanner](#port-scanner)
- [WebApp Login Cracker](#login-cracker)
- [Webpage Spider](#web-spider)
- [TODOs](#todo)

---
<a name="dns-spoofer"></a>
### Python DNS Spoofer

Simple python program to spoof DNS

Usage:  
`python dns_spoof.py`

---
<a name="interceptor"></a>
### MITM File Download Interceptor

Usage:  
`python3 dl_intercept.py`

Works via the following steps:  
1. Monitor network traffic for seq/ack transmit data across HTTP traffic
2. If found, check raw packet for common document file types
3. If found, modify raw load to redirect victim to malicious site & download
  
Supported doc types
* .exe  
---
<a name="mac-changer"></a>
### MAC Address Changers

simple_mac_changer usage:  
`python3 simple_mac_changer.py <interface> <MAC>`  
- user provides interface and what MAC to set manually *no input validation*  

mac_changer usage:  
`python3 mac_changer.py -i interface`
* generates random hex MAC value
* more verbosity on process

---
<a name="net-scanner"></a>
### Network Scanner

Usage:  
`python3 netscan.py -t ip/subnet`

Will return Responding IP and MAC Address of the scanned network range

---
<a name="port-scanner"></a>
### Port Scanner

Usage:  
`python portscan.py <ip>`

Scans the top 1000 ports and returns ports found open

---
<a name="login-cracker"></a>
### Python WebApp Login Cracker

A simple login page cracker using a supplied username and wordlist file for passwords.  

Usage:  
`python login_cracker.py -t TARGET -u USER -w WORDLIST`
  
The output will only generate if a password is found for the supplied username *does not verbose all attempted passwords*  
`[+] Login found --> password`  
  
If no password is found to match the username supplied:    
`[-] End of file reached - no password found`  

---
<a name="web-spider"></a>
### Python Webpage Spider

A simple python script to crawl a website and output all URLs located

Usage:  
`python web_spider.py -t TARGET`
 
The output will generate all links located on the target site *example below is IP of metasplotable*  
```
python main.py -t http://10.10.20.131/
http://10.10.20.131/twiki/
http://10.10.20.131/phpMyAdmin/
http://10.10.20.131/mutillidae/
http://10.10.20.131/dvwa/
http://10.10.20.131/dav/
```
---
<a name="todo"></a> 
## TODOs:

- Update to python3 needed
    - DNS Spoofer
    - Port Scanner
    - WebApp Login Cracker
    - Web Spider

- File Interceptor
    - Planned doc types
        * .pdf
        * .doc / .docx
        * .xls / .xlsx        
        * .csv
        * *others*

- Network Scanner
    - Obtain host info
    - Add port scanning within the script
    - Obtain port service informaiton like nmap once included
    - Add execution for simple exploit checks (anon FTP, SSH enum, SMB mapping, rpcclient, etc)

- Login Cracker
    - Argument to accept username file
    - Try all options with supplied user/pass files not locating first successful login
    - Support for : separated files (user:pass)

- Web Spider
    - Get recursive working to click-thru and pull all links that can be located
    - Output in a cleaner format
    - Highligh of import URLs found (e.g. login, admin, etc.)
    - Incorporate into a vuln scanner script using lists of important URLs found
    - Commented code within script to incorporate scanning for subdomains still needs to be worked out (e.g. subdomain.domain.com)

