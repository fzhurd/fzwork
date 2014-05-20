#!/usr/bin/python
FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
 #   str_1number = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
 #   str_2number = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
 #   str_3number = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred']
    
    if number < 10:
        return FIRST_TEN[number]

    if number >= 10 and number < 20:
        return SECOND_TEN[number % 10]

    if number >= 20 and number < 100:
        if number % 10 == 0:
       #     return OTHER_TENS[((number - (number % 10)) / 10) -2 ]
             return OTHER_TENS[int((number  / 10)) -2 ]
        else:
        #    return OTHER_TENS[((number - (number % 10)) / 10) -2 ] + " " + checkio(number % 10)
             return OTHER_TENS[int(((number - (number % 10)) / 10)) -2 ] + " " + checkio(number % 10)

    if number > 100 and number % 100 !=0 and number < 1000:
            return FIRST_TEN[int((number - (number % 100)) / 100)] +" "+ HUNDRED +" "+ checkio(number % 100)
    
    if (number % 100==0):
            return FIRST_TEN[int((number - (number % 100)) / 100)] +" "+ HUNDRED 
    
    ''' firstRead='' 
    secondRead=''
    thirdRead='' 
    final =''
    length = len(str(number))
    if length ==3:
        if number[0]==1:
            firstRead=FIRST_TEN[1]
        elif number[0]==2:
            firstRead=FIRST_TEN[2]
        elif number[0]==3:
            firstRead=FIRST_TEN[3]
        elif number[0]==4:
            firstRead=FIRST_TEN[4]
        elif number[0]==5:
            firstRead=FIRST_TEN[5]
        elif number[0]==6:
            firstRead=FIRST_TEN[6]
        elif number[0]==7:
            firstRead=FIRST_TEN[7]
        elif number[0]==8:
            firstRead=FIRST_TEN[8]
        elif number[0]==9:
            firstRead=FIRST_TEN[9]
        
    firstRead= firstRead + HUNDRED
    '''