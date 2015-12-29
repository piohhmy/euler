from itertools import *
from functools import reduce
import math
import operator


def find_champernowne_for(digit):
    c = 0
    counter = count(1)
    while c<digit:
        n = next(counter)
        length = (int(math.log10(n))+1)
        c += length
    index = length-(c-digit)-1
    return int(str(n)[index])

def solve_p040():
    numbers = [find_champernowne_for(x) for x in (1,10,100,1000,10000,100000)]
    return reduce(operator.mul, numbers)

def build_champernowne(limit):
    c = ''
    x = 1
    while len(c) < limit:
        c += str(x)
        x +=1
    return c

def build_up_to(builder, limit):
    a = ''
    while True:
        a = next(builder)
        if len(a) > limit:
            return a

def solve_p040_slow():
    a = build_champernowne(1000000)
    return int(a[0]) * int(a[9]) * int(a[99]) * int(a[999]) * int(a[9999]) * int(a[99999]) * int(a[999999])

