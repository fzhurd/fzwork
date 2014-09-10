#!/bin/bash  

colls=( t1.json t2.json t3.json  )

for c in ${colls[@]}
do
  mongoimport -h localhost:27017 -d myDatabase -c myCollection  --jsonArray < $c

done