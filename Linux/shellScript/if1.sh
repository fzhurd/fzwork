#!/bin/bash 
 
a=5;if [[ a -gt 4 ]] ;then echo 'ok';fi;


scores=40;
if [[ $scores -gt 90 ]]; then
 echo "very good!";
elif [[ $scores -gt 80 ]]; then
 echo "good!";
elif [[ $scores -gt 60 ]]; then
 echo "pass!";
else
 echo "no pass!";
fi;