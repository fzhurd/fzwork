#!/bin/bash  
clear  
echo "enter a number from 1 to 5:"  
read num  
case $num in  
    1) echo "you enter 1"  
    ;;  
    2) echo "you enter 2"  
    ;;  
    3) echo "you enter 3"  
    ;;  
    4) echo "you enter 4"  
    ;;  
    5) echo "you enter 5"  
    ;;  
    *) echo "error"  
    ;;  
esac    