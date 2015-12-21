import math

def solve_p9():
    for a in range(1,500):
        for b in range(a+1,500):
            c = math.sqrt(a**2 + b**2)
            if (a + b + c == 1000) and (a**2 + b**2 == c**2):
                return a*b*c


if __name__ == '__main__':
    print(solve_p9())

