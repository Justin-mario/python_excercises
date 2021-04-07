# collecting userdetails using a dictionaries in a list

user_data = []
input_collector = 0

while input_collector < 3:
    user_name = str(input("input user name: "))
    user_age = int(input("Input user age: "))
    user_bio = {user_name: user_age}
    user_data.append(user_bio)
    input_collector += 1

for dictionary_iterator in user_data:
    print(dictionary_iterator)
