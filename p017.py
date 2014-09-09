"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

singles = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
tens = {11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
doubles = {10:"ten", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy",80:"eighty", 90:"ninety"}

from nose.tools import *
from nose_parameterized import parameterized

def write_num(num):
    if num < 100:
        return write_1_thru_99(num)
    elif num  % 100 == 0 and num < 1000:
        hundred = int(str(num)[0])
        return singles[hundred] + " hundred"
    elif num < 1000:
        hundred = int(str(num)[0])
        double = int(str(num)[1:])
        return singles[hundred] + " hundred and " + write_1_thru_99(double)
    elif num == 1000:
        return "one thousand"
    else:
        raise ValueError(num)

def write_1_thru_99(num):
    if num <= 0 or num >= 100:
        raise ValueError(num)
    if num < 10: 
        return singles[num]
    elif num < 20 and num > 10:
        return tens[num]

    ten = int(str(num)[0]) * 10
    one = int(str(num)[1])
    if num % 10 == 0:
        return doubles[ten]
    else:
        return doubles[ten] + " " + singles[one]

def solve_p17():
    written_nums = [write_num(x) for x in xrange(1,1001)]
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
    print solve_p17()
