# Find sum of all numbers which are equal to the sum of the factorial of their digits

import math

def find_numbers_equal_to_sum_of_factorial_of_its_digits():
    factorial_cache = {str(i) : math.factorial(i) for i in range(10)}
    for num in range(10,10**7):
        if sum([factorial_cache[digit] for digit in str(num)]) == num:
            yield num

def solve_p34():
    return sum(find_numbers_equal_to_sum_of_factorial_of_its_digits())

if __name__ == '__main__':
    print(solve_p34())
