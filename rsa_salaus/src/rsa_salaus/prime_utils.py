def sieve_of_eratosthenes(n):
    """Käy läpi ja seuloo Erathosteneen seulalla kaikki alkuluvut väliltä 0-n.

    Args:
        n (int): Yläraja etsittäville alkuluvuille.

    Returns:
        list[int]: Löydetyt alkuluvut listaformaatissa"""

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