 #!/bin/bash  
while line=`ls /export/um_lpp_source`  
do  
    if test $line=""  
    then  echo "NULL"  
    sleep 1  
    else echo $line  
    chfs -a size=3G /export/um_lpp_source  
    exit 0  
    fi  
done  