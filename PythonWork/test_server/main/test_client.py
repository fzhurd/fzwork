#!/usr/bin/python
# -*- coding: utf-8 -*-

from ..lib import jsonrpc
server = jsonrpc.ServerProxy(jsonrpc.JsonRpc20(),
    jsonrpc.TransportTcpIp(addr=('127.0.0.1',31415)))

res=server.echo('test second')
print res

first_res = server.minus_numbers(first_number=36,second_number=72)
second_res = server.minus_numbers(first_number=100,second_number=72)

third_res = server.add_numbers(first_number=100,second_number=72)

print first_res
print second_res
print third_res