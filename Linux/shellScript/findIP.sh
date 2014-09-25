#!/bin/bash  
ifconfig | grep "inet addr:" | awk '{ print $2 }'| sed 's/addr://g'  