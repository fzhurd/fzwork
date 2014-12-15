#!/bin/bash  
awk -F '|' '{print $1, $2}' a.txt >b.txt