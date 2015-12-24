from itertools import *

def build_champernowne():
    c = ''
    for x in count(1):
        c += repr(x)
        yield c

def build_up_to(builder, limit):
    a = ''
    while True:
        a = next(builder)
        if len(a) > limit:
            return a


def solve_p040():
    builder = build_champernowne()
    a = build_up_to(builder, 1000000)
    return int(a[0]) * int(a[9]) * int(a[99]) * int(a[999]) * int(a[9999]) * int(a[99999]) * int(a[999999])



