#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import unittest

class BaseTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		raise NotImplementedError()

	@classmethod
	def tearDownClass(cls):
		raise NotImplementedError()

	def setUp(self):
		raise NotImplementedError()

	def tearDown(self):
		raise NotImplementedError()

