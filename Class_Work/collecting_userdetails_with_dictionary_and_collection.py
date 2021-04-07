# colling user name and age
collection = []
user_age = []
user = 0

while user < 3:
    user_name = str(input("Enter user name: "))
    user_age = str(input("Enter user age: "))
    user1 = {'name': user_name, 'age': user_age}
    collection.append(user1)
    user += 1
for i in collection:
    print(i)
