#!/bin/bash  

word=Linux
letter_sequence=inu

if echo "$word" | grep -q "$letter_sequence"
	then
	echo "$letter_sequence found in word $word"
else
	echo  "$letter_sequence not found in word $word"

fi


directory=${l-`pwd`}

echo "symbolic links in directory \"$directory\""

for file in "$( find $directory -type l )"
do
	echo "$file"

done | sort


ROOT_UID=0 

if [ "$UID" -eq "$ROOT_UID" ] 
	then
	echo "You are root."
else
	echo "You are just an ordinary user "
fi