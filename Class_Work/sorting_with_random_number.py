import random
numbers = [2, 4, 6, 9, 8]
i = 0

while i < len(numbers):
    temp = numbers[i]
    shuffle = random.randint(0, len(numbers))
    numbers[i] = numbers[shuffle-1]
    numbers[shuffle - 1] = temp
    i += 1
print(numbers)
