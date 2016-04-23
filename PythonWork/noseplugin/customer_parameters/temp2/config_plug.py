#! /usr/bin/python
# -*- coding: utf-8 -*-

from nose.plugins import Plugin

class ConfiguringPlugin(Plugin):
	enabled = True
	def configure(self, options, conf):
		pass 

	def begin(self):
		ConfigurableWidget.cfg = {}
