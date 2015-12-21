import math
from timeit import Timer


def solve_p10_sieve():
    return sum(sieve_primes_up_to(2000000))

def solve_p10_sieve_w_generator():
    return sum(prime_sieve_generator(2000000))

def sieve_primes_up_to(num):
    num_list = list(range(num))
    num_list[1] = 0 # cross out 1, special case
    i = 2

    while num_list[i] <= int(math.sqrt(num))+1:
        cross_out_composite_multiples(num_list[i], num_list)
        i = next_non_crossed_out_index(i, num_list)

    return [x for x in num_list if x != 0]

def cross_out_composite_multiples(multiple, num_list):
    for composite in range(multiple*2, len(num_list), multiple):
        num_list[composite] = 0

def prime_sieve_generator(limit):
    num_list = [True] * limit
    num_list[0] = num_list[1] = False
    square_root_limit = int(math.sqrt(limit))+1
    for i, isprime in enumerate(num_list):
        if isprime:
            yield i
            if i > square_root_limit:
               continue #optimization, composites already marked
            for composite in range(i*2, len(num_list), i):
                num_list[composite] = False



def next_non_crossed_out_index(i, num_list):
    increment_index = True
    while increment_index:
        i += 1
        increment_index = num_list[i] == 0
    return i

if __name__ == '__main__':
    sieve_timer = Timer(solve_p10_sieve)
    sieve_generator_timer = Timer(solve_p10_sieve_w_generator)
    print("Filter approach: {0}".format(sieve_timer.timeit(1)))
    print("Generator approach: {0}".format(sieve_generator_timer.timeit(1)))

    print(solve_p10_sieve())
    print(solve_p10_sieve_w_generator())

