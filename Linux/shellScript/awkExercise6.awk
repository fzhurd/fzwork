
#! /bin/awk -f

 echo "1:2:3" | awk -F: '{print $1 " and " $2 " and " $3}'

 echo | awk -v a=1 'BEGIN {print a}'

awk 'BEGIN {print "BEGIN: " var} {print "PROCESS: " var} \
END {print "END: " var }' var=1 a