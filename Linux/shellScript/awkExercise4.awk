
#! /bin/awk -f

awk '{print;}' employee.txt

Syntax: 

BEGIN { Actions}
{ACTION} # Action for everyline in a file
END { Actions }

# is for comments in Awk

$ awk 'BEGIN {print "Name\tDesignation\tDepartment\tSalary";}
> {print $2,"\t",$3,"\t",$4,"\t",$NF;}
> END{print "Report Generated\n--------------";
> }' employee.txt


Awk Example 6. Print the list of employees in Technology department

Now department name is available as a fourth field, so need to check if $4 matches with the string “Technology”, if yes print the line.

$ awk '$4 ~/Technology/' employee.txt