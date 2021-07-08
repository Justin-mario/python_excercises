class SortingArraysAndFindFirstAndLastIndex:

    @staticmethod
    def sorting_array(numbers):
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if numbers[i] < numbers[j]:
                    temp = numbers[i]
                    numbers[i] = numbers[j]
                    numbers[j] = temp
        print(numbers)
        return numbers


    @staticmethod
    def finding_first_and_last_index_of_array(list_numbers, value_to_find_the_index):
        first_index = -1
        second_index = -1
        indices = [first_index, second_index]
        for i in range(len(list_numbers)):
            if list_numbers[i] == value_to_find_the_index and first_index == -1:
                first_index = i
                indices[0] = first_index

            if list_numbers[i] == value_to_find_the_index and first_index != -1:
                second_index = i
                if first_index != second_index:
                    indices[1] = second_index
        print(indices)


number = [0, 8, -2, 5, 0, 0, 0, 8]
value_to_find_index = 0
sorting_arrays = SortingArraysAndFindFirstAndLastIndex()
sorted_array = sorting_arrays.sorting_array(number)
sorting_arrays.finding_first_and_last_index_of_array(sorted_array, value_to_find_index)
