def concat_multiples(num, multiples):
    return int("".join([str(num*multiple) for multiple in range(1,multiples+1)]))

def is_pandigital(num):
    return sorted([int(digit) for digit in str(num)]) == range(1,10):
    

def solve_p038():
    # retrieve only 9 digit concatinations of multiples where n = (1,2,..n)
    n6 = [concat_multiples(num, 6) for num in [3]]
    n5 = [concat_multiples(num, 5) for num in range(5,10)]
    n4 = [concat_multiples(num, 4) for num in range(25,33)]
    n3 = [concat_multiples(num, 3) for num in range(100,333)]
    n2 = [concat_multiples(num, 2) for num in range(5000,9999)]

    all_concats = set(n2 + n3 + n4 + n5 + n6)
    return max([num for num in all_concats if is_pandigital(num)])

if __name__ == '__main__':
    print(solve_p038())
