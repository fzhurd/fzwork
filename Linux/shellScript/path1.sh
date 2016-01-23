#!/bin/bash 
 
echo "Current path is: `pwd`"
scriptPath=`dirname $0` 
#获取脚本所在路径
 
echo "The script is located at: $scriptPath"
cat "$scriptPath/readme" 
#使用绝对路径引用外部文件