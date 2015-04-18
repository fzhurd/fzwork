#!/bin/bash 
exec 3< file1.txt 
exec 4< file2.txt 
exec 5< file3.txt
while : 
do 
	read x <&3 
	read y <&4 
	read z <&5
	[ -n "$x" ] && echo $x 
	[ -n "$y" ] && echo $y 
	[ -n "$z" ] && echo $z
	[ -z "$x" -a -z "$y" -a -z "$z" ] && break 
done 