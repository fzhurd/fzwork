#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def main():
	home = os.environ.get('TMPTESTHOME')
	print home

	print os.getcwd()
	os.chdir("/home/frank/workAtHome")

	print os.getcwd()
	current_dir=os.getcwd()

	all_folders = os.listdir(current_dir)
	print all_folders

	os.rename("/home/frank/workAtHome/tmp_test","/home/frank/workAtHome/tmp_test_after_change")

	all_folders_after_change=os.listdir(current_dir)
	print all_folders_after_change

	print '***********************************'

	os.chdir(home)

	print os.getcwd()
	


if __name__ == '__main__':
	main()

