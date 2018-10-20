from primes import is_prime


def test_is_prime():
    assert is_prime(3) is True


def test_is_not_prime():
    assert is_prime(4) is False
