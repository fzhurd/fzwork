#!/bin/bash 

echo {1..5}

for i in {1..10}
do
	echo $i
done

aNumList=$(seq 100);
echo $aNumList

bNumList=$(seq 10)
echo $bNumList