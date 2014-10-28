
#! /bin/awk -f

echo "1234/1234/bb234xx/134" | awk -F'/' '{ i=1;while(i<NF) {print NF,$i;i++}}'