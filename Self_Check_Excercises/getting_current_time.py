import time

current_time = time.time()
total_second = int(current_time)
current_seconds = total_second % 60
total_minutes = total_second // 60
current_minutes = total_minutes % 60
total_hour = total_minutes // 60
current_hour = total_hour % 24
current_hour = current_hour - 11
print(current_hour, current_minutes, current_seconds, sep=":")
