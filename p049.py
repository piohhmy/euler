'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?  '''

from itertools import permutations

def prime_sieve(up_to):
    nums = list(range(up_to))
    nums[0] = nums[1] = 0

    for num in nums[:int(up_to**.5)+1]:
        if num != 0:
            multiple = num+num
            while multiple < up_to:
                nums[multiple] = 0
                multiple += num

    return (prime for prime in nums if prime != 0)

def find_2_equal_diffs(it):
    if len(it) < 3:
        return None

    sorted_it = sorted(list(it))
    for i1, num1 in enumerate(sorted_it):
        for i2, num2 in  enumerate(sorted_it[i1+1:]):
            diff = num2-num1
            if num2 + diff in it:
                return (num1, num2, num2 + diff)
    return None


def find_matching_permutations(num, matchset):
    perms = set([int(''.join(p)) for p in permutations(str(num))])
    return perms.intersection(matchset)


def solve_p049():
    primes = [p for p in prime_sieve(10000) if p > 999]
    prime_sets = [find_matching_permutations(p, primes) for p in primes]
    return set([find_2_equal_diffs(p) for p in prime_sets if find_2_equal_diffs(p)])

