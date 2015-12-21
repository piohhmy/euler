import math

	
def find_factors(num):
	return set([factor for x in range(1, int((math.sqrt(num)+1))) for factor in (x, num//x) if num % x == 0])

def is_prime(num):
	for x in range(2, int(math.sqrt(num)) +1):
		if num%x == 0:
			return False
	return True

def find_prime_factors(num):
	return list(filter(is_prime, find_factors(num)))

def solve_p3():
	return max(find_prime_factors(600851475143))

if __name__ == '__main__':
    print(solve_p3())
