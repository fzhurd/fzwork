#!/bin/bash  


  
for file in $(ls /tmp/test/mytest |grep sh)   #for in格式是shell for的基本格式，根js的for in类似  
do               # 循环开始你就把它当成{  
 echo $file  
done             #循环结束你就把它当成}  
  
for ((i=0;i<10;i++))        #注意是双小括号，由于受其他语言的影响，很容易搞错  
do  
 echo -n $i  
done  
  
echo \     #输出换行  
  
for i in 0 1 2 3 4 5 6 7 8 9  
do  
 echo -n $i  
done  
  
echo \  
  
for i in "0 1 2 3 4 5 6 7 8 9"    #这个根上面是有区别的，这个循环只循环了一次，双引号里面只是一个变量  
do  
 echo -n $i  
done  
  
exit 0  