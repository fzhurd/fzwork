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