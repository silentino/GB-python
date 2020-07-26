plus = int(input("Введите значение выручки фирмы: "))
minus = int(input("Введите значение издержек фирмы: "))
if plus > minus:
    input("Фирма получает прибыль")
    rent = (plus - minus) / plus * 100
    input(f"Рентабельность выручки: {rent}")
    worker = int(input("Введите численность сотрудников: "))
    rent_for_worker = round((rent / worker), 2)
    input(f"Прибыль фирмы в расчете на одного сотрудника: {rent_for_worker}")
if plus < minus:
    input("Фирма работает в убыток")
else:
    input("Фирма работает в ноль")
