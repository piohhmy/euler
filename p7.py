import unittest
import itertools
import math

class TestP7(unittest.TestCase):
	def test_6th_prime(self):
		self.assertEqual(13, calc_prime(6))

def is_prime(num):
	for x in xrange(2, int(math.sqrt(num)+1)):
		if num % x == 0: 
			return False	
	return True

def prime_generator():
    return (num for num in itertools.count(2) if is_prime(num))

def calc_prime(num):
	return next(itertools.islice(prime_generator(), num-1, None))

if __name__ == '__main__':
	import time
	start = time.time()
	print calc_prime(10001)
	print "total secs: %f" % (time.time() - start)
	unittest.main()