
#!/usr/bin/python
def checkio(data):

    lenth=len(data)
    uppNum=0
    dig=0
    lowNum =0 
    if lenth >=10:
        for individual in data:
            if individual.isupper():
                uppNum = uppNum+1
            if individual.islower():
                lowNum = lowNum+1
            if individual.isdigit():
                dig= dig+1
        if dig>0 and uppNum >0 and lowNum >0:
            return True
        else:
            return False
       
    else:
       return False
       
       
        
    # return True or False

#Some hints
#Just check all conditions


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
