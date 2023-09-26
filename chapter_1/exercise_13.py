# Цены разных монет в центах
TOONIE = 200
LOONIE = 100
QUARTER = 25
DIME = 10
NICKEL = 5


# Запрашиваем кол-во центов долга у пользователя
change = int(input("Сколько центов я вам должен? "))


# Считаем кол-во 2-х долларовых монет
print(f"Кол-во 2-х долларовых монет: {change // TOONIE};")

# Считаем кол-во 1-х долларовых монет
change = change % TOONIE
print(f"Кол-во долларовых монет: {change // LOONIE};")

# Считаем кол-во монет по 25 центов
change = change % LOONIE
print(f"Кол-во монет(25 центов): {change // QUARTER};")

# Считаем кол-во монет по 10 центов
change = change % QUARTER
print(f"Кол-во монет(10 центов): {change // DIME};")

# Считаем кол-во монет по 5 центов
change = change % DIME
print(f"Кол-во монет(5 центов): {change // NICKEL};")

# Считаем кол-во монет по 1 центу
change = change % NICKEL
print(f"Кол-во монет(1 цент): {change}.")
