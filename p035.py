from collections import deque

def is_prime(num):
    for i in range(2, int(num**.5)+1):
        if num % i == 0:
            return False
    return True


def is_circular_prime(num):
    num = deque(str(num))
    
    for _ in range(len(num)):
        if not is_prime(int("".join(num))):
            return False
        num.rotate(1)
    return True


def solve_p35():
    return len([num for num in range(2, 1000000) if is_circular_prime(num)])

if __name__ == '__main__':
    print(solve_p35())
    

