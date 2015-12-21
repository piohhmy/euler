import unittest
import math

class TestP6(unittest.TestCase):
	def test_sum_of_squares_first_10(self):
		self.assertEqual(385, sum_of_squares(list(range(1,11))))

	def test_square_of_sums_first_10(self):
		self.assertEqual(3025, square_of_sums(list(range(1,11))))

	def test_difference_first_10(self):
		self.assertEqual(2640, sum_square_difference(list(range(1,11))))

def sum_of_squares(nums):
	return sum([num**2 for num in nums])

def square_of_sums(nums):
	return sum(nums)**2

def sum_square_difference_brute(nums):
	return square_of_sums(num) - sum_of_squares(nums) 

if __name__ == '__main__':
	print(sum_square_difference(list(range(1,101))))
	unittest.main()