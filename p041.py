'''We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.  What is the largest n-digit pandigital prime that exists?'''

import itertools
import functools

def pandigital_generator(n):
    perms = itertools.permutations(range(1,n+1))
    for perm in perms:
        yield functools.reduce(lambda x,y: x*10 + y, perm)

def is_prime(n):
    for x in range(2,int(n**.5)+1):
        if n%x == 0:
            return False
    return True

def solve_p041():
    for n in range(9,0, -1):
        big_pandigitals = sorted(pandigital_generator(n), reverse=True)
        for pand in big_pandigitals:
            if is_prime(pand):
                return pand
