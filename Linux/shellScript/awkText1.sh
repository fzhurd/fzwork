


# mongorestore  -d test -c collection_name --directoryperdb  ./dump

awk -F '|' '{print $1}' file1.txt >file2.txt
awk '$1=$1' file2.txt > file3.txt

awk -F '|' '{print $1 $2 ","}' file1.txt >file12.txt
awk '$1=$1' file12.txt > file15.txt

awk -F '|' '{print $1 $2}' file1.txt | awk '{print $0,","}' >file11.txt

awk -F '|' '{print $1 $2 }' file1.txt >file16.txt
awk '$1=$1' file16.txt > file18.txt