import itertools

def fib(i):
	if i == 1: return 1
	if i == 2: return 2
	return fib(i-1) + fib(i-2)

def iseven(x):
	return x % 2 == 0	

def fibs_that_calc_less_than(max):
	return itertools.takewhile(lambda x: x < max, itertools.imap(fib, itertools.count(1)))

def functional_solver():
	return sum(filter(iseven, fibs_that_calc_less_than(4000000)))

def primitve_loop_solver():
	x = 1
	total = 0

	while(True):
		result = fib(x)
		if result > 4000000:
			break
		if result % 2 == 0:
			total += result
		x +=1
	return total


from timeit import Timer

def time_impls():
	solvers = [primitve_loop_solver, functional_solver]
	for solver in solvers:
		t = Timer(solver)
		print t.timeit(number=1)



def test_primitive_solver():
	assert primitve_loop_solver(), 4613732

def test_functional_solver():
	assert functional_solver(), 4613732



