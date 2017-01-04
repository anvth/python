import sys
import unittest

def parse_int(s):
	return int(s)

class TestValueError(unittest.TestCase):
	def test_parse_int(self):
		with self.assertRaises(ValueError):
			r = parse_int('N/A')

def main(out=sys.stderr, verbosity=2):
	loader = unittest.TestLoader()
	suite = loader.loadTestsFromModule(sys.modules[__name__])
	unittest.TextTestRunner(out, verbosity=verbosity).run(suite)
	
if __name__ == '__main__':
	with open('output.txt', 'w') as f:
		main(f)