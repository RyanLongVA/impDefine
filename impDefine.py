#!/usr/bin/env python
import socket, sys, os, requests, pdb, optparse
import multiprocessing as mp
def main():
    parser = optparse.OptionParser('python impDefine.py' + ' -i <input link list> -s "<string to look for>" *optional* -s "<second string>"')
    parser.add_option('-i', dest='iListName', type='string', help='input link list')
    parser.add_option('-s', dest='fString', type='string', help='provide what to look for', action='append')
    global options
    (options, args) = parser.parse_args(sys.argv[1:])
    if (options.iListName == None) | (options.fString == None):
        print parser.usage
        exit(0)
    clist = filter(None, [clist.replace('\n', '') for clist in open(options.iListName, "r").readlines()])
    cleanList = []
    pool = mp.Pool(mp.cpu_count())
    cleanList += filter(None, pool.map(startList, clist))
    pool.close()
def searchRes(respCont):
    #Here -- Goal
    for c in options.fString:
        if c in respCont:
            return False
            break
    return True


def startList(a):
    try:
        response = sslConnect(a)
        if searchRes(response.content):
            print '[+] %s, clean'%(a)
            return a
        else:
            print '[-] %s, dirty'%(a)
    except requests.ConnectionError:
        print '[-] %s, timeout error'%(a)

def sslConnect(domain):
    connection = requests.get(domain, timeout=3); return connection

#Going to have to step through manually to get through to the goal b/c of multiprocessing
if __name__=="__main__":
    main()
