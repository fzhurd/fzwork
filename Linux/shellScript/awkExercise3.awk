
#! /bin/awk -f

#while loop
echo "1234/1234/bb234xx/134" | awk -F'/' '{ i=1;while(i<NF) {print NF,$i;i++}}'

# for example
echo "1234/1234/bb234xx/134" | awk -F'/' '{ for(i=1;i<NF;i++) {print NF,$i}}'