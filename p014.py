from nose.tools import *
# Collatz
#even: n -> n/2
#odd:  n -> n*3 + 1

def is_even(i):
    return i % 2 == 0

def memoize(func):
    memoized_results = {}
    def wrapper(*args):
        if args not in memoized_results:
            memoized_results[args] = func(*args)
        return memoized_results[args]
    return wrapper

@memoize
def collatz_recursive(start):
    if start == 1:
        return (1,)
    elif is_even(start):
        return (start,) + collatz_recursive(start/2)
    else:
        return (start,) + collatz_recursive(start*3 + 1)


memoized_results = {1:[1]}
def collatz_iterative_memoized(start):
    global memoized_results
    curr = start
    stack = []
    while True: 
        if curr not in memoized_results:
            stack.append(curr)
            if is_even(curr):
                curr /= 2
            else:
                curr = curr * 3 + 1
        else:
            for index, value in enumerate(stack):
                memoized_results[value] = stack[index:] + memoized_results[curr]
            break
    
    return memoized_results[start]

def collatz_iterative_slow(start):
    return [i for i in collatz_generator(start)]

def collatz_generator(start):
    while start != 1:
        if is_even(start):
            start /= 2
            yield start
        else:
            start = start * 3 + 1
            yield start

def test_collatz_13():
    assert_equal((13,40,20,10,5,16,8,4,2,1), collatz_iterative(13))

def solve_p014():
    collatz_lengths = [len(collatz_recursive(i)) for i in xrange(1,1000000)]
    return collatz_lengths.index(max(collatz_lengths)) + 1

def solve_p014_it():
    collatz_lengths = [len(collatz_iterative_memoized(i)) for i in xrange(1,1000000)]
    return collatz_lengths.index(max(collatz_lengths)) + 1

if __name__ == '__main__':
    print solve_p014_it()
