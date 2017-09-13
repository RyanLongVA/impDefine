#!/usr/bin/env python
import socket, sys, os, requests, pdb
import multiprocessing as mp
def main():
    clist = filter(None, [clist.replace('\n', '') for clist in open("start.links", "r").readlines()])
    cleanList = []
    pool = mp.Pool(4)
    cleanList += filter(None, pool.map(startList, clist))
    pool.close()

def startList(a):
    try:
        response = sslConnect(a)
        if "Path not supported" not in response.content:
            print '[+] %s, clean'%(a)
            return a
        else:
            print '[-] %s, dirty'%(a)
    except requests.ConnectionError:
        print '[-] %s, timeout error'%(a)

def sslConnect(domain):
    connection = requests.get(domain, timeout=3); return connection

if __name__=="__main__":
    main()
#test = sslConnect(sys.argv[1], sys.argv[2])
#print test
