#!/usr/bin/python
# -*- coding: utf-8 -*-

# from ..lib import jsonrpc
# server = jsonrpc.ServerProxy(jsonrpc.JsonRpc20(),
#     jsonrpc.TransportTcpIp(addr=('127.0.0.1',31415)))

# res=server.echo('test second')
# print res

# first_res = server.minus_numbers(first_number=36,second_number=72)
# second_res = server.minus_numbers(first_number=100,second_number=72)

# third_res = server.add_numbers(first_number=100,second_number=72)

# print first_res
# print second_res
# print third_res

from ..lib import jsonrpc
import unittest


class TestJsonRPC20Server(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.server = jsonrpc.ServerProxy(jsonrpc.JsonRpc20(),
            jsonrpc.TransportTcpIp(addr=('127.0.0.1',31415)))

    @classmethod
    def tearDown(self):
        pass


    def test_add(self):
        self.first_res = self.server.add_numbers(first_number=36,second_number=72)
        self.assertEqual(self.first_res, 108)

    def test_minus(self):
        self.first_res = self.server.minus_numbers(first_number=36,second_number=72)
        self.assertEqual(self.first_res, -36)