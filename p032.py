
def find_pandigital_products():
    pandigital = set(range(1,10))

    for multiplicand in xrange(1,100):
        # find min/max multipliers that will produce a product of only 4 digits
        max_multiplier = 10**4/multiplicand
        min_multiplier = 1000 if multiplicand < 10 else 100
        for multiplier in xrange(min_multiplier, max_multiplier):
            product = multiplicand * multiplier
            numbers = (product, multiplicand, multiplier)
            all_digits = {int(digit) for number in numbers
                                     for digit in str(number)}
            if all_digits == pandigital:
                yield product

def solve_p032():
    return sum(set(find_pandigital_products()))

if __name__ == '__main__':
    print solve_p032()

