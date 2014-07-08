import math
def is_prime(x):
    for y in range(2,int(math.sqrt(x)) + 1):
        if x % y == 0:
            return False
    return True

def solve_p10():
    return sum([x for x in xrange(2, 2000000) if is_prime(x)])

if __name__ == '__main__':
    print solve_p10()
