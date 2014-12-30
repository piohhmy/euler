def sum_of_digits_raised(num, power):
    return sum(map(lambda x: int(x)**power, str(num)))

def solve_p030():
    return  sum(filter(lambda num: sum_of_digits_raised(num, 5) == num,
                       xrange(2, 1000000)))

if __name__ == '__main__':
    print solve_p030()

