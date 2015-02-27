#!/bin/bash  
cd /usr/local/mysql/bin
for i in *
do ln /usr/local/mysql/bin/$i /usr/bin/$i
done


# check ps number
ps aux | wc -l