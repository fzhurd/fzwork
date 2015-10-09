#!/usr/bin/python

import psutil


def main():
	# print 'hi'
	for proc in psutil.process_iter():
		if proc.name()=='sonarsql':
			print proc.cmdline()


if __name__=='__main__':
	main()