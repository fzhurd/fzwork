fSum 3 2;
 function fSum()
 {
     echo $1,$2;
     return $(($1+$2));
 }
 fSum 5 7;
 total=$(fSum 3 2);
 echo $total,$?;


 echo $(uname);
declare num=1000;
 
uname()
{
    echo "test!";
    ((num++));
    return 100;
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