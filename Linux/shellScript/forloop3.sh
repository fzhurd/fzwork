#!/bin/bash  

# for file in $(ls /tmp/test/mytest |grep sh)   #for in格式是shell for的基本格式，根js的for in类似  
# do               # 循环开始你就把它当成{  
#  echo $file  
# done             #循环结束你就把它当成}  
  
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


#!/bin/bash  
i=0  
while ((i<10))  
do  
 echo $i  
 ((i += 1))  
done  
  
i=0  
while [ $i -lt 10 ]  #注意括号内侧二边的空格  
do  
 echo $i  
 let "i+=1"   #加1  
done  
exit 0  #!/bin/bash  
  
echo "Input a number #1 "  
read num  
echo "variable #1 = $num"  
  
if [ $num -lt 60 ]    #注意lt前面的-，很容易忘的  
then  
 echo "you are not pass"  
elif [ $num -lt 70 ] && [ $num -ge 60 ]  #多个条件的判断  
then  
 echo "pass"  
elif [[ $num -lt 85 && $num -ge 70 ]] #如果放在一起，要注意是双方括号，不要写成[ $num -lt 85 && $num -ge 70 ]  
then  
 echo "good"  
elif (( $num <= 100 )) && (( $num >= 85 ))  #对于有语言基础的人来说，这种写法让人觉得很舒服，不要忘了是双小括号  
then  
 echo "very good"  
else  
 echo "num is wrong"  
fi                                 #if要有结束标签的，根XML很像,不闭合，就报错  
  
exit 0  



#!/bin/bash  
  
echo "Input a number #1 "  
read num  
echo "variable #1 = $num"  
  
if [ $num -lt 60 ]    #注意lt前面的-，很容易忘的  
then  
 echo "you are not pass"  
elif [ $num -lt 70 ] && [ $num -ge 60 ]  #多个条件的判断  
then  
 echo "pass"  
elif [[ $num -lt 85 && $num -ge 70 ]] #如果放在一起，要注意是双方括号，不要写成[ $num -lt 85 && $num -ge 70 ]  
then  
 echo "good"  
elif (( $num <= 100 )) && (( $num >= 85 ))  #对于有语言基础的人来说，这种写法让人觉得很舒服，不要忘了是双小括号  
then  
 echo "very good"  
else  
 echo "num is wrong"  
fi                                 #if要有结束标签的，根XML很像,不闭合，就报错  
  
exit 0  