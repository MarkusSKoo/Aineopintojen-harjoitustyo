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