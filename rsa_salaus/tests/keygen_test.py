"""
keygen_test.py suorittaa yksikkötestejä keygen.py-tiedostossa oleville funktioille.
"""

import random
import pytest
from src.rsa_salaus.keygen import (
    generate_1024bit_number,
    check_primarility_sieve,
    check_primarility_miller_rabin,
    generate_prime,
    generate_keypair
)

def test_generate_1024bit_number():
    number = generate_1024bit_number()
    assert number.bit_length() == 1024

def test_generate_prime():
    prime = generate_prime()
    assert prime.bit_length() == 1024
    assert check_primarility_miller_rabin(prime) is True

def test_generate_keypair():
    keypair = generate_keypair()
    p = keypair[0]
    q = keypair[1]
    assert p.bit_length() == 1024
    assert q.bit_length() == 1024
    assert check_primarility_miller_rabin(p) is True
    assert check_primarility_miller_rabin(q) is True
