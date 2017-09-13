#!/usr/bin/env python
import socket, sys, os, requests, pdb

def main():
    list = filter(None, [list.replace('\n', '') for list in open("start.links", "r").readlines()])
    cleanList = []
    for a in list:
        try:
            response = sslConnect(a)
        except requests.ConnectionError:
            print '[-] %s, timeout error'%(a)
            continue
        #print response
        if "Path not supported" not in response.content:
            print '[+] %s, clean'%(a)
            cleanList.append(a)
        else:
            print '[-] %s, dirty'%(a)
        #sslConnect(domain, directory)
        #if response.status blah blah

#def prefixRemoval(link):
#    if link.startswith("https://"): return link[8:]
#    return link[7:] if link.startswith("http://") else link

def sslConnect(domain):
    connection = requests.get(domain, timeout=3); return connection

#test = sslConnect(sys.argv[1], sys.argv[2])
#print test
main()
