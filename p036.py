def is_palindrome(text):
    if text == text[::-1]:
        return True

def find_double_base_palindromes(limit):
    for num in range(1, limit):
        base2 = format(num, 'b')
        base10 = str(num)
        if is_palindrome(base2) and is_palindrome(base10):
            yield num

def solve_p036():
    return sum(find_double_base_palindromes(1000000))

if __name__ == '__main__':
    print(solve_p036())

