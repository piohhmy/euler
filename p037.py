import itertools

def prime_generator(start=2):
    for x in itertools.count(start):
        if is_prime(x):
            yield x

def is_prime(num):
    if num <= 1:
        return False
    for x in range(2, int(num**.5)+1):
        if num % x == 0:
            return False
    return True

def truncated_slices(num):
    for x in range(1, len(str(num))):
        yield int(str(num)[:-x])
        yield int(str(num)[x:])
    
def truncatable_prime_generator():
    for prime in prime_generator(10): 
        if all((is_prime(truncation) for truncation in truncated_slices(prime))):
            yield prime

def solve_p037():
    return sum(itertools.islice(truncatable_prime_generator(), 11))

if __name__ == '__main__':
    print((solve_p037()))
