from io import StringIO
import unittest
from unittest.mock import patch
import stdout

class TestStdOut(unittest.TestCase):
	def test_url_gets_to_stdout(self):
		protocol = 'http'
		host = 'www'
		domain = 'example.com'
		expected_url = '{}://{}.{}\n'.format(protocol, host, domain)

		with patch('sys.stdout', new=StringIO()) as fake_out:
			stdout.print_url(protocol, host, domain)
			self.assertEqual(fake_out.getvalue(), expected_url)

if __name__ == '__main__':
	unittest.main() 