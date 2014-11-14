"""
What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

def solve_p025():
    for i, num in enumerate(fib_generator()):
        if len(str(num)) == 1000:
            return i + 1

def fib_generator():
    prev = 1
    curr = 1
    yield prev
    while True:
        yield curr
        prev, curr = curr, prev + curr

if __name__ == '__main__':
    print solve_p025()