#!/bin/bash  
clear  
echo "enter [y/n]:"  
read a  
case $a in  
    y|Y|Yes|YES) echo "you enter $a"  
    ;;  
    n|N|NO|no) echo "you enter $a"  
    ;;  
    *) echo "error"  
    ;;  
esac  