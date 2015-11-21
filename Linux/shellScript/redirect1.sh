#!/bin/bash 

exec 6>&1
#将标准输出与fd 6绑定
  
ls /proc/self/fd/
0 1 2 3 6
#出现文件描述符6
  
exec 1>suc.txt
#将接下来所有命令标准输出，绑定到suc.txt文件（输出到该文件）
  
ls -al
#执行命令，发现什么都不返回了，因为标准输出已经输出到suc.txt文件了
  
exec 1>&6
#恢复标准输出
  
exec 6>&-
#关闭fd 6描述符

ls /proc/self/fd/
0 1 2 3