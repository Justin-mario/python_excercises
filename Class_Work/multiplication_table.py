# multiplication table
def multiplication_table():
    print("                         MULTIPLICATION TABLE\n")

    for row in range(1, 10):
        print("\t ", row, end=" ")

    print("\n________________________________________________________________________")

    for column in range(1, 10):
        print(column, " | ", end=' ',)
        for rows in range(1, 10):
            print(" ", rows * column, "\t", end='')
        print(" ")


multiplication_table()