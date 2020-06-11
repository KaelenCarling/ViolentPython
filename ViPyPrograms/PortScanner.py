import optparse
import socket
from socket import *


def connectionScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)

        print('%d/tcp open' % tgtPort)
        print(str(results))

        connSkt.close()
    except:
        print('%d/tcp closed' % tgtPort)


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("Cannot resolve '%s': Unkown host" % tgtHost)
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\nScan Results for: ' + tgtName[0])
    except:
        print('\nScan Results for: ' + tgtIP)

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning Ports ' + tgtPort)
        connectionScan(tgtHost, int(tgtPort))


def main():
    parser = optparse.OptionParser('usage: %prog -H <target host> -p <target port>')

    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='int', help='specify target port')

    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(', ')

    if (tgtHost is None) | (tgtPorts is None):
        print('Please specify a target host and at least 1 port')
        exit(0)

    portScan(tgtHost, tgtPorts)


if __name__ == '__main__':
    main()
