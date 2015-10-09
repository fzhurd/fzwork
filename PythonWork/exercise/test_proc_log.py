#!/usr/bin/python

import psutil


def main():
	find_process()

def find_process():
	for proc in psutil.process_iter():
		if proc.name()=='sonarsql':
			print proc.cmdline()


def tail():
	pass


if __name__=='__main__':
	main()