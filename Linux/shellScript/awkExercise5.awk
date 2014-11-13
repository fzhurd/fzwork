
#! /bin/awk -f

awk -F '|' '{print $1}'  file1.txt >file2.txt

#remove the head and tail white space
awk '$1=$1' file2.txt > file3.txt

awk -F '|' '{print $1, $2}' f1.txt > f2.txt

#add double quotes for the line
awk -F '|' '{print "\""$1"\"", $2}' f1.txt > f2.txt


awk  '{print "\""$1"\""}' f1.txt > f2.txt