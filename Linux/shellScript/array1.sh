#!/bin/bash 
a=(1 2 3 4 5)
echo ${a[*]}

echo ${#a[@]}

echo ${a[@]:0:3}

echo ${a[@]:1:4}

unset a
echo ${a[*]}