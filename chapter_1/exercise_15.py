# Кол-во дюймов, ярдов, миль в футе
INCHES_IN_FEETS = 0.0833333
YARDS_IN_FEETS = 0.333333
MILES_IN_FEETS = 0.000189394

# Запрашиваем у пользователя расстояние в футах
a = float(input("Введите расстояние в футах: "))

# Выводим результат в дюймах, ярдах и милях соответственно
print(f"Расстояние в дюймах: {a * INCHES_IN_FEETS};")
print(f"Расстояние в ярдах: {a * YARDS_IN_FEETS};")
print(f"Расстояние в милях: {a * MILES_IN_FEETS}.")
