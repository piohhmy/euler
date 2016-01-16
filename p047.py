import itertools

class PrimeLazySolver():
    def __init__(self):
        self.gen = self.prime_generator()
        self.primes = [next(self.gen)]

    def primes_up_to(self, limit):
        while self.primes[-1] < limit:
            self.primes.append(next(self.gen))

        return itertools.takewhile(lambda x: x < limit, self.primes)

    @staticmethod
    def prime_generator():
        for i in itertools.count(2):
            if not next((s for s in range(2, int(i**.5)+1) if i % s == 0), None):
                yield i
                

def has_factors(num, primes, factor_count):
    factors = (prime for prime in primes if num%prime == 0)
    first_n_factors = list(next(factors, None) for i in range(factor_count))
    return all(first_n_factors)

def is_prime_factor_seq(num, solver, seq_len):
    return all(has_factors(num+i, solver.primes_up_to(num//2+1), seq_len) for i in range(seq_len))


def solve_p047():
    solver = PrimeLazySolver()
    for n in itertools.count(1):
        if is_prime_factor_seq(n, solver, 4):
            return n
            
    
