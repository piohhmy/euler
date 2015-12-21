import itertools
import operator

def memoize(func):
    memoized = {}
    def wrapper(*args):
        if args not in memoized:
            memoized[args] = func(*args)
        return memoized[args]

    return wrapper


@memoize
def is_prime(num):
    if num < 0:
        return False
    return not any((num%x==0 for x in range(2, int(num**.5)+1)))

def quadratic_generator(a_limit, b_limit):
    for a in range(-a_limit+1, a_limit):
        for b in range(-b_limit+1, b_limit):
            yield (lambda n : n**2 + a*n + b, a, b)

def solve_p027():
    max_primes = 0
    answer = 0
    for func, a, b in quadratic_generator(1000,1000):
        consec_primes = len(list(itertools.takewhile(lambda x: is_prime(func(x)), itertools.count())))
        if consec_primes > max_primes:
            max_primes = consec_primes
            answer = a*b

    return answer

if __name__ == '__main__':
    print(solve_p027())

