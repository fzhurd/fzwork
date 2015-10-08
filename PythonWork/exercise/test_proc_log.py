#!/usr/bin/python

import psutil


def main():
	# print 'hi'
	for proc in psutil.process_iter():
		if proc.name()=='mongod':
			print proc


if __name__=='__main__':
	main()