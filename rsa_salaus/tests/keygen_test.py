"""
keygen_test.py suorittaa yksikkötestejä keygen.py-tiedostossa oleville funktioille.
"""

import time
from unittest.mock import patch
import pytest
from src.rsa_salaus.keygen import (
    generate_1024bit_number,
    check_primality_sieve,
    generate_prime,
    generate_keypair,
    generate_rsa_keys
)
from src.rsa_salaus.prime_utils import miller_rabin

class TestGenerate1024BitNumber():
    """Testaa generate_1024bit_number() -funktion toimintaa"""

    def setup_method(self):
        self.number = generate_1024bit_number() # pylint: disable=attribute-defined-outside-init

    def test_generate_1024bit_number_length(self):
        assert self.number.bit_length() == 1024

    def test_generate_1024bit_number_oddity(self):
        assert self.number % 2 == 1

    def test_generate_1024bit_number_randomness(self):
        a = generate_1024bit_number()
        b = generate_1024bit_number()
        assert a != b

class TestCheckPrimalitySieve():
    """Testaa check_primarility_sieve() -funktion toimintaa"""

    def test_check_primality_sieve_large_primes(self):
        large_primes = [
            17977, 10619863, 6620830889, 80630964769, 228204732751, 1171432692373,
            1398341745571, 10963707205259, 15285151248481, 10657331232548839,
            790738119649411319, 18987964267331664557
        ]

        for lp in large_primes:
            assert check_primality_sieve(lp) is True

    def test_check_primality_sieve_large_nonprimes(self):
        big_non_primes = [5342, 6609, 10765, 11851]

        for bnp in big_non_primes:
            assert check_primality_sieve(bnp) is False

    def test_check_primality_sieve_too_small(self):
        too_small = [-5, 0, 247]

        for ts in too_small:
            with pytest.raises(ValueError, match="n must be greater than 4500"):
                check_primality_sieve(ts)

class TestPrimeGeneration():
    """Testaa alkulukujen generoimiseen liittyvien funktioiden toimintaa"""

    def test_generate_prime(self):
        prime = generate_prime()
        assert prime.bit_length() == 1024
        assert miller_rabin(prime, 40) is True

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

        assert miller_rabin(p, 40) is True
        assert miller_rabin(q, 40) is True

    @patch("src.rsa_salaus.keygen.generate_prime")
    def test_generate_keypair_mocked(self, mock):
        """Testaa generate_keypair() -funktion toimintaa identtisillä paluuarvoilla"""

        mock.side_effect = [13, 13, 19, 5]
        # Testaamista varten valitsee ensimmäiselle kierrokselle identtisen arvon
        keypair = generate_keypair()

        p = keypair[0]
        q = keypair[1]

        assert p != q

class TestGenerateRsaKeys:
    """Testaa generate_rsa_keys() -funktion toimintaa"""

    def test_keypair_return_format(self):
        rsa_keypair = generate_rsa_keys()
        public_key = rsa_keypair[0]
        private_key = rsa_keypair[1]

        assert len(rsa_keypair) == 2
        assert len(public_key) == 2
        assert len(private_key) == 2
        assert public_key[0] == private_key[0]

        assert isinstance(public_key[0], int)
        assert isinstance(public_key[1], int)
        assert isinstance(private_key[0], int)
        assert isinstance(private_key[1], int)

    @patch("src.rsa_salaus.keygen.euclidean")
    def test_keypair_return_format_mocked(self, mock_euclidean):
        """Yksikkötesti generate_rsa_keypair -funktiolle, jossa euclidean:in
        paluuarvot mockattu yksikkötestien kattavuuden parantamiseksi"""

        mock_euclidean.side_effect = [0] * 12 + [1]

        rsa_keypair = generate_rsa_keys()
        public_key = rsa_keypair[0]
        private_key = rsa_keypair[1]

        assert len(rsa_keypair) == 2
        assert len(public_key) == 2
        assert len(private_key) == 2
        assert public_key[0] == private_key[0]

        assert isinstance(public_key[0], int)
        assert isinstance(public_key[1], int)
        assert isinstance(private_key[0], int)
        assert isinstance(private_key[1], int)
