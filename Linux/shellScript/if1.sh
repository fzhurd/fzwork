#!/bin/bash 
 
a=5;if [[ a -gt 4 ]] ;then echo 'ok';fi;


scores=40;
if [[ $scores -gt 90 ]]; then
 echo "very good!";
elif [[ $scores -gt 80 ]]; then
 echo "good!";
elif [[ $scores -gt 60 ]]; then
 echo "pass!";
else
 echo "no pass!";
fi;


##########################################################


for i in $(seq 10); do
 echo $i;
done;

#################################################################

for((i=1;i<=10;i++));do
 echo $i;
done;

#############################################################

i=10;
while [[ $i -gt 5 ]];do
 echo $i;
 ((i--));
done;

####################################################################

while read line;do
 echo $line;
done < /etc/hosts;