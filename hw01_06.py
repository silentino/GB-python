a = int(input("Введите результат в первый день : "))
b = int(input("Введите желаемый результат : "))
day = 1
input(f"{day}-й день: {round(a,2)}")
while a < b:
    a = a + (a * 0.1)
    day += 1
    input(f"{day}-й день: {round(a,2)}")
input(f"На {day}-й день спортсмен достиг результата - не менее {b} км")
