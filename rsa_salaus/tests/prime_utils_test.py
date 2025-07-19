import pytest
from src.rsa_salaus.prime_utils import sieve_of_eratosthenes

def test_sieve_small():
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]

def test_sieve_negative():
    assert sieve_of_eratosthenes(-5) == "Input must be greater than 1"

def test_sieve_empty():
    assert sieve_of_eratosthenes(0) == "Input must be greater than 1"

def test_sieve_one():
    assert sieve_of_eratosthenes(1) == "Input must be greater than 1"

def test_sieve_two():
    assert sieve_of_eratosthenes(2) == [2]

def test_sieve_three():
    assert sieve_of_eratosthenes(3) == [2, 3]

def test_sieve_large():
    assert sieve_of_eratosthenes(200) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]