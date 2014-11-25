#!/usr/bin/python
import sys
import os


def is_list_of_dict_all(input_field):
    
    is_dict_all = all(isinstance(i, dict) for i in input_field)

    return is_dict_all


def is_list_of_dict_any(input_field):
    
    is_dict_any = any(isinstance(i, dict) for i in input_field)

    return is_dict_any

def main():

	lis1 =[{'a1':1},{'a2':2},{'a3':3}]
	lis2 =[{'a1':1},'a2', 'a3']
	lis3= ['a1','a2', 'a3']

	print 'check all-1: ',is_list_of_dict_all(lis1)
	print 'check any-1: ',is_list_of_dict_any(lis1)

	print '***********************************'

	print 'check all-2: ',is_list_of_dict_all(lis2)
	print 'check any-2: ',is_list_of_dict_any(lis2)

	print '***********************************'

	print 'check all-3: ',is_list_of_dict_all(lis3)
	print 'check any-3: ',is_list_of_dict_any(lis3)

	h= [{'a':1},{'b':2},{'c':'cname'}]

	for i in h:
		print i



# class Student(object):
# 	def __init__(self, studentId, name):
# 		pass

# def generator():
# 	for x in xrange(4):
# 		yield x+1

# 		print('incrementing x')
# 		# print next(x)

# def main():
# 	print 'hello'
	
# 	result = generator()
# 	print result
# 	print type(result)
# 	# for i in result:
# 	# 	print i
# 	print result.next()
# 	print result.next()
# 	print result.next()
# 	print result.next()
# 	print result.next()
# 	print result.next()
	
if __name__ == '__main__':
	main()