numeral = int(input("Введите целое положительное число: "))
number = numeral % 10
numeral = numeral // 10
while numeral > 0:
    if numeral % 10 > number:
        number = numeral % 10
    numeral = numeral // 10
print(f"Самая большая цифра в числе >>> {number}")
