import math
def is_prime(x):
    for y in range(2,int(math.sqrt(x)) + 1):
        if x % y == 0:
            return False
    return True

def solve_p10():
    return 2 + sum([x for x in xrange(3, 2000000, 2) if is_prime(x)])

def solve_p10_sieve():
    total = range(2,2000000)
    x = 0
    curr = 2

    while curr < int(math.sqrt(2000000))+1:
        for composite in xrange(2*curr, 2000000, curr):
            total[composite-2] = 0 
        x = x + 1
        while total[x] == 0:
            x = x+1
        curr = total[x]
    return sum(total)


if __name__ == '__main__':
    print solve_p10_sieve()
