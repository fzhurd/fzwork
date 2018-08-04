#!/usr/bin/python
# -*- coding: utf-8 -*-

import jsonrpc2

print 'test'

# pip install jsonrpyc
# export PYTHONPATH=$PYTHONPATH
# runjsonrpc2 test_server_v1

def greeting(name):
    return dict(message="test, %s" %name)