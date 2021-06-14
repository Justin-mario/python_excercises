import random
import time

count = 0
student_answer = -1
correct_count = 0
incorrect_count = 0
start_time = time.time()
while count < 5:
    number1 = random.randint(1, 20)
    number2 = random.randint(1, 20)
    answer = number1 + number2

    student_answer = eval(input("what is " + str(number1) + " + " + str(number2) + " "))

    if student_answer == answer:
        print("Correct")
        correct_count += 1
    else:
        print("Incorrect")
        incorrect_count += 1

    count += 1
end_time = time.time()
test_time = (end_time - start_time)
print("Time you spent writing the test was:  ", format(test_time, "5.2f"), "seconds")
print("Your got ", correct_count, "questions correct")
print("your failed ", incorrect_count, "question")
