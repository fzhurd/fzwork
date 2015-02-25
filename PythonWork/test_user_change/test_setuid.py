#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import datetime
import os
import pymongo
import sys
import time
from pymongo import MongoClient
import subprocess
import getpass
import  pwd


def main():
	print os.getuid()
	print os.getgid()
	print os.environ['USER']
	os.environ['USER']='test'
	print os.environ['USER']


	# print os.environ['USERNAME']
	print os.environ['LOGNAME']
	# print os.getlogin()
	print getpass.getuser(), 'ttttttttttt'
	# os.setuid(0)
	# print os.getuid()

	os.getlogin = lambda: pwd.getpwuid(os.getuid())[0]

	print os.getlogin

	newuid = pwd.getpwnam('frank').pw_uid
	print newuid
	os.setuid(newuid)    
	print('User :' + getpass.getuser())
	getpass.setuser('test')

	if not os.geteuid() == 0:
		
		sys.exit('Script must be run as root')
		# os.setuid(0)
		# print os.getuid()




if __name__=='__main__':
	main()


# import os
# import pwd
# import subprocess
# import sys


# def main(my_args=None):
#     if my_args is None: my_args = sys.argv[1:]
#     user_name, cwd = my_args[:2]
#     args = my_args[2:]
#     pw_record = pwd.getpwnam(user_name)
#     user_name      = pw_record.pw_name
#     user_home_dir  = pw_record.pw_dir
#     user_uid       = pw_record.pw_uid
#     user_gid       = pw_record.pw_gid
#     env = os.environ.copy()
#     env[ 'HOME'     ]  = user_home_dir
#     env[ 'LOGNAME'  ]  = user_name
#     env[ 'PWD'      ]  = cwd
#     env[ 'USER'     ]  = user_name
#     report_ids('starting ' + str(args))
#     process = subprocess.Popen(
#         args, preexec_fn=demote(user_uid, user_gid), cwd=cwd, env=env
#     )
#     result = process.wait()
#     report_ids('finished ' + str(args))
#     print 'result', result


# def demote(user_uid, user_gid):
#     def result():
#         report_ids('starting demotion')
#         os.setgid(user_gid)
#         os.setuid(user_uid)
#         report_ids('finished demotion')
#     return result


# def report_ids(msg):
#     print 'uid, gid = %d, %d; %s' % (os.getuid(), os.getgid(), msg)


# if __name__ == '__main__':
#     main()