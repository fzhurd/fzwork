#!/bin/bash  
test -e a.c  
while read line  
do  
  a=$(($line+1))  
done < a.c  
echo $a  