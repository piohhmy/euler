from nose.tools import assert_equal
from nose_parameterized import parameterized
from itertools import count
from collections import Counter,defaultdict


def find_right_angle_sums():
    d = defaultdict(set)
    counter = Counter()
    for a in range(1,1000):
        for b in range(1,1000):
            c = (a**2 + b**2)**.5
            if c.is_integer() and (a + b + c) < 1000:
                d[a+b+c].add(tuple(sorted((a,b,c))))
    return d
            
            
def solve_p039():
    sums = find_right_angle_sums()
    return Counter({k:len(v) for k,v in sums.items()}).most_common(1)
    
if __name__ == '__main__':
    print(solve_p039())
