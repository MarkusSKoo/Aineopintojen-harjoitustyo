"""
keygen_test.py suorittaa yksikkötestejä keygen.py-tiedostossa oleville funktioille.
"""

import time
import pytest
from src.rsa_salaus.keygen import (
    generate_1024bit_number,
    check_primarility_sieve,
    check_primarility_miller_rabin,
    generate_prime,
    generate_keypair
)

class TestGenerate1024BitNumber():
    """Testaa generate_1024bit_number() -funktion toimintaa"""

    def setup_method(self):
        self.number = generate_1024bit_number()

    def test_generate_1024bit_number_length(self):
        assert self.number.bit_length() == 1024

    def test_generate_1024bit_number_oddity(self):
        assert self.number % 2 == 1

    def test_generate_1024bit_number_randomness(self):
        a = generate_1024bit_number()
        b = generate_1024bit_number()
        assert a != b

class TestCheckPrimarilitySieve():
    """Testaa check_primarility_sieve -funktion toimintaa"""

    def test_check_primarility_sieve_small_primes(self):
        small_primes = [2, 3, 5, 7, 11, 13, 73, 79, 83]
        for sm in small_primes:
            assert check_primarility_sieve(sm) is True

    def test_check_primarility_sieve_large_primes(self):
        large_primes = [
            17977, 10619863, 6620830889, 80630964769, 228204732751, 1171432692373,
            1398341745571, 10963707205259, 15285151248481, 10657331232548839,
            790738119649411319, 18987964267331664557
        ]

        for lp in large_primes:
            assert check_primarility_sieve(lp) is True

    def test_check_primarility_sieve_small_nonprimes(self):
        non_primes = [24, 49, 52, 81, 99]

        for np in non_primes:
            assert check_primarility_sieve(np) is False

    def test_check_primarility_sieve_large_nonprimes(self):
        big_non_primes = [5342, 6609, 10765, 11851]

        for bnp in big_non_primes:
            assert check_primarility_sieve(bnp) is False

    def test_check_primarility_sieve_too_small(self):
        too_small = [1, 0, -5]

        for ts in too_small:
            with pytest.raises(ValueError, match="n must be greater than 1"):
                check_primarility_sieve(ts)

class TestPrimeGeneration():
    """Testaa alkulukujen generoimiseen liittyvien funktioiden toimintaa"""

    def test_generate_prime(self):
        prime = generate_prime()
        assert prime.bit_length() == 1024
        assert check_primarility_miller_rabin(prime) is True

    def test_generate_keypair(self):
        time_before = time.time()
        keypair = generate_keypair()
        time_after = time.time()

        p = keypair[0]
        q = keypair[1]

        assert p != q
        assert time_after - time_before <= 4

        assert p.bit_length() == 1024
        assert q.bit_length() == 1024

        assert check_primarility_miller_rabin(p) is True
        assert check_primarility_miller_rabin(q) is True
