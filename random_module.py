# Python Random Module

import random

print("Random Number:", random.randint(1, 100))
print("Random Choice:", random.choice(["Python", "Java", "C++"]))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)

print("Shuffled List:", numbers)
