# using for to iterate through list

total = 0
for number in [2, 4, 8, 12, 14]:
    total = total + number
print("total sum of numbers in list is: ", total)

for count in range(10):
    print(count, end=', ')

total1 = 0
for counter in range(1000001):
    total1 += counter
print("\n", "Total sum of numbers in 1,000,000 is: ", total1)
