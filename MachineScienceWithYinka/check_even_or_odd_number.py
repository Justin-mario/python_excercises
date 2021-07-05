def even_odd_number():
    number = eval(input("enter number: "))
    if number % 2 == 0:
        print(number, "is an even number")
    else:
        print(number, "is an odd number")


even_odd_number()


def checking_for_vowel_in_a_word():
    list_of_vowels = ['a', 'e', 'i', 'o', 'u']
    user_input = input("Enter word: ")

    for i in list_of_vowels:
        if i in user_input:
            return "contains vowel"

    return"does not contain vowel"


print(checking_for_vowel_in_a_word())


def sorting_list_of_integers():
    list_of_numbers = [3, 2, 18, 0, 7, 6]
    list_of_numbers.sort()
    odd_number = []
    even_number = []
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] % 2 == 0:
            even_number.append(list_of_numbers[i])
        if list_of_numbers[i] % 2 == 1:
            odd_number.append(list_of_numbers[i])
    for i in odd_number:
        even_number.append(i)
    print(even_number)


sorting_list_of_integers()
