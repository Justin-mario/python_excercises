def common_element_of_Array():
    list_of_input = ["11, 3, 14, 131, 17", "1, 2, 4, 13, 15"]
    first_element = list_of_input[0].split(", ")
    second_element = list_of_input[1].split(", ")
    new_element = ''

    for i in range(len(first_element)):
        for j in range(len(second_element)):
            if first_element[i] == second_element[j]:
                new_element += first_element[i] + ', '
    if len(new_element) == 0:
        print('False')
    print(new_element)


common_element_of_Array()


def common_element_of_Array_storing_in_collection():
    list_of_input = ["11, 3, 14, 131, 17", "1, 2, 4, 13, 15"]
    first_element = list_of_input[0].split(", ")
    second_element = list_of_input[1].split(", ")
    new_element = []

    for i in range(len(first_element)):
        for j in range(len(second_element)):
            if first_element[i] == second_element[j]:
                new_element.append(first_element[i])

    if len(new_element) == 0:
        print('False')
        exit()
    print(new_element)


common_element_of_Array_storing_in_collection()
