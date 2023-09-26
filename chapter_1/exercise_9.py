# Проценты, которые будут начисляться за один год хранения денег в банке
PERCENT_FOR_ONE_YEAR = 1 + 0.04

# Запрашиваем сумму взноса у пользователя
deposit = float(input("Введите сумму взноса: "))

# Считаем сумму в конце первого, второго и третьего годов
year_1 = deposit * PERCENT_FOR_ONE_YEAR
year_2 = year_1 * PERCENT_FOR_ONE_YEAR
year_3 = year_2 * PERCENT_FOR_ONE_YEAR

# Выводим результат
print(f"Сумма в конце 1 года: %.2f;\n"
      f"Сумма в конце 2 года: %.2f;\n"
      f"Сумма в конце 3 года: %.2f." % (year_1, year_2, year_3))
