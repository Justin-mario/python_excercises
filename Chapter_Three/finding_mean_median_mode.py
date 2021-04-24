# program to find mean median mode
import statistics
set_of_Number = (9, 11, 22, 34, 17, 22, 34, 22, 40, 34)
mode = statistics.mode(set_of_Number)
print(mode)
print(statistics.median(set_of_Number))
print(f'{statistics.mean(set_of_Number):.2f}')