# Запрашиваем у пользователя число
x = float(input("Введите число: "))

guess = x / 2


# Вычисляем квадратный корень
while guess * guess - x > 10 ** -12:
    guess = (guess + x / guess) / 2


# Выводим результат
print(guess)
