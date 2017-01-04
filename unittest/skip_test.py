import os
import unittest
import platform

class Test(unittest.TestCase):
	def test_0(self):
		self.assertTrue(True)

	@unittest.skip('skipped test')
	def test_1(self):
		self.fail('Should have failed')

	@unittest.skipIf(os.name == 'posix', 'Not supported in Unix')
	def test_2(self):
		import someWindowsSpecificThingy

	@unittest.skipUnless(platform.system() == 'Darwin', 'Mac Specific test')
	def test_3(self):
		import someMacSpecificThingy

	@unittest.expectedFailure
	def test_4(self):
		self.assertEqual(2+2, 5)

if __name__ == '__main__':
	unittest.main()