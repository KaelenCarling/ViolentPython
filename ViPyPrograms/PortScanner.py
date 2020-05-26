import optparse
from socket import *


def connectionScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        print('%d/tcp open' % tgtPort)
        connSkt.close()
    except:
        print('%d/tcp closed' % tgtPort)

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("Cannot resolve '%s': Unkown host"%tgtHost)

    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n Scan Results for: ' + tgtName[0])
    except:
        print('\n Scan Results for: ' + tgtIP)

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
    tgtPort = options.tgtPort

    if (tgtHost is None) | (tgtPort is None):
        print(parser.usage)
        exit(0)


if __name__ == '__main__':
    main()
