def adding_two_list():
    list1 = [13, 15, 19]
    list2 = [11, 13, 18]
    list3 = list1 + list2

    # list3 = []
    # for i in range(len(list1)):
    #     list3.append(list1[i])
    #     list3.append(list2[i])
    # print(list3)

    for i in range(len(list3)):
        for j in range(len(list3)):
            temp_i = list3[i]
            temp_j = list3[j]
            if temp_i < temp_j:
                list3[i] = temp_j
                list3[j] = temp_i
    print(list3)


adding_two_list()
