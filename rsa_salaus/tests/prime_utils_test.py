import pytest
from src.rsa_salaus.prime_utils import sieve_of_eratosthenes

def test_sieve_small():
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]
