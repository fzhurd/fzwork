
#! /bin/awk -f

# select 1st and 2nd fields
awk -F '|' '{print $1, $2}'  fields_origin.txt > fields1


# remove white space
cat  ebsco_fields1 | tr -s ' ' >  fields12

# add comma
awk '{print $0 ","}' fields12 > fields16

# add double quote
awk '{print "\""$1"\"", $2 $3}' fields16 >ebsco_fields17

#########################################################

awk '$3 >0 { print $1, $2 * $3 }' emp.data

awk ‘$3 == 0 { print $1 }’ emp.data

{ print NF, $1, $NF }

################################################################

start=1;
 
total=0;
 
while [ $start -le 1000 ];do
 
    [[ $(($start%2)) == 0 ]]&&total=$(($total+$start));
 
   start=$(($start+1));
 
done;
 
echo $total;

####################################################################
start=0;
 
total=0;
 
for i in $(seq $start 2 1000); do
 
    total=$(($total+$i));
 
done;
 
echo $total;

#######################################################################3