#!/usr/bin/python
# -*- coding: utf-8 -*-




import re

# regexes = [re.compile('.js')]

# mystring = 'hi'

# if any(regex.match('.js') for regex in regexes):
#     print 'Some regex matched!'



def read_file(file, mode):

    # regex=re.compile("*.js")
    with open(file,mode) as fn:
        for f in fn:
            line=f.split()

            # print '**************'

            for l in line:
                ele=l.split('/')              
                # x=[m.group(0) for l in ele for m in [regex.search(l)] if m]
                # print x
                for e in ele:
                    if '.js' in e:
                        print e


def main():
    read_file('./temp.txt', 'r')
    


    # regex=re.compile("*(.js)")
    # [m.group(0) for l in ele for m in [regex.search(l)] if m]



if __name__=='__main__':
    main()