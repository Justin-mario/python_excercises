# collecting using details using a single list

user_details = []
user = 0

while user < 3:
    name = str(input("enter name: "))
    user_details.append(name)
    age = str(input("enter age: "))
    user_details.append(age)
    user += 1

for user_list in user_details:
    print(user_list)
