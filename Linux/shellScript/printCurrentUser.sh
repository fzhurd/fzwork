#!/bin/bash  
echo "Current User is :"  
echo $(ps | grep "$$" | awk '{print $2}')  