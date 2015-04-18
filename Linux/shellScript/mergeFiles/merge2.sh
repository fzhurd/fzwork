#!/bin/bash 
exec 3< file1.txt 
exec 4< file2.txt 
while : 
do 
	read x <&3 
	read y <&4 
	[ -n "$x" ] && echo $x 
	[ -n "$y" ] && echo $y 
	[ -z "$x" -a -z "$y" ] && break 
done 