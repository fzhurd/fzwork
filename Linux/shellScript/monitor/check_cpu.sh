#!/bin/bash  
function GetCpu
{
	CpuValue=`ps -p $1 -o pcpu |grep -v CPU | awk '{print $1}' | awk - F. '{print $1}'`
 	echo $CpuValue
}

 function CheckCpu
 {
 	PID=$1
 	cpu=`GetCpu $PID`
 	if [ $cpu -gt 80 ]
 	then
 	{
 		echo “The usage of cpu is larger than 80%”
 	}
 	else
 	{
 	echo “The usage of cpu is normal”
 	}
 	fi
 }



 function GetMem
 {
   MEMUsage=`ps -o vsz -p $1|grep -v VSZ`
   (( MEMUsage /= 1000))
   echo $MEMUsage
 }

 mem=`GetMem $PID`
 if [ $mem -gt 1600 ]
 then
 {
 	echo “The usage of memory is larger than 1.6G”
 }
 else
 {
 	echo “The usage of memory is normal”
 }
 fi


mem=`GetMem 11426`
echo "The usage of memory is $mem M"
if [ $mem -gt 1600 ]
 then
 {
 	echo "The usage of memory is larger than 1.6G"
 }
 else
 {
 	echo "The usage of memory is normal"
 }
 fi


function GetDes
 {
 	DES=`ls /proc/$1/fd | wc -l`
 	echo $DES
 }

 des=` GetDes $PID`
 if [ $des -gt 900 ]
 then
 {
 echo “The number of des is larger than 900”
 }
 else
 {
 echo “The number of des is normal”
 }
 fi


des=`GetDes 11426`
echo "The number of des is $des"
if [ $des -gt 900 ]
then
 {
 echo "The number of des is larger than 900"
 }
else
 {
 echo "The number of des is normal"
 }
fi