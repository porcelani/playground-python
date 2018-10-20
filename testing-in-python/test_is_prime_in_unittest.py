from unittest import TestCase


class TestIsPrime(TestCase):
    def test_is_prime(self):
        from primes import is_prime
        self.assertTrue(is_prime(3))

    def test_is_not_prime(self):
        from primes import is_prime
        self.assertFalse(is_prime(4))
