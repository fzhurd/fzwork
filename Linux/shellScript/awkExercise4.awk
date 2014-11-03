
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