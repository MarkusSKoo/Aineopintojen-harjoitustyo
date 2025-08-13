"""
keygen_test.py suorittaa yksikkötestejä keygen.py-tiedostossa oleville funktioille.
"""

from unittest.mock import patch
import pytest
from src.rsa_salaus.keygen import (
    generate_1025bit_number,
    check_primality_sieve,
    generate_prime,
    generate_keypair,
    generate_rsa_keys
)
from src.rsa_salaus.prime_utils import miller_rabin, euclidean

class TestGenerate1025BitNumber():
    """Testaa generate_1025bit_number()-funktion palauttaman luvun
    satunnaisuutta, parittomuutta ja pituutta."""

    def setup_method(self):
        self.number = generate_1025bit_number() # pylint: disable=attribute-defined-outside-init

    def test_generate_1024bit_number_length(self):
        assert self.number.bit_length() >= 1024

    def test_generate_1024bit_number_oddity(self):
        assert self.number % 2 == 1

    def test_generate_1024bit_number_randomness(self):
        a = generate_1025bit_number()
        b = generate_1025bit_number()
        assert a != b

class TestCheckPrimalitySieve():
    """Testaa check_primality_sieve() -funktion toimintaa."""

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
        too_small = [-5, 0, 247, 4500]

        for ts in too_small:
            with pytest.raises(ValueError, match="n must be greater than 4500"):
                check_primality_sieve(ts)

    def test_check_primality_sieve_1025bits(self):
        assert check_primality_sieve(generate_prime()) is True

class TestPrimeGeneration():
    """Testaa alkulukujen generoimiseen liittyvien funktioiden toimintaa."""

    def test_generate_prime(self):
        prime = generate_prime()
        assert prime.bit_length() >= 1024
        assert miller_rabin(prime, 40) is True

    def test_generate_keypair(self):
        keypair = generate_keypair()

        p = keypair[0]
        q = keypair[1]

        assert p != q

        assert p.bit_length() >= 1024
        assert q.bit_length() >= 1024

        assert miller_rabin(p, 40) is True
        assert miller_rabin(q, 40) is True

    @patch("src.rsa_salaus.keygen.generate_prime")
    def test_generate_keypair_mocked(self, mock):
        """Testaa generate_keypair() -funktion toimintaa identtisillä paluuarvoilla."""

        mock.side_effect = [13, 13, 19, 5]
        # Testaamista varten valitsee ensimmäiselle kierrokselle identtiset arvot,
        # jotta while-silmukka toistetaan
        keypair = generate_keypair()

        p = keypair[0]
        q = keypair[1]

        assert p != q

# pylint: disable=too-many-instance-attributes, attribute-defined-outside-init
class TestGenerateRsaKeys:
    """Testaa generate_rsa_keys() -funktion toimintaa."""

    def setup_method(self):
        """Asettaa testattavat paluuarvot debug=True-tilassa tehtäviä testejä varten."""

        self.rsa_keypair = generate_rsa_keys(debug=True)

        self.public_key = self.rsa_keypair[0]
        self.private_key = self.rsa_keypair[1]
        self.e = self.public_key[1]
        self.d = self.private_key[1]

        self.p = self.rsa_keypair[2][0]
        self.q = self.rsa_keypair[2][1]
        self.phi_n = (self.p - 1) * (self.q - 1)

    def test_rsa_keypair_return_format(self):
        """Testaa funktion returns-arvojen formaattia, kun debug=True."""

        assert len(self.rsa_keypair) == 3
        assert len(self.public_key) == 2
        assert len(self.private_key) == 2
        assert len(self.rsa_keypair[2]) == 2

        assert isinstance(self.public_key[0], int)
        assert isinstance(self.e, int)

        assert isinstance(self.private_key[0], int)
        assert isinstance(self.d, int)

        assert isinstance(self.p, int)
        assert isinstance(self.q, int)

    def test_rsa_keypair_math(self):
        """Testaa funktion matemaattista oikeellisuutta, kun debug=True."""

        assert self.public_key[0] == self.private_key[0]
        assert self.p * self.q == self.public_key[0]

        assert self.p != self.q
        assert self.p.bit_length() >= 1024
        assert self.q.bit_length() >= 1024

        assert miller_rabin(self.p, 40) is True
        assert miller_rabin(self.q, 40) is True

        assert euclidean(self.e, self.phi_n) == 1
        assert (self.e * self.d) % self.phi_n == 1
        assert 1 <= self.d < self.phi_n - 1

    def helper_mock_euclidean(self, a: int, b: int):
        """Apufunktio mockaamiseen, jotta testattaessa generate_rsa_keys menee
        else-haaraan ja käyttää sen jälkeen euclidean-funktiota."""

        self.euclidean_counter += 1

        if self.euclidean_counter < 13:
            return 0

        return euclidean(a, b)

    @patch("src.rsa_salaus.keygen.euclidean")
    def test_keypair_return_format_mocked(self, mock_euclidean):
        """Yksikkötesti generate_rsa_keys() -funktiolle, jossa kutsuttavien funktioiden paluuarvoja
        mockattu yksikkötestien kattavuuden parantamiseksi, kun debug=False."""

        self.euclidean_counter = 0
        mock_euclidean.side_effect = self.helper_mock_euclidean

        rsa_keypair = generate_rsa_keys()
        public_key = rsa_keypair[0]
        private_key = rsa_keypair[1]

        assert len(rsa_keypair) == 2
        assert len(public_key) == 2
        assert len(private_key) == 2

        assert public_key[0] == private_key[0]
        assert public_key[0].bit_length() >= 2048
        assert private_key[0].bit_length() >= 2048

        assert isinstance(public_key[0], int)
        assert isinstance(public_key[1], int)
        assert isinstance(private_key[0], int)
        assert isinstance(private_key[1], int)
