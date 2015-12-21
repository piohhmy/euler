def sum_of_digits_raised(num, power):
    return sum([int(x)**power for x in str(num)])

def solve_p030():
    return  sum([num for num in range(2, 1000000) if sum_of_digits_raised(num, 5) == num])

if __name__ == '__main__':
    print(solve_p030())

