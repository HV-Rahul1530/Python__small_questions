numbers = [1, 2, 3, 4, 5]

# Using map to square each number
squared_numbers = list(map(lambda x: x * x, numbers))

# Using filter to keep even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

from functools import reduce
# Using reduce to calculate the product of all numbers
product = reduce(lambda x, y: x * y, numbers)

print(even_numbers)
print(product)
print(squared_numbers)