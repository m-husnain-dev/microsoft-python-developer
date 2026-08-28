def fibonacci_sequence():
	"""A generator that generates the Fibonacci sequence."""
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b


# Generate the first 10 Fibonacci numbers
fib_gen = fibonacci_sequence()
for i in range(10): 
    print(next(fib_gen))   
