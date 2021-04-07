# Heart Rate Calculator

age = int(input("Input age: "))
maximum_heart_rate: int = 220 - age
print("Your age is: ", age, "And Maximum Heart Rate is: ", maximum_heart_rate)
print("Your Target Heart Rate is: ", maximum_heart_rate * 0.5, "%", " - ", maximum_heart_rate * 0.85, "%",
      "of maximum heart rate")
