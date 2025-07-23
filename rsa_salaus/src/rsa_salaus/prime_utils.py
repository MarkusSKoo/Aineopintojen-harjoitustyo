import random

def sieve_of_eratosthenes(n):
    """Käy läpi ja seuloo Erathosteneen seulalla kaikki alkuluvut väliltä 0-n.

    Args:
        n (int): Yläraja etsittäville alkuluvuille.

    Returns:
        list[int]: Löydetyt alkuluvut listaformaatissa"""
    
    if n <= 1:
        return "Input must be greater than 1"

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

def miller_rabin(n, k):
    """Testaa onko luku 2 tai sitä suurempi pariton luku todennäköisesti alkuluku.
    
    Args:
        n (int): Testattava pariton luku, kun n > 2.
        k (int): Haluttu testikierrosten määrä.
        
    returns:
        True, jos luku on todennäköisesti alkuluku.
        False, jos luku ei varmasti ole alkuluku"""
    
    if k <= 0:
        return "k must be greater than 0"
    if n in [2, 3, 5, 7]:
        return True
    if n < 2:
        return "n must be greater than 2"
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

        elif x != 1 and x != n-1:
            for _ in range(s):
                y = pow(x, 2, n)
                if y == 1 and x != 1 and x != n - 1:
                    return False
                
                x = y
            if y != 1:
                return False
        
    return True