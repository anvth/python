import unittest

def parse_int(s):
	return int(s)

class TestValueError(unittest.TestCase):
	def test_parse_int(self):
		with self.assertRaises(ValueError):
			r = parse_int('N/A')

if __name__ == '__main__':
	unittest.main()