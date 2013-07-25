# 1, 2, 3, 5, 8, 13,
# 1, 2, 3, 4, 5, 6

import itertools


def fib(i):
    """ Finds fibinocci recursively for any given index """
    if i == 1: return 1
    if i == 2: return 2
    return fib(i-1) + fib(i-2)

def fib_gen():
    """ Iterative generator for all fib numbers """
    yield 1
    yield 2
    last2 = 1
    last = 2 
    for i in itertools.count(1):
        result = last + last2
        yield result
        last2 = last
        last = result

def fib_gen_recursive(prev=2, prev2=1):
    """ Recursive generator for all fib numbers """
    if prev == 2:
        yield 1
        yield 2
    result = prev + prev2
    yield result
    for val in fib_gen_recursive(prev=result, prev2=prev):
        yield val
    



def iterative_solver():
    return sum(filter(iseven, itertools.takewhile(lambda x: x < 4000000, fib_gen())))

def recurrsive_solver():
    return sum(filter(iseven, itertools.takewhile(lambda x: x < 4000000, fib_gen_recursive())))    

def test_fib_max():
    assert 1, fib_max(1)
    assert 2, fib_max(2)
    assert 3, fib_max(3)
    assert 3, fib_max(4)
    assert 5, fib_max(5)

def iseven(x):
    return x % 2 == 0   

def fibs_that_calc_less_than(max):
    return itertools.takewhile(lambda x: x < max, itertools.imap(fib, itertools.count(1)))

def functional_solver():
    return sum(filter(iseven, fibs_that_calc_less_than(4000000)))


def optimized_functional_solver():
    return sum(filter(iseven, fib_max(1, 4000000)))

def primitve_loop_solver():
    x = 1
    total = 0

    while(True):
        result = fib(x)
        if result > 4000000:
            break
        if result % 2 == 0:
            total += result
        x +=1
    return total


from timeit import Timer

def time_impls():
    solvers = [recurrsive_solver, iterative_solver]
    for solver in solvers:
        t = Timer(solver)
        print t.timeit(number=100)

def test_primitive_solver():
    assert primitve_loop_solver(), 4613732

def test_functional_solver():
    assert functional_solver(), 4613732



