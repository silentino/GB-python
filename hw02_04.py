# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

my_list = []
user_string = str(input("Введите строку из нескольких слов, разделенных пробелами >>> "))

for el in range(user_string.count(' ') + 1):
    my_list = user_string.split()

for ind, el in enumerate(my_list):
    print(ind, el[0:10])
