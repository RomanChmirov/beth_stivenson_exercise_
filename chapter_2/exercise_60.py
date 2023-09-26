from math import floor

# Запрашиваем год у пользователя
year = int(input("Введите год: "))

# Вычисляем числовой эквивалент, соответствующий 1 января заданного года
day_of_the_week = (year + floor((year - 1) / 4) - floor((year - 1) / 100) + floor((year - 1) / 400)) % 7


# Вычисляем полное название дня недели
if day_of_the_week == 0:
    day = "воскресенье"

elif day_of_the_week == 1:
    day = "понедельник"

elif day_of_the_week == 2:
    day = "вторник"

elif day_of_the_week == 3:
    day = "среда"

elif day_of_the_week == 4:
    day = "четверг"

elif day_of_the_week == 5:
    day = "пятница"

elif day_of_the_week == 6:
    day = "суббота"


# Выводим результат
print(f'1 января {year} года — {day}.')
