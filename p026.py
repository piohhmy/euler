''' Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.

* For fraction m/n, longest possible recurring cycle is n-1
* Euler's totient function (phi)     is the number of integers that are coprime
  (i.e., do not contain any factor in common with) with n, for numbers 1-n, 1 is coprime with all numbers
* For fraction m/n, if n is coprime with 10 then longest possible recurring cycle is phi n
* multiplicative order: given integer a and n, with gcd(a,n) = 1, multiplicative order of n is smallest
positive integer k with a^k = 1 (mod n).
The powers of 4 modulo 7 are as follows:


4^0 = 1    = 0 * 7 + 1 == 1(mod 7)
4^1 = 4    = 0 * 7 + 4 == 4(mod 7)
4^2 = 16   = 2 * 7 + 2 == 2(mod 7)
4^3 = 64   = 9 * 7 + 1 == 1(mod 7)
4^4 = 256  = 36 * 7 + 4 == 4(mod 7)
4^5 = 1024 = 146 * 7 + 2 == 2(mod 7)

The smallest positive integer k such that 4^k = 1 (mod 7) is 3, so the multiplicative order of 4 modulo 7 = 3.

* For fraction m/n, the number of digits in the recurring cycle can be found directly by the multiplicative order of n
'''
from nose.tools import *
from nose_parameterized import parameterized
from itertools import count
import itertools
from decimal import *
import operator

getcontext().rounding = ROUND_DOWN

def solve_p26():
    repeating_cycles = {d: len(repeating_cycle_of_fraction(d)) for d in xrange(1,1001)}
    divisor_w_longest_cycle, period = max(repeating_cycles.items(), key=operator.itemgetter(1))
    return divisor_w_longest_cycle


def repeating_cycle_of_fraction(divisor):
    getcontext().prec = divisor*3
    result = str(1/Decimal(divisor))
    repeatingcycle = result[divisor+2:]

    for x in xrange(2, len(repeatingcycle), 2):
        substr = repeatingcycle[:x]
        if substr[:x/2] == substr[x/2:]:
            if is_cyclic(substr[:x/2], repeatingcycle):
                return substr[:x/2]
    return ""

def is_cyclic(cycle, word):
    if cycle not in word:
        return False
    cycle_start = word.index(cycle)

    c = itertools.cycle(cycle)
    forward = all(n == c.next() for n in word[cycle_start:])

    rev_c = itertools.cycle(cycle[::-1])
    backward = all(n == rev_c.next() for n in word[:cycle_start][::-1])

    return forward and backward


def test_solve_p026():
    assert_equal(983, solve_p26())

@parameterized([(True, '123', '123123123'),
                (False, '1234', '12121212'),
                (True, '123', '231231231'),
                (False, '123', '33123123'),
                (True, '1', '111111111'),
                (True, '428571', '42857142857142')])
def test_is_cyclic(expected, cycle, word):
    assert_equal(expected, is_cyclic(cycle, word))


@parameterized([(0,2), (1, 3), (0,4), (1,6), (6,7), (2, 11), (22,23), (16,34),
                (982, 983)])
def test_dec_period(expected, divisor):
    assert_equal(expected, len(repeating_cycle_of_fraction(divisor)))


def m_order(a, n):
    return next(k for k in xrange(1,n) if a**k % n == 1)

def test_order_of_4_modulo_7():
    assert_equal(3, m_order(4,7))

def test_order_of_2_modulo_7():
    assert_equal(3, m_order(2,7))

def test_order_of_2_modulo_11():
    assert_equal(10, m_order(2,11))
