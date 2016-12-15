#!/usr/bin/python
# -*- coding: utf-8 -*-




import re

# regexes = [re.compile('.js')]

# mystring = 'hi'

# if any(regex.match('.js') for regex in regexes):
#     print 'Some regex matched!'


from collections import Counter

def find_test(element):
    if '.js' in element:
        return element


def read_file(file, mode):


    # regex=re.compile("*.js")
    tests=[]
    with open(file,mode) as fn:
        for f in fn:
            line=f.split()
            for l in line:
                ele=l.split('/')  
                # tests=map(find_test, ele)
                temp= [e.upper() for e in ele if '.js' in e]
                print temp
                # if temp is not None:
                #     tests.append(temp)
                

                # for e in ele:
                #     if '.js' in e:
                #         tests.append(e)
        return tests


def main():
    tests=read_file('./temp.txt', 'r')
    # print tests
    tim=Counter(tests)
    # print tim

    for k, v in tim.iteritems():
        if v==2:
            print k, v
    


    # regex=re.compile("*(.js)")
    # [m.group(0) for l in ele for m in [regex.search(l)] if m]



if __name__=='__main__':
    main()