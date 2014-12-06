#!/bin/bash  
colls=( mycollection1 mycollection2 mycollection3 )

for c in ${colls[@]}
do
	mongodump -d mydb -c $c
done