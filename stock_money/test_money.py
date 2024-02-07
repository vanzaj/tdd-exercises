# Build a stock portfolio management system
#
# Example:
# | stock | shares | share price | total    |
# | IBM   | 100    | 90 USD      | 9000 USD |
# | BMW   |  10    | 75 EUR      |  750 EUR |
#
# Initial test cases:
#
# [*] 5 USD x 2 == 10 USD
# [ ] 5 EUR x 2 == 10 EUR
# [ ] 5 SGD / 2 = 2.5 SGD
# [ ] 5 USD + 2 USD == 7 USD
# [ ] 5 EUR - 2 EUR == 3 EUR
# [ ] 5 USD + 10 EUR = 16 USD (EUR/USD = 1.1)

import unittest

from money import Money, InvalidCurrency


class TestMoney(unittest.TestCase):


    def test_invalid_currency(self):
        with self.assertRaises(InvalidCurrency):
            money = Money(1, "FOO")


    def testMultiply(self):
        fiveUSD = Money(5, "USD")
        expected = Money(10, "USD")
        self.assertEqual(expected, fiveUSD.times(2))

if __name__ == '__main__':
    unittest.main()
