def find_digit_canceling_fractions():
    for numerator in range(10,100):
        for denominator in range(10,100):
            for num_digit in str(numerator):
                for denom_digit in str(denominator):
                    if num_digit == denom_digit and "0" not in str(denominator) and numerator/float(denominator) < 1:
                        try:
                            simplified_numer = float(str(numerator).replace(num_digit, "", 1))
                            simplified_denom = float(str(denominator).replace(denom_digit, "", 1))
                            if simplified_numer/simplified_denom == numerator/float(denominator):
                                yield (numerator, denominator)
                        except ZeroDivisionError:
                            pass

def gcd(a, b):
    # Euclid's algorithm
    while b:
        a, b = b, a % b
    return a


def solve_p033():
    numerator = 1
    denominator = 1
    for numer, denom in find_digit_canceling_fractions():
        numerator = numerator * numer
        denominator = denominator * denom

    common = gcd(numerator, denominator)
    return denominator/common


if __name__ == '__main__':
    print(solve_p033())
