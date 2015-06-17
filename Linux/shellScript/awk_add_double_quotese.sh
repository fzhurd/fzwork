#! /bin/awk -f

awk -F ',' '{print $1,$2,$3,$4,"\""$5"\""}' col2.csv >col2b.csv