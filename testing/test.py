import unittest as ut
class TestCaseDemo(ut.TestCase):
	def setUp(self):
		print("Setup method Execution ... ")

	def test1(self):
		print("test method 1 Execution .. ")


	def test2(self):
		print("test method 2 Execution .. ")

	def tearDown(self):
		print("Tear Down method Execution .. ")

ut.main()
