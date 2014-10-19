
#! /bin/awk -f

# awk array
 awk  'BEGIN { print split("123#45678#9", ar, "#")} '


 #exercise 2

BEGIN {
record="123#45#678#9"; 
split(record, ar2, "#")} 
	END {for (i in ar2) {print ar2[i]}}