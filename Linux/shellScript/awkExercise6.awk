
#! /bin/awk -f

 echo "1:2:3" | awk -F: '{print $1 " and " $2 " and " $3}'