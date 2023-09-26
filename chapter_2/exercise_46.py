# Запрашиваем у пользователя название поля
name = input("Введите название поля: ")

# Проводим некоторые расчёты для дальнейшего вычисления цвета клетки
column = (name[0])
line = int(name[1])


if column == 'a' or column == 'c' or column == 'e' or column == 'g':
    s_ec = 1
else:
    s_ec = 0

if line == '1' or line == '3' or line == '5' or line == '7':
    s_ka = 1
else:
    s_ka = 0


# Вычисляем цвет клетки
if s_ec == s_ka:
    color = "чёрный"
else:
    color = "белый"


# Выводим результат
print(f"Цвет клетки — {color}.")
