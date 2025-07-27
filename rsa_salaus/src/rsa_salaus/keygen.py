"""
keygen.py generoi RSA-salauksessa tarvittavat avainparit.
"""

import random
from rsa_salaus.prime_utils import (
    sieve_of_eratosthenes,
    miller_rabin
)

def generate_1024bit_number():
    """
    Tuottaa ja palauttaa satunnaisen 1024-bittiä pitkän parittoman luvun.
    """
    number = random.getrandbits(1024)
    number |= (1 << (1024 - 1))
    number |= 1
    return number

def check_primality_sieve(n: int):
    """
    Testaa ovatko pienet alkuluvut luvun osatekijöitä.

    Args:
        n (int): Testattava luku.

    Returns:
        True, jos luku ei ole jaollinen millään pienillä alkuluvuista.
        False, jos luku ei ole alkuluku.
    """

    if n < 2:
        raise ValueError("n must be greater than 1")

    small_primes = sieve_of_eratosthenes(4500)

    if n in small_primes:
        return True

    for prime in small_primes:
        if n % prime == 0:
            return False

    return True

def generate_prime():
    """
    Luo 1024-bittisen luvun, joka on todennäköisesti alkuluku
    """
    while True:
        number = generate_1024bit_number()
        if check_primality_sieve(number):
            if miller_rabin(number, 40):
                return number

def generate_keypair():
    """
    Luo kaksi erisuuruista lukua, jotka ovat todennäköisesti alkulukuja.
    """
    while True:
        p = generate_prime()
        q = generate_prime()
        if p != q:
            return (p, q)
