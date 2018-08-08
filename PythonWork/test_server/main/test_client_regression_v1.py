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

from test_server.lib import jsonrpc
import unittest


class TestJsonRPC20Server(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = jsonrpc.ServerProxy(jsonrpc.JsonRpc20(),
            jsonrpc.TransportTcpIp(addr=('127.0.0.1',31415)))

    @classmethod
    def tearDown(cls):
        pass

    def test_add(self):
        # import pdb
        # pdb.set_trace()
        self.first_res = self.server.add_numbers(first_number=36,second_number=72)
        self.assertEqual(self.first_res, 108)

    def test_minus(self):
        self.first_res = self.server.minus_numbers(first_number=36,second_number=72)
        self.assertEqual(self.first_res, -36)

    def test_request(self):
        # res=jsonrpc.JsonRpc20().dumps_request("some method")
        res=jsonrpc.JsonRpc20().dumps_request("some method")
        expected_results = '{"jsonrpc": "2.0", "method": "some method", "id": 0}' 
        self.assertEqual(res, expected_results)

    def test_request_with_int_id(self):
        import pdb
        pdb.set_trace()
        res=jsonrpc.JsonRpc20().dumps_request(method="some method", id=100)
        expected_results = '{"jsonrpc": "2.0", "method": "some method", "id": 100}' 
        self.assertEqual(res, expected_results)

    def test_request_with_strid(self):
        pass

    def test_request_with_params(self):
        pass

    def test_response(self):
        pass