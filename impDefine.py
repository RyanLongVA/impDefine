import socket, sys, os, httplib

def main():
    list = filter(None, [list.replace('\n', '') for list in open("start.links", "r").readlines()])
    print list
def sslConnect(domain, directory):
    connection = httplib.HTTPSConnection(domain)
    connection.request("GET", directory)
    response = connection.getresponse()
    return str(response.status) + '\n' + response.reason + '\n' + response.read()

#test = sslConnect(sys.argv[1], sys.argv[2])
#print test
main()
