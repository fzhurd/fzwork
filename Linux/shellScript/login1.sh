#!/bin/bash
echo -n "login:"   
read name  
echo -n "password:"  
read passwd  
if [ $name = "cht" -a $passwd = "abc" ];then  
echo "the host and password is right!"  
else echo "input is error!"  
fi  