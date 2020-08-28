# Eulers Totient function finds the number of relative primes of a number n from 1 to n
def totient(n: int) -> list:
    is_prime = [True for i in range(n + 1)]
    totients = [i - 1 for i in range(n + 1)]
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
        for prime in primes:
            if i * prime >= n:
                break
            is_prime[i * prime] = False

            if i % prime == 0:
                totients[i * prime] = totients[i] * prime
                break

            totients[i * prime] = totients[i] * (prime - 1)

    return totients


def test_totient() -> None:
    """
    >>> n = 10
    >>> totient_calculation = totient(n)
    >>> for i in range(1, n):
    ...     print(f"{i} has {totient_calculation[i]} relative primes.")
    1 has 0 relative primes.
    2 has 1 relative primes.
    3 has 2 relative primes.
    4 has 2 relative primes.
    5 has 4 relative primes.
    6 has 2 relative primes.
    7 has 6 relative primes.
    8 has 4 relative primes.
    9 has 6 relative primes.
    """
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
