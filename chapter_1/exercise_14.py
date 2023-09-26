# Кол-во сантиметров в футе и дюйме соответственно
CENTIMETERS_IN_FOOTS = 12
CENTIMETERS_IN_INCH = 2.54

# Запрашиваем у пользователя рост в футах и дюймах соответственно у пользователя
height_f = int(input("Сколько в вашем росте футов? "))
height_d = int(input("Сколько в вашем росте дюймов? "))

# Считаем рост в сантиметрах
rost = (height_f * CENTIMETERS_IN_FOOTS + height_d) * CENTIMETERS_IN_INCH

# Выводим результат
print(f"Ваш рост(сантиметры): {rost}.")
