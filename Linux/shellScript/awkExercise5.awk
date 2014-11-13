
#! /bin/awk -f

awk -F '|' '{print $1}'  file1.txt >file2.txt

awk '$1=$1' file2.txt > file3.txt