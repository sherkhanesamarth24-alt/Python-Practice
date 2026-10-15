# Lambda Functions

square = lambda x: x ** 2
add = lambda a, b: a + b

print("Square:", square(5))
print("Addition:", add(10, 20))

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print("Squares:", squares)
