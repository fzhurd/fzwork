#!/bin/bash  
echo "Please enter a user:"  
read a  
b=$(whoami)  
if test $a = $b  
then echo "the user is running."  
else echo "the user is not running."  
fi  