import math

	
def find_factors(num):
	return set([factor for x in xrange(1, int((math.sqrt(num)+1))) for factor in (x, num//x) if num % x == 0])

def is_prime(num):
	for x in xrange(2, int(math.sqrt(num)) +1):
		if num%x == 0:
			return False
	return True

def find_prime_factors(num):
	return filter(is_prime, find_factors(num))

def solve_p3():
	return max(find_prime_factors(600851475143))