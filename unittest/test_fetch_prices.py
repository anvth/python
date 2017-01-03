import io
import unittest
from unittest.mock import patch
import fetch_prices

sample_data = io.BytesIO(b'''\
	"IBM",91.1\r
	"AA",86.3\r
	\r
	''')

class TestFetchPrices(unittest.TestCase):
	@patch('fetch_prices.urlopen', return_value=sample_data)
	def test_fetch_proces(self, mock_urlopen):
		p = fetch_prices.dowprices()
		self.assertTrue(mock_urlopen.called)

if __name__ == '__main__':
	unittest.main()