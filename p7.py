import unittest
import itertools
import math


def is_prime(num):
    return all(num % x != 0 for x in xrange(2, int(math.sqrt(num)+1)))

def prime_generator():
    return (num for num in itertools.count(2) if is_prime(num))

def calc_prime(num):
	return next(itertools.islice(prime_generator(), num-1, None))


class TestP7(unittest.TestCase):
    def test_6th_prime(self):
        self.assertEqual(13, calc_prime(6))
if __name__ == '__main__':
	import time
	start = time.time()
	print calc_prime(10001)
	print "total secs: %f" % (time.time() - start)
	unittest.main()