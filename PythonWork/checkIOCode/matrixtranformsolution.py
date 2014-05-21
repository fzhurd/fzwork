#!/usr/bin/python

def checkio(data):
   
   data = [list(i) for i in zip(*data)]
   return data
   
'''
    i= len(data)
    j= len(data[0])
    
    newData = [j][i]
    
    for x in range(0, i):
        for x in range(0, j):
          
   
   
   
   for list in data:
        for x in list:
            print x
    
'''

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]) == [[1, 4, 7],
                                    [2, 5, 8],
                                    [3, 6, 9]], "Square matrix"
    assert checkio([[1, 4, 3],
                    [8, 2, 6],
                    [7, 8, 3],
                    [4, 9, 6],
                    [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                                    [4, 2, 8, 9, 8],
                                    [3, 6, 3, 6, 1]], "Rectangle matrix"
