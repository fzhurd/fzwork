#!/bin/bash  
echo "No Password User are :"  
echo $(cat /etc/shadow | grep "!!" | awk 'BEGIN { FS=":" }{print $1}')  