def user_detail():
    user_name = str(input("input user name: "))
    user_age = int(input("Input user age: "))
    return user_name, user_age


def store_username_and_age():
    name, age = user_detail()
    user_data.update({name: age})


user_data = {}


for _ in range(3):
    store_username_and_age()
print(user_data)
