#!/bin/bash  
fSum 3 2;
function fSum()
 {
     echo $1,$2;
     return $(($1+$2));
 }
 fSum 5 7;
 echo '***************************'
 total=$(fSum 3 2);
 echo $total,$?;
 echo '***************************8'
 total2=$(fSum 300 200);
 echo $total2,$?;

 total3=$(fSum 12 20);
 echo $total3,$?;



echo $(uname);
echo '***********************'
declare num=1000;
 
uname()
{
    echo "test!";
    ((num++));
    return 10000;
}
testvar()
{
    local num=10;
    ((num++));
    echo $num;
 
}
 
uname;
echo $?
echo $num;
testvar;
echo $num;
          