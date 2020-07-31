# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

user_number = int(input("Введите месяц в виде целого числа от 1 до 12 >>> "))

# решение через list
print("Решение через list")
month = [1, 2, 12, 3, 4, 5, 6, 7, 8, 9, 10, 11]
season = ["зима", "весна", "лето", "осень"]
if user_number == month[0] or user_number == month[1] or user_number == month[2]:
    print(f"Этот месяц относится к времени года {season[0]}")
elif user_number == month[3] or user_number == month[4] or user_number == month[5]:
    print(f"Этот месяц относится к времени года {season[1]}")
elif user_number == month[6] or user_number == month[7] or user_number == month[8]:
    print(f"Этот месяц относится к времени года {season[2]}")
elif user_number == month[9] or user_number == month[10] or user_number == month[11]:
    print(f"Этот месяц относится к времени года {season[3]}")
else:
    print("Некорректный ввод месяца")


# решение через dict
print("Решение через dict")
seasons_dict = {"ЗИМА": (1, 2, 12),
           "ВЕСНА": (3, 4, 5),
           "ЛЕТО": (6, 7, 8),
           "ОСЕНЬ": (9, 10, 11)
            }
for key in seasons_dict.keys():
    if user_number in seasons_dict[key]:
        print(f"Этот месяц относится к времени года {key}")
