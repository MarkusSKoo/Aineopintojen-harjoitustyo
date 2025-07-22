import pytest
from src.rsa_salaus.prime_utils import sieve_of_eratosthenes, miller_rabin

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
    assert miller_rabin(8, 1) == "n must be an odd number"

def test_miller_rabin_small_k():
    assert miller_rabin(3, 0) == "k must be greater than 0"

def test_miller_rabin_199():
    numbers = sieve_of_eratosthenes(200)
    for number in numbers:
        assert miller_rabin(number, 10) == True

def test_miller_rabin_middle():
    numbers = [7727, 7741, 7753, 7757, 7759, 7789, 7793, 7817, 7823, 7829, 7841, 7853, 7867, 7873, 7877, 7879, 7883, 7901, 7907, 7919]
    for number in numbers:
        assert miller_rabin(number, 10) == True

def test_miller_rabin_large():
    numbers = [611693, 611707, 611729, 611753, 611791, 611801, 611803, 611827, 611833, 611837, 611839, 611873, 611879, 611887, 611903, 611921, 611927, 611939, 611951, 611953]
    for number in numbers:
        assert miller_rabin(number, 10) == True

def test_miller_rabin_not_primes():
    primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
    127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
    179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
    233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
    283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
    353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
    419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
    467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
    547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
    607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
    661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
    739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
    811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
    877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
    947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013,
    1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069,
    1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151,
    1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223
]

    numbers = []
    for i in range(3, 1223):
        if i % 2 != 0:
            if i not in primes:
                numbers.append(i)

    for number in numbers:
        assert miller_rabin(number, 10) == False

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
        assert miller_rabin(number, 10) == False

