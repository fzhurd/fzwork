#!/bin/bash  
p_num ()  
{  
    num=$1  
    echo $num  
}  
for n in $@  
do  
    p_num $n  
done 