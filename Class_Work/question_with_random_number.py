import random

number1 = random.randint(1, 100)
number2 = random.randint(1, 100)
number3 = random.randint(1, 100)
answer = number1 + number2 + number3
student_answer = 0

while student_answer != answer:
    student_answer = int(input("what is " + str(number1) + "  +  " + str(number2) + "  +  " + str(number3) + " "))
    if student_answer == answer:
        print("correct", answer)
    else:
        print("incorrect", answer)
