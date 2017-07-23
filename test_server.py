# test_server.py

import unittest
import os
import json

from server import create_app
import z3
import json

class ServerTestCase(unittest.TestCase):
	"""This class represents the modsplanner server test case"""

	def setUp(self):
		"""Define test variables and initialize app"""
		self.app = create_app(config_name="testing")
		self.client = self.app.test_client

	def test_api_get(self):
		result = self.client().get('/api/1/4/CS2105,CS2107,MA1100,MA1102R/CS1231,CS2101/%7B%7D')
		self.assertEqual(result.status_code, 200)

	def test_api_get_returns_valid_smtlib(self):
		result = self.client().get('/api/1/4/CS2105,CS2107,MA1100,MA1102R/CS1231,CS2101/%7B%7D')
		# smtQuery = result.data[0]
		data = json.loads(result.data)
		smtQuery = data[0]
		
		s = z3.Solver()
		s.add(z3.parse_smt2_string(smtQuery))

		self.assertEqual(s.check(), z3.sat)
		
if __name__ == "__main__":
	unittest.main()