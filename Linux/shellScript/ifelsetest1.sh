#!/bin/bash  

word=Linux
letter_sequence=inu

if echo "$word" | grep -q "$letter_sequence"
	then
	echo "$letter_sequence found in word $word"
else
	echo  "$letter_sequence not found in word $word"

fi


directory=${1-`pwd`}

echo "symbolic links in directory \"$directory\""

for file in "$( find $directory -type l )"
do
	echo "$file"

done | sort