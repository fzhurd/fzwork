
#! /bin/awk -f

awk -F '|' '{print $1, $2}'  fields_origin.txt > fields1

cat  ebsco_fields1 | tr -s ' ' >  fields12
awk '{print $0, ","}' fields12 > fields15
awk '{print $0 ","}' fields12 > fields16

awk '{print "\""$1"\"", $2 $3}' fields16 >ebsco_fields17