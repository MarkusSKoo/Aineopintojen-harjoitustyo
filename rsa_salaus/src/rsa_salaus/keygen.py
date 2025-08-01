"""
keygen.py generoi RSA-salauksessa tarvittavat avainparit.
"""

import random
from rsa_salaus.prime_utils import (
    sieve_of_eratosthenes,
    miller_rabin,
    euclidean,
    extended_euclidean
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
            return p, q

def generate_keys():
    """Luo julkisen ja yksityisen avaimen.
    
    Returns:
        Tuple[Tuple[int, int], Tuple[int, int]]:
        Julkinen avain, yksityinen avain"""

    p, q = generate_keypair()
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e_candidates = [11939, 19391, 19937, 37199, 39119, 71993, 91193, 93719, 93911, 99371]

    for e_c in e_candidates:
        if euclidean(phi_n, e_c) == 1:
            e = e_c
            break

    else:
        while True:
            e = random.randint(1, 100000)
            if euclidean(phi_n, e) == 1:
                break

    d, _ = extended_euclidean(e, phi_n)
    d = d % phi_n

    public_key = n, e
    private_key = n, d

    return public_key, private_key
