#!/bin/bash  
tcp: netstat -an|egrep $1 |awk '$6 == "LISTEN" && $1 == "tcp" {print $0}'
udp: netstat -an|egrep $1 |awk '$1 == "udp" && $5 == "0.0.0.0:*" {print $0}'


function GetSysCPU
{
 CpuIdle=`vmstat 1 5 |sed -n '3,$p' \n
 |awk '{x = x + $15} END {print x/5}' |awk -F. '{print $1}'
 CpuNum=`echo "100-$CpuIdle" | bc`
 echo $CpuNum
}