awk 'BEGIN{
x=1;
while(getline != 0)
{
   print "what I want to prefix", "label_",x, " as ", $0;
   x++;
 }
}' filea.txt > fileb.txt