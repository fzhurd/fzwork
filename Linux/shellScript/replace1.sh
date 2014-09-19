#!/bin/bash  

directory = /usr/bin

fs = "Free Software Foundation"

for f $( find $directory -type f -name '*' | sort )
do
	strings -f $file | grep "$fstring" | sed -e "s%$directory%%"
done
