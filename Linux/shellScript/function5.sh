fSum 3 2;
 function fSum()
 {
     echo $1,$2;
     return $(($1+$2));
 }
 fSum 5 7;
 total=$(fSum 3 2);
 echo $total,$?;