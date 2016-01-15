'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
from itertools import count

def composite_odds():
    for i in count(9,2):
        if next((n for n in range(3,int(i**.5)+1) if i%n==0), None):
            yield i

def twice_a_squares(less_than):
    for i in count(1):
        square2 = i**2 * 2
        if square2 < less_than:
            yield square2
        else:
            break

def is_prime(n):
    divisor = next((i for i in range(2, int(n**.5)+1) if n%i == 0), None)
    return divisor is None

def solve_p046():
    try:
        for co in composite_odds():
            next(ts for ts in twice_a_squares(less_than=co) if is_prime(co-ts))
    except StopIteration:
        return co
