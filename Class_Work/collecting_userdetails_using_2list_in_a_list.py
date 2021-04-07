# using two  list to collect userdetails

user_details = []

user = 0
while user < 3:
    name = str(input("Enter user name: "))
    user_name = [name]
    user_details.append(user_name)
    age = int(input("Enter Age: "))
    user_age = [age]
    user_details.append(user_age)
    user += 1

for i in user_details:
    print(i,)
