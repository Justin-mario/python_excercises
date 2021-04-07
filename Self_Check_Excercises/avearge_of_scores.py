# finding average of scores for a group of 10 students

"""average = 0
for grade in [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]:
    average += grade/10
print("Average is: ", average)"""

grade1_int = 1
total_int = 0
average1_float = 0
while grade1_int <= 10:
    number = int(input("Input grade: "))
    total_int += number
    average1_float = total_int / grade1_int
    grade1_int += 1
print("Total Score is: ", total_int, "\n", "Average is: ", average1_float)
