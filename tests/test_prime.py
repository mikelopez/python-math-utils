import sys
import unittest
from decimal import Decimal
sys.path.append('../')
from pymathutils.prime import *
from actual_primes import primes

# debug types
i, e, w = "INFO", "ERROR", "WARNING"

class TestPrimeNumberCheck(unittest.TestCase):
    """Tests if a number is a prime number."""
    primes = primes.split(' ')

    def setUp(self):
        pass

    def test_prime_number_output(self):
        """Tests accuracy when checking if n is prime number by
        running the list against a list of actual prime numbers from
        online resource wiki."""
        myprimes = []
        for i in range(2, 501):
            if isprime(i):
                myprimes.append(i)
        c = 0
        for i in myprimes:
            self.assertEquals(int(self.primes[c]), i)
            print '- %s is prime man!!' % i
            c += 1


