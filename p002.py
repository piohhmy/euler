import itertools
from timeit import Timer

def memoize(func):
    memoized_results = {}

    def wrapper(*args):
        if args not in memoized_results:
            memoized_results[args] = func(*args)
        return memoized_results[args]
            
    return wrapper



@memoize
def fib_finder(i):
    """ Finds fibonacci recursively for any given index """
    if i == 1: return 1
    if i == 2: return 2
    return fib_finder(i-1) + fib_finder(i-2)



def fib_generator():
    """ Iterative generator for all fibonacci numbers """
    last = 1
    curr = 2 
    yield last

    while True:
        yield curr
        next = curr + last
        last, curr = curr, next


def fib_generator_recursive(curr=2, prev=1):
    """ Recursive generator for all fib numbers """
    if curr == 2:
        yield 1
        yield 2
    next = curr + prev
    yield next
    for val in fib_generator_recursive(next, curr):
        yield val


def fibs_less_than(max):
    return itertools.takewhile(lambda x: x < max, map(fib_finder, itertools.count(1)))

def p2_recursive():
    return sum([x for x in fibs_less_than(4000000) if x % 2 == 0])

def p2_iterative_generator():
    return sum([x for x in itertools.takewhile(lambda x: x < 4000000, fib_generator()) if x % 2 == 0])  

def p2_recursive_generator():
    return sum([x for x in itertools.takewhile(lambda x: x < 4000000, fib_generator_recursive()) if x % 2 == 0])  

def p2_primitve():
    x = 1
    total = 0

    while(True):
        result = fib_finder(x)
        if result > 4000000:
            break
        if result % 2 == 0:
            total += result
        x +=1
    return total



def time_impls():
    runs = 1000
    solvers = [p2_recursive, p2_iterative_generator, p2_recursive_generator, p2_primitve]
    for solver in solvers:
        t = Timer(solver)
        assert solver() == 4613732
        print("%d runs of %s solved in %f seconds" % (runs, solver.__name__, t.timeit(number=1000)))

if __name__ == '__main__':
    time_impls()