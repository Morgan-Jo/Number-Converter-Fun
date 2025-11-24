from number_utils import is_prime, get_factors

def run_tests():
    # Prime tests
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(17) is True
    assert is_prime(18) is False
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-7) is False

    # Factor tests
    assert get_factors(1) == [1]
    assert get_factors(6) == [1, 2, 3, 6]
    assert get_factors(28) == [1, 2, 4, 7, 14, 28]
    assert get_factors(-12) == [1, 2, 3, 4, 6, 12]

    # 0 factors should raise ValueError
    try:
        get_factors(0)
    except ValueError:
        pass
    else:
        raise AssertionError("get_factors(0) should raise ValueError")

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
