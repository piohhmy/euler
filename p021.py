"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from nose.tools import *
import math
def test_divisors_of():
    assert_equal(set([1,2,4,5,10,11,20,22,44,55,110]), divisors_of(220))

def test_find_amicable_pair_match():
    assert_true(has_amicable_pair(220))

def test_find_amicable_pair_no_match():
    assert_false(has_amicable_pair(10))

def has_amicable_pair(num):
    sum_of_divisors = sum(divisors_of(num))
    if sum(divisors_of(sum_of_divisors)) == num and sum_of_divisors != num:
        return True

def divisors_of(num):
    return set([i for i in xrange(1, num//2+2) if num%i==0])

def solve_p21():
    return sum([num for num in xrange(1,10001) if has_amicable_pair(num)])

if __name__ == '__main__':
    print solve_p21()
