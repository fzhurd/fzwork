#!/bin/bash  

directory=/usr/bin/

fstring="Free Software Foundation" 

for file in $( find $directory -type f -name '*' | sort )
do
	strings -f $file | grep "$fstring" | sed -e "s%$directory%%"

done