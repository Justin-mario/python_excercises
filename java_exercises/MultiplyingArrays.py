def multiply_array_elements(list_of_number):
    new_list_of_numbers = []
    product = 1
    for i in range(len(list_of_number)):
        product *= list_of_number[i]
    for j in range(len(list_of_number)):
        new_list_of_numbers.append(product//list_of_number[j])
    #     for j in range(len(list_of_number)):
    #         if i == j:
    #             continue
    #         product *= list_of_number[j]
    #
    #     new_list_of_numbers.append(product)
    #
    return new_list_of_numbers



list_of_numbers = [4, 5, 10, 2]
print(multiply_array_elements(list_of_numbers))
