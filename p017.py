"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

singles = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
tensomethings = {10: "ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
tens = {11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
doubles = {10:"ten", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy",80:"eighty", 90:"ninety"}

from nose.tools import *
from nose_parameterized import parameterized

def write_num(num):
    digits = len(str(num))
    if digits == 1:
        return convert_single_digit(num)
    elif digits == 2:
        return convert_double_digits(num)
    elif digits == 3:
        return convert_triple_digits(num)
    elif num == 1000:
        return "one thousand"
    else:
        raise ValueError(num)

def convert_single_digit(num):
    if num < 1 or num > 9:
        raise ValueError(num)
    return singles[num]

def convert_double_digits(num):
    if num < 10 or num > 99:
        raise ValueError(num)

    if num < 20:
        return tensomethings[num]
    else:
        ones_digit = num % 10
        if ones_digit == 0:
            return doubles[num]
        else:
            return doubles[(num/10)*10] + " " + write_num(ones_digit)

def convert_triple_digits(num):
    hundreds_digit = num % 100
    if hundreds_digit == 0:
        return write_num(num/100) + " hundred"
    else:
        double = int(str(num)[1:])
        return write_num(num/100) + " hundred and " + write_num(double)


def solve_p17():
    written_nums = [write_num(x) for x in range(1,1001)]
    return len(reduce(lambda x,y: x + y, written_nums).replace(" ", ""))
# Tests

@parameterized([(1, "one"),
                (2, "two"),
                (10, "ten"),
                (11, "eleven"),
                (20, "twenty"),
                (21, "twenty one"),
                (25, "twenty five"),
                (49, "forty nine"),
                (101, "one hundred and one"),
                (149, "one hundred and forty nine"),
                (950, "nine hundred and fifty"),
                (300, "three hundred"),
                (1000, "one thousand"),
                (100, "one hundred")])
def test_write_num(num, expected):
    assert_equal(expected, write_num(num))

if __name__ == '__main__':
    print(solve_p17())
