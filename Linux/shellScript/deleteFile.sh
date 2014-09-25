#!/bin/bash  
for filename in `ls`  
do  
    if test -d $filename  
    then b=0  
    else      
       a=$(ls -l $filename | awk '{ print $5 }')  
            if test $a -eq 0  
             then rm $filename  
             fi  
        fi        
done  