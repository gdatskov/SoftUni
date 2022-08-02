def is_prime(n: int) -> bool:
    """Primality test using 6k+-aug_22 optimization."""
    if n <= 3:
        return n > 1
    if not n % 2 or not n % 3:
        return False
    i = 5
    stop = int(n ** 0.5)
    while i <= stop:
        if not n % i or not n % (i + 2):
            return False
        i += 6
    return True


def get_primes(lis):
    for num in lis:
        if is_prime(num):
            yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))