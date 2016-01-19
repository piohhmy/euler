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


def solve_p047():
    solver = PrimeLazySolver()
    limit = 1000000
    nums = [0] * limit
    seq_length = 4
    for prime in solver.primes_up_to(limit):
        multiplier = 2
        while prime * multiplier < limit:
            nums[prime * multiplier] += 1
            multiplier += 1

    for i, num in enumerate(nums):
        if all(nums[i + x] >= seq_length for x in range(1, seq_length + 1)):
            return i + 1
