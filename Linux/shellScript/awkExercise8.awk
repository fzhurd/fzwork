
#! /bin/awk -f

# select 1st and 2nd fields
awk -F '|' '{print $1, $2}'  fields_origin.txt > fields1


# remove white space
cat  ebsco_fields1 | tr -s ' ' >  fields12

# add comma
awk '{print $0 ","}' fields12 > fields16

# add double quote
awk '{print "\""$1"\"", $2 $3}' fields16 >ebsco_fields17