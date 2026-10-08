# List Comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [number ** 2 for number in numbers]

even_numbers = [number for number in numbers if number % 2 == 0]

print("Numbers:", numbers)
print("Squares:", squares)
print("Even Numbers:", even_numbers)
