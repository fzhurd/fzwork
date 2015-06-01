#!/bin/bash  
function GetDiskSpc
{
 if [ $
# -ne 1 ]
 then
 return 1
 fi
	Folder="$1$"
	DiskSpace=`df -k |grep $Folder |awk '{print $5}' |awk -F% '{print $1}'
 	echo $DiskSpace
}


Folder="/boot"
DiskSpace=`GetDiskSpc $Folder`
echo "The system $Folder disk space is $DiskSpace%"
if [ $DiskSpace -gt 90 ]
 then
 {
 	echo "The usage of system disk($Folder) is larger than 90%"
 }
 else
 {
 	echo "The usage of system disk($Folder) is normal"
 }
 fi


