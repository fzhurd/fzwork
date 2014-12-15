#!/bin/bash  
while :  
do  
    echo "please input file's name:"  
    read a  
    if test -e /root/$a  
    then  
         echo "the file is existing Please input new file name:"  
    else  
        mkdir $a  
        echo "you aye sussesful!"  
        break   
    fi  
done  