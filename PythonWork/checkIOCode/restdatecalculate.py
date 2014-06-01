# Q:Sofia has given you a schedule and two dates and told you she needs help planning her weekends. She has asked you to count each day of rest (Saturday and Sunday) starting from the initial date to final date. You should count the initial and final dates if they fall on a Saturday or Sunday.
# The dates are given as datetime.date (Read about this module here). The result is an integer.
# Input: Two dates -- from and to inclusive (datetime.date).
# Output: An integer.



from datetime import date
from datetime import timedelta

def checkio(from_date, to_date):
    
    currentdate = from_date
    enddate = to_date
    count=0
    
    
    while currentdate <= enddate:     
       
        theDay = currentdate.weekday()
        if theDay==5:
            count = count+1
        elif theDay==6:
            count = count+1
        currentdate += timedelta(days=1)
   
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"

