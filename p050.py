'''
The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13 This is the longest sum of consecutive primes
    that adds to a prime below one-hundred.

    The longest sum of consecutive primes below one-thousand that adds to a
    prime, contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of the most
    consecutive primes?
'''

def prime_sieve(up_to):
    nums = list(range(up_to))
    not_prime = -1
    nums[0] = nums[1] = not_prime

    for num in nums[:int(up_to**.5)+1]:
        if num == not_prime:
            continue

        for mult in range(num*2, up_to, num):
            nums[mult] = not_prime
    return (num for num in nums if num != not_prime)


def find_consecutive_prime_sum(primes):
    longest_prime_seq_len = seq_len = 1
    i = 0
    prime_set = set(primes)
    primes_len = len(primes)

    while i < primes_len - seq_len + 1:
        prime_seq = primes[i:i+seq_len]
        prime_seq_sum = sum(prime_seq)
        if prime_seq_sum in prime_set:
            longest_prime_seq = prime_seq
            longest_prime_seq_len = len(prime_seq)

        if prime_seq_sum > primes[-1]:
            seq_len = longest_prime_seq_len + 1
            i += 1
        else:
            seq_len += 1

    return sum(longest_prime_seq)

def solve():
    primes = list(prime_sieve(1000000))
    return find_consecutive_prime_sum(primes)
