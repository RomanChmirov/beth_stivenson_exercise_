# Запрашиваем у пользователя магнитуду землетрясения
magnitude = float(input("Введите магнитуду землетрясения(цифрами): "))

#  Создаём переменную для уровня землетрясения
level = ''


# Вычисляем уровень землетрясения
if 0 < magnitude < 2:
    level = "минимальное"

elif 2 <= magnitude < 3:
    level = "очень слабое"

elif 3 <= magnitude < 4:
    level = "слабое"

elif 4 <= magnitude < 5:
    level = "промежуточное"

elif 5 <= magnitude < 6:
    level = "умеренное"

elif 6 <= magnitude < 7:
    level = "сильное"

elif 7 <= magnitude < 8:
    level = "очень сильное"

elif 8 <= magnitude < 10:
    level = "огромное"

elif magnitude >= 10:
    level = "разрушительное"


# Выводим результат
print(f"Землетрясение — {level}.")
