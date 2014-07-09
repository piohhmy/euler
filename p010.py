import math
from timeit import Timer


def solve_p10_sieve():
    return sum(sieve_primes_up_to(2000000))

def sieve_primes_up_to(num):
    num_list = range(num)
    num_list[1] = 0 # cross out 1, special case
    i = 2

    while num_list[i] <= int(math.sqrt(num))+1:
        cross_out_composite_multiples(num_list[i], num_list)
        i = next_non_crossed_out_index(i, num_list)

    return filter(lambda x: x != 0, num_list)

def cross_out_composite_multiples(multiple, num_list):
    for composite in xrange(multiple*2, len(num_list), multiple):
        num_list[composite] = 0 

def next_non_crossed_out_index(i, num_list):
    increment_index = True
    while increment_index:
        i += 1
        increment_index = num_list[i] == 0
    return i

if __name__ == '__main__':
    sieve_timer = Timer(solve_p10_sieve)
    print sieve_timer.timeit(1)

    print solve_p10_sieve()

