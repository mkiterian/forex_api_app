import unittest

from exchange_rates import get_current_usd_rate_vs_world_currencies as forex_rates

class ExchangeRatesTest(unittest.TestCase):
	def test_if_data_is_returned(self):
		self.assertEqual(len(forex_rates())>0, True)

	def test_usd_correct_values_returned(self):
		rates = forex_rates()
		self.assertEqual(rates['USDKES'] > 95, True)

if __name__ == '__main__':
	unittest.main() 

