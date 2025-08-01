"""
prime_utils_test.py suorittaa yksikkötestejä prime_utils.py-tiedostossa oleville funktioille.
"""

import csv
import random
import pytest
from src.rsa_salaus.prime_utils import (
    sieve_of_eratosthenes,
    miller_rabin, euclidean,
    extended_euclidean
)

class TestSieveOfEratosthenes():
    """yksikkötestit sieve_of_eratosthenes -funktiolle"""

    def test_sieve_small(self):
        assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]

    def test_sieve_negative(self):
        with pytest.raises(ValueError, match="Input must be greater than 1"):
            sieve_of_eratosthenes(-5)

    def test_sieve_zero(self):
        with pytest.raises(ValueError, match="Input must be greater than 1"):
            sieve_of_eratosthenes(0)

    def test_sieve_one(self):
        with pytest.raises(ValueError, match="Input must be greater than 1"):
            sieve_of_eratosthenes(1)

    def test_sieve_two(self):
        assert sieve_of_eratosthenes(2) == [2]

    def test_sieve_three(self):
        assert sieve_of_eratosthenes(3) == [2, 3]

    def test_sieve_large(self):
        assert sieve_of_eratosthenes(200) == [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
            61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
            131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
            193, 197, 199
        ]

class TestMillerRabin():
    """Yksikkötestit miller_rabin -funktiolle"""

    def setup_method(self):
        self.verified_primes = [] # pylint: disable=attribute-defined-outside-init

        with open('tests/primes.csv', newline='', encoding='utf-8') as file:
            data = csv.reader(file)
            next(data) # Ohittaa ensimmäisen rivin

            for row in data:
                self.verified_primes.append(int(row[1], 16))

    def test_miller_rabin_small_n(self):
        with pytest.raises(ValueError, match="n must be greater than 1"):
            miller_rabin(1, 40)

    def test_miller_rabin_2(self):
        assert miller_rabin(2, 40) is True

    def test_miller_rabin_even_n(self):
        numbers = []
        for i in range(1000, 1100):
            if i % 2 == 0:
                numbers.append(i)

        for number in numbers:
            assert miller_rabin(number, 40) is False

    def test_miller_rabin_zero_k(self):
        with pytest.raises(ValueError, match="k must be greater than 0"):
            miller_rabin(3, 0)

    def test_miller_rabin_negative_k(self):
        with pytest.raises(ValueError, match="k must be greater than 0"):
            miller_rabin(3, -1)

    def test_miller_rabin_5000(self):
        numbers = sieve_of_eratosthenes(5000)
        for number in numbers:
            assert miller_rabin(number, 40) is True

    def test_miller_rabin_middle(self):
        numbers = [
            7727, 7741, 7753, 7757, 7759, 7789, 7793, 7817, 7823, 7829,
            7841, 7853, 7867, 7873, 7877, 7879, 7883, 7901, 7907, 7919
        ]

        for number in numbers:
            assert miller_rabin(number, 40) is True

    def test_miller_rabin_large(self):
        numbers = [
            611693, 611707, 611729, 611753, 611791, 611801, 611803, 611827, 611833, 611837,
            611839, 611873, 611879, 611887, 611903, 611921, 611927, 611939, 611951, 611953
        ]

        for number in numbers:
            assert miller_rabin(number, 40) is True

    def test_miller_rabin_not_primes(self):
        primes = sieve_of_eratosthenes(1224)

        numbers = []
        for i in range(3, 1223):
            if i not in primes:
                numbers.append(i)

        for number in numbers:
            assert miller_rabin(number, 40) is False

    def test_miller_rabin_big_not_primes(self):
        primes = [
        611693, 611707, 611729, 611753, 611791, 611801, 611803, 611827, 611833, 611837,
        611839, 611873, 611879, 611887, 611903, 611921, 611927, 611939, 611951, 611953
    ]

        non_primes = []
        for i in range(611693, 611953):
            if i not in primes:
                non_primes.append(i)

        for number in non_primes:
            assert miller_rabin(number, 40) is False

    def test_miller_rabin_carmichael(self):
        carmichaels = [561, 1105, 1729, 2465, 2821, 6601, 8911]

        for c in carmichaels:
            assert miller_rabin(c, 40) is False

    def test_miller_rabin_verified_primes(self):
        multipliers = [2, 3, 5]

        for prime in self.verified_primes:
            assert miller_rabin(prime, 40) is True

            for mp in multipliers:
                assert miller_rabin(prime * mp, 40) is False

class TestEuclidean():
    """Yksikkötestit euclidean -funktiolle"""

    def test_euclidean_small_common_divisor(self):
        assert euclidean(48, 18) == 6

    def test_euclidean_small_coprime(self):
        assert euclidean(17, 12) == 1

    def test_euclidean_one(self):
        assert euclidean(1, 174562) == 1

    def test_euclidean_large_common_divisor(self):
        assert euclidean(10000, 100000) == 10000

    def test_euclidean_large_coprime(self):
        big_primes = sieve_of_eratosthenes(100000)

        for i in range(100):

            if i == 10:
                a = big_primes[10]
                b = big_primes[10]

            else:
                a = random.choice(big_primes)
                b = random.choice(big_primes)

            if a == b:
                assert euclidean(a, b) == a

            else:
                assert euclidean(a, b) == 1

    def test_euclidean_samevalue(self):
        assert euclidean(2746, 2746) == 2746

    def test_euclidean_both_zero(self):
        with pytest.raises(ValueError, match="Both values cannot be 0"):
            euclidean(0, 0)

    def test_euclidean_a_zero_b_negative(self):
        assert euclidean(0, -173) == 173

    def test_euclidean_a_negative_b_zero(self):
        assert euclidean(-189, 0) == 189

    def test_euclidean_both_negative(self):
        assert euclidean(-48, -18) == -6

    def test_euclidean_a_negative_b_positive(self):
        assert euclidean(-48, 18) == 6

class TestExtendedEuclidean():
    """Yksikkötestit extended_euclidean -funktiolle"""

    def test_extended_euclidean_common_divisor(self):
        x, y = extended_euclidean(30, 12)
        gcd = euclidean(30, 12)
        assert 30 * x + 12 * y == gcd

    def test_extended_euclidean_coprime(self):
        x, y = extended_euclidean(11, 17)
        gcd = euclidean(11, 17)
        assert 11 * x + 17 * y == gcd

    def test_extended_euclidean_same(self):
        x, y = extended_euclidean(11, 11)
        gcd = euclidean(11, 11)
        assert 11 * x + 11 * y == gcd

    def test_extended_euclidean_a_zero(self):
        x, y = extended_euclidean(0, 23)
        gcd = euclidean(0, 23)
        assert 0 * x + 23 * y == gcd

    def test_extended_euclidean_b_zero(self):
        x, y = extended_euclidean(23, 0)
        gcd = euclidean(23, 0)
        assert 23 * x + 0 * y == gcd

    def test_extended_euclidean_large(self):
        x, y = extended_euclidean(5776, 8334)
        gcd = euclidean(5776, 8334)
        assert 5776 * x + 8334 * y == gcd

    def test_extended_euclidean_one_neg(self):
        x, y = extended_euclidean(-23, 19)
        gcd = euclidean(-23, 19)
        assert -23 * x + 19 * y == gcd

    def test_extended_euclidean_both_neg(self):
        x, y = extended_euclidean(-23, -19)
        gcd = euclidean(-23, -19)
        assert -23 * x + -19 * y == gcd

    def test_extended_euclidean_both_zero(self):
        with pytest.raises(ValueError, match="Both values cannot be 0"):
            extended_euclidean(0, 0)
