# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []
count_elem = int(input("Введите количество элементов списка >>> "))
i = 0
el = 0
while i < count_elem:
    i += 1
    my_list.append(input(f"Введите значение {i}-элемента списка >>> "))
print(f"Сформированный список: {my_list}")
for elem in range(int(len(my_list)/2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(f"Новый список: {my_list}")
