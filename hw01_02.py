user_time = int(input("Введите время в секундах >>>"))
hour = user_time // 360
minute = (user_time - (360 * hour)) // 60
second = (user_time - (360 * hour) - (60 * minute))
print(f"Время в формате чч:мм:сс >>> {hour:02}:{minute:02}:{second:02}")
