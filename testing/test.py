import unittest as ut
class TestCaseDemo(ut.TestCase):
	def setUp(self):
		print("Setup method Execution ... ")

	def test(self):
		print("test method Execution .. ")

	def tearDown(self):
		print("Tear Down method Execution .. ")

ut.main()
