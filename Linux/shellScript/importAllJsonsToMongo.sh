#!/bin/bash  
ls -1 *.json | sed 's/.json$//' | while read col; do 
    mongoimport -d database --port 27017 -c collection < $col.json; 
done 