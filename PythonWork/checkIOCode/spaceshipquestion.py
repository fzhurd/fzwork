#!/usr/bin/python

def checkio(data):

    initial_sofi, raise_sofi, initial_oldman, reduction_oldman = data
    current_sofi = initial_sofi + raise_sofi
    current_oldman = initial_oldman - reduction_oldman
    
    while True:
        if initial_sofi >= initial_oldman:
            val = max(initial_oldman, initial_oldman + reduction_oldman)
            return min(initial_sofi, val)
        else:
            initial_sofi += raise_sofi
            initial_oldman -= reduction_oldman

#Some hints
#Be careful with endless loop


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([150, 50, 1000, 100]) == 450, "1st example"
    assert checkio([150, 50, 900, 100]) == 400, "2nd example"
