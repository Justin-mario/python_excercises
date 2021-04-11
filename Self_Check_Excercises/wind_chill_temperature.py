
temperature = eval(input("Input Temperature Between -58F and 41f: "))
velocity_of_wind = eval(input("Input velocity: "))
wind_chill_temperature = 35.74 + (0.6215 * temperature) - 35.75 * (velocity_of_wind ** 0.16) \
                         + 0.4275 * temperature * (velocity_of_wind ** 0.16)
print(f'{wind_chill_temperature}')
