import unittest
import itertools

class TestP5(unittest.TestCase):
	def test_1_for_1(self):
		self.assertEqual(1, smallest_multiple_of(range(1,2)))

	def test_2_for_1_thru_2(self):
		self.assertEqual(2, smallest_multiple_of(range(1,3)))

	def test_2520_for_1_thru_10(self):
		self.assertEqual(2520, smallest_multiple_of(range(1,11)))

	def test_232792560_for_1_thru_20(self):
		self.assertEqual(232792560, smallest_multiple_of(range(1,21)))

def gcd(a, b):
	# Euclid's algorithm
	while b:
		a, b = b, a % b
	return a

def lcm(a, b):
	return a*b//gcd(a,b)

def smallest_multiple_of(nums):
	if len(nums) == 1:
		return nums[0]
	if len(nums) == 2:
		return lcm(nums[0], nums[1])
	else:
		a = nums.pop()
		b = nums.pop()
		nums.append(lcm(a,b))
		return smallest_multiple_of(nums)


def brute_smallest_multiple_of(nums):
	step = max(nums)
	for multiple in itertools.count(start=step, step=step):
		multiples_found = [num for num in itertools.takewhile(lambda x: multiple%x==0, nums)]
		if len(multiples_found) == len(nums):
			return multiple


if __name__ == '__main__':
	print smallest_multiple_of(range(1,21))
	unittest.main()
