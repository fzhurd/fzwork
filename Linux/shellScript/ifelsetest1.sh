#!/bin/bash  

word=Linux
letter_sequence=inu

if echo "$word" | grep -q "$letter_sequence"
	then
	echo "$letter_sequence found in word $word"
else
	echo  "$letter_sequence not found in word $word"

fi
