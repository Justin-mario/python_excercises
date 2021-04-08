# using sentinel control loop to input and calculate the average of grade

counter = 0
total = 0

grade = int(input("input grade or -1 to end:  "))

while grade != -1:
    total += grade
    counter += 1
    grade = int(input("input grade or -1 to end:  "))

if total != 0:
    average = total/counter
    print(f"Average is:  {average:.4f}")
else:
    print("no grade was entered")
