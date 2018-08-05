#!/usr/bin/python
# -*- coding: utf-8 -*-

#frank2@frank2-VirtualBox:~/workAtHome/git/fzwork/PythonWork$ python -m test_server.main.start_server.py
#frank2@frank2-VirtualBox:~/workAtHome/git/fzwork/PythonWork$ python -m test_server.main.test_client
from test_server.lib import jsonrpc

# from lib import jsonrpc

server = jsonrpc.Server(jsonrpc.JsonRpc20(), 
    jsonrpc.TransportTcpIp(addr=('127.0.0.1', 31415),
    logfunc=jsonrpc.log_file('rpc.log')))

def echo(s):
    return s

def add_numbers(first_number=None, second_number=None):
    return first_number + second_number

def minus_numbers(first_number, second_number):
    return first_number - second_number

server.register_function(echo)
server.register_function(add_numbers)
server.register_function(minus_numbers)

server.serve()
print 'server started'