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
    number |= (1 << (1024 - 1)) # Asettaa suurimman bitin arvoksi 1
    number |= 1 # Asettaa pienimmän bitin arvoksi 1 tuottaen parittoman luvun
    return number

def check_primality_sieve(n: int):
    """
    Testaa onko luku pieni alkuluku tai jaollinen jollain pienistä alkuluvuista.

    Args:
        n (int): Testattava luku.

    Returns:
        True, jos luku ei ole jaollinen pienillä alkuluvuilla.
        False, jos luku ei ole alkuluku.
    """

    if n < 4500:
        raise ValueError("n must be greater than 4500")

    small_primes = sieve_of_eratosthenes(4500)

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
