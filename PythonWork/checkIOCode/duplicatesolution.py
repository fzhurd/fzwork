#!/usr/bin/python


def checkio(data):
 
    #replace this for solution
    uniqueList = list(set(data))
    newData = []
    counter =0
 #   repeatList = data - uniqueList
    for uni in uniqueList :
        for single in data:
            if uni == single:
                counter = counter +1
        if counter == 1:
            data.remove(uni)
        counter=0
            
  #  data = newData
    return data



#automatic test driven
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"