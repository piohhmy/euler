'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

from functools import reduce
import operator

def solve_p048():
    numsToAdd = (num**num for num in range(1,1001))
    return str(reduce(operator.add, numsToAdd))[-10:]
    
    

