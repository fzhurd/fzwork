#!/bin/bash  
tcp: netstat -an|egrep $1 |awk '$6 == "LISTEN" && $1 == "tcp" {print $0}'
udp: netstat -an|egrep $1 |awk '$1 == "udp" && $5 == "0.0.0.0:*" {print $0}'