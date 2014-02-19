def solve_p3():
	leftnums = range(100, 1000)
	rightnums = range(100, 1000)

	products = [left*right for left in leftnums for right in rightnums]
	return max(filter(is_palindrome, products))

def is_palindrome(num):
	orig = str(num)
	rev = orig[::-1]
	return orig == rev
