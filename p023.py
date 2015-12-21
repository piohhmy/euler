"""A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number. A
number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n. As 12 is the smallest abundant
number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the
sum of two abundant numbers is 24. By mathematical analysis, it can be shown
that all integers greater than 28123 can be written as the sum of two abundant
numbers. However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed as
the sum of two abundant numbers is less than this limit. Find the sum of all
the positive integers which cannot be written as the sum of two abundant
numbers."""

from nose.tools import *
import itertools
import math


def solve_p023():
    abundants = list(filter(is_abundant, range(1,28124)))
    abundant_combos = itertools.combinations_with_replacement(abundants, 2)
    abundant_sums = {sum(combo) for combo in abundant_combos}
    return sum([i for i in range(1, 28124) if i not in abundant_sums])

def find_divisors(num):
    divisors = {i for i in range(1, int(math.sqrt(num)+1)) if num%i == 0}
    divisors.update({num/divisor for divisor in divisors})
    divisors.discard(num)
    return divisors

def is_abundant(num):
    divisors = find_divisors(num)
    return sum(divisors) > num


def test_28_is_not_abundant():
    assert_false(is_abundant(28))

def test_8_is_not_abundant():
    assert_false(is_abundant(8))

def test_12_is_abundant():
    assert_true(is_abundant(12))

if __name__ == '__main__':
    print(solve_p023())
    