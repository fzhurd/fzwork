#!/usr/bin/python
import sys
import os
class Student(object):
	def __init__(self, studentId, name):
		pass

def generator():
	for x in xrange(4):
		yield x+1

		print('incrementing x')
		# print next(x)

def main():
	print 'hello'
	
	result = generator()
	print result
	print type(result)
	# for i in result:
	# 	print i
	print result.next()
	print result.next()
	print result.next()
	print result.next()
	print result.next()
	print result.next()
	
if __name__ == '__main__':
	main()