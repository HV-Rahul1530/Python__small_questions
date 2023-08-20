#A simple generator for Fibonacci Numbers
def fib(limit):
	
	# Initialize first two Fibonacci Numbers
	a, b = 0, 1

	# One by one yield next Fibonacci Number
	while a < limit:
		yield a
		a, b = a+b , sum(a, b)

# Create a generator object
x = fib(10)

# Iterating over the generator object using next
# In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# Iterating over the generator object using for
# in loop.


class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        if n == 1 or n == 2:
            return 1
        lst = [0, 1]
        a , b = 2 , 3
        while len(lst) <= n:
          a, b = b, a+b
          lst.append(b)
        return max(lst)
	

