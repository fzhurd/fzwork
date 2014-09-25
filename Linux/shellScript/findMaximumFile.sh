#!/bin/bash  
a=0  
for  name in *.*  
do  
    b=$(ls -l $name | awk '{print $5}')  
    if test $b -gt $a  
    then a=$b  
    namemax=$name  
    fi  
done  
echo "the max file is $namemax" 