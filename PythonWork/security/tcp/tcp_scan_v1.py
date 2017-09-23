#!/usr/bin/python
# -*- coding: utf-8 -*-


import optparse
from socket import *

def conn_scan(tgt_host, tgt_port):
    try:
        conn_skt=socket(AF_INET, SOCK_STREAM)
        conn_skt.connect(tgt_host, tgt_port)
        print tgt_port
    except:
        print tgt_port

def port_scan(tgt_host, tgt_ports):
    try:
        tgtIP=gethostbyname(tgt_host)
    except:
        print 'unknow host: '+ tgt_host
        return

    try:
        tgt_name=gethostbyaddr(tgtIP)
        print 'scan results for: '+ tgt_name[0]
    except:
        print 'scan results for: '+ tgtIP

    setdefaulttimeout[1]

    for tgt_port in tgt_ports:
        print 'Scanning port '+ tgt_port
        conn_scan(tgt_host, int(tgt_port))


def main():
    parser = optparse.OptionParser("usage%prog"+"-H <target host> -p <target port>")
    parser.add_option('-H', dest='tgt_host', type='string', help='specify target host')
    parser.add_option('-p', dest='tgt_port', type='string', help='specify taget ports separate by comma')

    (options, args) = parser.parse_args()
    tgt_host=options.tgt_host
    tgt_ports=str(options.tgt_port).split(',')

    if (tgt_host==None) | (tgt_ports[0]==None):
        print '[-] You must specify a target host and ports'
        exit (0)

    port_scan(tgt_host, tgt_ports)


if __name__ == '__main__':
    main()