def pandigital_generator():
    for perm in itertools.permutations(range(0,10)):
        if perm[0] != 0:
            yield functools.reduce(lambda x,y: x*10 + y, perm)

def prime_generator():
    yield 2
    yield 3
    yield 5
    yield 7
    yield 11
    yield 13
    yield 17

def has_p043_property(n):
    n_str = str(n)
    primes = prime_generator()
    return all(int(n_str[d:d+3]) % next(primes) == 0 for d in range(1, 8))

def solve_p043():
    return sum(p for p in pandigital_generator() if has_p043_property(p))

