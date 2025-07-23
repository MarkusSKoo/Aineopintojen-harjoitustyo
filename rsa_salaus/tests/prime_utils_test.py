import pytest
from src.rsa_salaus.prime_utils import sieve_of_eratosthenes, miller_rabin, euclidean
import random

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

def test_miller_rabin_small_n():
    assert miller_rabin(1, 1) == "n must be greater than 2"

def test_miller_rabin_even_n():
    assert miller_rabin(982, 1) == False

def test_miller_rabin_small_k():
    assert miller_rabin(3, 0) == "k must be greater than 0"

def test_miller_rabin_200():
    numbers = sieve_of_eratosthenes(200)
    for number in numbers:
        assert miller_rabin(number, 40) == True

def test_miller_rabin_middle():
    numbers = [7727, 7741, 7753, 7757, 7759, 7789, 7793, 7817, 7823, 7829, 7841, 7853, 7867, 7873, 7877, 7879, 7883, 7901, 7907, 7919]
    for number in numbers:
        assert miller_rabin(number, 40) == True

def test_miller_rabin_large():
    numbers = [611693, 611707, 611729, 611753, 611791, 611801, 611803, 611827, 611833, 611837, 611839, 611873, 611879, 611887, 611903, 611921, 611927, 611939, 611951, 611953]
    for number in numbers:
        assert miller_rabin(number, 40) == True

def test_miller_rabin_not_primes():
    primes = sieve_of_eratosthenes(1224)

    numbers = []
    for i in range(3, 1223):
        if i % 2 != 0:
            if i not in primes:
                numbers.append(i)

    for number in numbers:
        assert miller_rabin(number, 40) == False

def test_miller_rabin_big_not_primes():
    primes = [
    611693, 611707, 611729, 611753, 611791, 611801, 611803, 611827, 611833, 611837,
    611839, 611873, 611879, 611887, 611903, 611921, 611927, 611939, 611951, 611953
]
    
    numbers = []
    for i in range(611693, 611953):
        if i % 2 != 0:
            if i not in primes:
                numbers.append(i)

    for number in numbers:
        assert miller_rabin(number, 40) == False

def test_miller_rabin_2048_primes():
    primes = [32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123930385521914333389668342420684974786564569494856176035326322058077805659331026192708460314150258592864177116725943603718461857357598351152301645904403697613233287231227125684710820209725157101726931323469678542580656697935045997268352998638215525166389647960126939249806625440700685819469589938384356951833568218188663, 32317006071311007300714876688669951960444102669715484032130345427524655138867890893197201411522913463688717960921898019494119559150490921095088152386448283120630877367300996091750197750389652106796057638384067568276792218642619756161838094338476170470581645852036305042887575891541065808607552399123930385521914333389668342420684974786564569494856176035326322058077805659331026192708460314150258592864177116725943603718461857357598351152334063994785580370721665417662212881203104945914551140008147396357886767669820042828793708588252247031092071155540224751031064253209884099238184688246467489498721336450133889385773]

    for prime in primes:
        assert miller_rabin(prime, 40) == True

def test_euclidean_small_common_divisor():
    assert euclidean(48, 18) == 6

def test_euclidean_small_coprime():
    assert euclidean(17, 12) == 1

def test_euclidean_one():
    assert euclidean(1, 174562) == 1

def test_euclidean_large_common_divisor():
    assert euclidean(10000, 100000) == 10000

def test_euclidean_large_coprime():
    big_primes = sieve_of_eratosthenes(100000)

    for _ in range(20):
        a = random.choice(big_primes)
        b = random.choice(big_primes)

        if a == b:
            assert euclidean(a, b) == a
        else:
            assert euclidean(a, b) == 1

def test_euclidean_samevalue():
    assert euclidean(2746, 2746) == 2746

def test_euclidean_both_zero():
    try:
        assert euclidean(0, 0) == "Both values cannot be 0"
    except: ValueError("Both values cannot be 0")

def test_euclidean_a_zero_b_negative():
    assert euclidean(0, -173) == 173

def test_euclidean_a_negative_b_zero():
    assert euclidean(-189, 0) == 189

def test_euclidean_both_negative():
    assert euclidean(-48, -18) == -6

def test_euclidean_a_negative_b_positive():
    assert euclidean(-48, 18) == 6

