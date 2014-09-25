#!/bin/bash  

for c in "hello world" "good weather" "this a sunny day"
do
  echo $c
done

file1="addOne.sh"
file2="forloop1.sh"


for file in `ls`
do
	if [ $file == $file2 ] ;then 

		echo $file " is  the forloop1.sh right script"; 

	elif [ $file != $file1 ] ; then

		echo $file " is not the addOne file" ;
	else 
		echo $file " is the addOne" ; echo

	fi
done


NUMBERS="1 2 3 4 5"


for i in `echo $NUMBERS`

do
	echo -n $i; 
done

echo


PASSWORD_FILE=/etc/passwd
n=1

for name in $(awk 'BEGIN{FS=":"}{print $1}' < "$PASSWORD_FILE" )

do
	echo "USER #$n = $name"
	let "n += 1"
done