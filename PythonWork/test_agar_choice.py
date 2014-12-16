#!/usr/bin/python
import sys
import os




def main():

	parser = argparse.ArgumentParser()

	# parser = argparse.ArgumentParser(prog='roshambo.py')
	parser.add_argument('-throw', choices=['rock', 'paper', 'scissors'])
	args = parser.parse_args()
	print("~ Throw: {}".format(args.throw))

	

if __name__ == '__main__':
	main()