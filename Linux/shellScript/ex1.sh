#!/bin/bash  
echo "pleas input a integer:"
read score

echo $score

if [ "$score" -lt 0 -o "$score" -gt 100 ]
	then echo "the score what you inpt is not integer or the is not in 0 and 100"
elif [ "$score" -ge 90 ]
	then echo "A"

fi