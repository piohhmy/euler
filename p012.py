from nose.tools import *
from nose_parameterized import parameterized
import itertools
import math

def triangle_iter():
    total = 0
    for num in itertools.count(1):
        total += num
        yield total

def find_divisors(num):
    divisors = set(i for i in xrange(1, int(math.sqrt(num)+1)) if num%i == 0)
    divisors.update(set(num/i for i in divisors))
    return divisors

def find_first_triangle_w_500_divisors():
    for triangle in triangle_iter():
        num_of_divisors = len(find_divisors(triangle))
        if num_of_divisors > 500:
            return triangle


@parameterized([(1, 1),
                (2, 3),
                (3, 6),
                (4, 10),
                (5, 15),
                (6, 21),
                (7, 28)])
def test_triangle_numbers(input, expected_output):
    it = triangle_iter()
    for i in range(input):
        actual_output = it.next()

    assert_equal(actual_output, expected_output)

@parameterized([(1, set((1,))),
                (3, set((1,3))),
                (6, set((1,2,3,6))),
                (10, set((1,2,5,10)))])
def test_find_divisors(input, expected_output):
    actual_output = find_divisors(input)
    assert_equal(actual_output, expected_output)


if __name__ == '__main__':
    print find_first_triangle_w_500_divisors()
