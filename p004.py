import itertools
from timeit import Timer

def solve_p3_combinations():
    products = [left*right for (left, right) in itertools.combinations(range(100,1000), 2)]
    print max(filter(is_palindrome, products))

def solve_p3_permutations():
    products = [left*right for (left, right) in itertools.permutations(range(100,1000), 2)]
    print max(filter(is_palindrome, products))

def solve_p3_nested_list_comprehension():
    nums = range(100, 1000)
    products = [left*right for left in nums for right in nums]
    print max(filter(is_palindrome, products))

def is_palindrome(num):
    orig = str(num)
    rev = orig[::-1]
    return orig == rev

if __name__ == '__main__':
    for solver in (solve_p3_permutations, solve_p3_nested_list_comprehension, solve_p3_combinations):
        t = Timer(solver)
        seconds = t.timeit(number=1)
        print "%s solved in %s seconds"  % (solver, seconds)

