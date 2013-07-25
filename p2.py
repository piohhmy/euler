import itertools

def fib(i):
	if i == 1: return 1
	if i == 2: return 2
	return fib(i-1) + fib(i-2)


def count_till_max():
	count = 1
	while True:
		if fib(count) < 4000000:
			yield count
		else:
			break
		count += 1

def iseven(x):
	return x % 2 == 0	

def fib_indexes_that_calc_less_than(max):
	return itertools.takewhile(lambda x: fib(x) < max, itertools.count(1))

def fibs_that_calc_less_than(max):
	return itertools.takewhile(lambda x: x < max, itertools.imap(fib, itertools.count(1)))


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

def primitive_functional_hybrid_solver():
	return sum(filter(lambda x: x % 2 == 0, [fib(x) for x in count_till_max()]))

def functional_double_call_solver():
	return sum(filter(iseven, [fib(x) for x in fib_indexes_that_calc_less_than(4000000)]))

def functional_solver():
	return sum(filter(iseven, fibs_that_calc_less_than(4000000)))



from timeit import Timer

def time_impls():
	solvers = [primitve_loop_solver, primitive_functional_hybrid_solver, functional_double_call_solver, functional_solver]
	for solver in solvers:
		t = Timer(solver)
		print t.timeit(number=1)



def test_p2():
	assert fib_counter(), 4613732

def test_p2_2():
	assert fib_generator(), 4613732



