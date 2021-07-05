def arithmetic_progression(first_number, second_number, third_number):

    third_and_second_number_difference = third_number - second_number
    second_and_first_number_difference = second_number - first_number

    if third_and_second_number_difference == second_and_first_number_difference:
        fourth_number = third_number + third_and_second_number_difference
        print("The sequence is ", first_number, " ", second_number, " ", third_number, " ", fourth_number)
    else:
        print("Not an arithmetic progression")


arithmetic_progression(1, 3, 5)


def geometric_progression(first_number, second_number, third_number):
    third_and_second_number_ratio = third_number / second_number
    second_and_first_number_ratio = second_number / first_number
    ratio = third_and_second_number_ratio

    if third_and_second_number_ratio == second_and_first_number_ratio:
        fourth_number = first_number * int((ratio ** 3))
        print("The sequence is ", first_number, " ", second_number, " ", third_number, " ", fourth_number)
    else:
        print("Not a Geometric progression")


geometric_progression(6, 36, 216)
