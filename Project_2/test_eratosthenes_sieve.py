''' Unit test to eratosthenes_sieve.py script. 
Run as a module: $python -m uniitest test_eratosthenes_sieve '''

import unittest
from sympy import sieve

from eratosthenes_sieve import find_all_prime_numbers, is_valid

class TestCalc(unittest.TestCase):
    def test_find_all_prime_numbers(self):
        self.assertEqual(find_all_prime_numbers(2), [2])
        self.assertEqual(find_all_prime_numbers(3), [2,3])

        # use build-in function from sympy library to test bigger numbers
        self.assertEqual(find_all_prime_numbers(47), 
                        list(sieve.primerange(2, 48)))
        self.assertEqual(find_all_prime_numbers(9999), 
                list(sieve.primerange(2, 10000)))

    def test_is_valid(self):
        self.assertTrue(is_valid('10'))
        self.assertFalse(is_valid('xD'))
        self.assertFalse(is_valid('5.5'))
        self.assertFalse(is_valid('-8'))
        self.assertFalse(is_valid('0'))

        # to check if ValueError is raised
        # with self.assertRaises(ValueError):
        #     is_valid('xD')