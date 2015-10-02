#!/usr/bin/python
import sys
import os
import argparse




def main():

	parser = argparse.ArgumentParser()

	# parser = argparse.ArgumentParser(prog='roshambo.py')
	parser.add_argument('-throw', dest= 'throw_dest',required=False, default= 'paper',choices=['rock', 'paper', 'scissors'])
	args = parser.parse_args()
	print("~ Throw: {}".format(args.throw_dest))

	

if __name__ == '__main__':
	main()