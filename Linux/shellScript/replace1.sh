#!/bin/bash  

directory=/usr/bin

fs="Free Software Foundation"

for f in $( find $directory -type f -name 'l*' | sort )
do
	#strings -f $file | grep "$fstring" | sed -e "s%$directory%%"
	echo $f
done
