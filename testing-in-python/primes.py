def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x):
            if x % n == 0:
                return False
        return True


if __name__ == "__main__":
    print is_prime(3)  # Should be True
    print is_prime(4)  # Should be False
