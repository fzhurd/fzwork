#!/bin/bash  
awk -F '|' '{print $1}' tweetsfields1 > tweetsfields2
awk '{print $1=$1}' tweetsfields2 >tweetsfields3
awk '{print "\""$1"\""}' tweetsfields3 >tweetsfields4

awk '{print $1, ","}' tweetsfields4 > tweetsfields5

awk '{{printf"%s",$0}}' tweetsfields5 > tweetsfields6

cat tweetsfields5 | xargs echo