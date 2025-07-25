import random

def sieve_of_eratosthenes(n: int):
    """Käy läpi ja seuloo Erathosteneen seulalla kaikki alkuluvut väliltä 0-n.

    Args:
        n (int): Yläraja etsittäville alkuluvuille.

    Returns:
        list[int]: Löydetyt alkuluvut listaformaatissa"""
    
    if n <= 1:
        raise ValueError("Input must be greater than 1")

    numbers_to_n = [True] * (n + 1)
    primes = []
    p = 2

    numbers_to_n[0] = False
    numbers_to_n[1] = False

    for p in range(2, n + 1):
        if numbers_to_n[p] == True:
            for multiple in range(p * p, n + 1, p):
                numbers_to_n[multiple] = False

    for i, value in enumerate(numbers_to_n):
        if value == True:
            primes.append(i)

    return primes

def miller_rabin(n: int, k: int):
    """Testaa onko luku 2 tai sitä suurempi pariton luku todennäköisesti alkuluku.
    
    Args:
        n (int): Testattava pariton luku, kun n > 2.
        k (int): Haluttu testikierrosten määrä.
        
    Returns:
        True, jos luku on todennäköisesti alkuluku.
        False, jos luku ei varmasti ole alkuluku"""
    
    if k <= 0:
        raise ValueError("k must be greater than 0")
    if n < 2:
        raise ValueError("n must be greater than 1")
    if n in [2, 3]:
        return True
    if n % 2 == 0:
        return False
    
    d = n - 1
    s = 0

    while d % 2 == 0:
        d = d // 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue

        else:
            for _ in range(s):
                y = pow(x, 2, n)
                if y == 1 and x != 1 and x != n - 1:
                    return False
                
                x = y
            if y != 1:
                return False
        
    return True

def euclidean(a: int, b: int):
    """Etsii suurimman yhteisen tekijän luvuille a ja b.

    Args:
        a (int): Testattava kokonaisluku.
        b (int): Testattava kokonaisluku.
        
    Returns:
        int: Palauttaa kokonaisluvun, joka on suurin yhteinen tekijä."""
    
    if a == b == 0:
        raise ValueError("Both values cannot be 0")
    if a == 0:
        return abs(b)
    if b == 0:
        return abs(a)
    
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def extended_euclidean(a: int, b:int):
    """Laskee kokonaisluvuille a ja b Bezoutin kertoimet x ja y siten, että a * x + b * y = gcd(a, b).

    Args:
        a (int): Laskennassa käytettävä kokonaisluku.
        b (int): Laskennassa käytettävä kokonaisluku.

    Returns:
        Tuple[x: int, y: int]: Bezoutin kertoimet tuplena.
    """

    if a == b == 0:
        raise ValueError("Both values cannot be 0")

    s = 0
    old_s = 1
    r = b
    old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s

    if b != 0:
        bezout_t = (old_r - old_s * a) // b
    
    else:
        bezout_t = 0

    return (old_s, bezout_t)