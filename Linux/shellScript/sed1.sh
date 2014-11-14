#!/bin/bash

#replace the "" with NA
sed "s/\"\"/NA/g" tcsv1.txt >tcsv2.txt

#replace the "" with empty space
sed "s/\"\"//g" tcsv1.txt >tcsv2b.txt