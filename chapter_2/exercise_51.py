# Импортируем необходимые модули
from math import sqrt

# Запрашиваем переменные у пользователя
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# Задаём переменные для корней квадратичной функции
x1 = float()
x2 = float()
x = float()

# Считаем дискриминант
discriminant = (b ** 2) - (4 * a * c)


if discriminant >= 0:

    if discriminant == 0:
        x = -b / (2 * a)

        print(f"Квадратичная функция имеет один корень:  х = {x}.")

    else:
        x1 = (-b - sqrt(discriminant)) / (2 * a)
        x2 = (-b + sqrt(discriminant)) / (2 * a)

        print(f"Квадратичная функция имеет два корня:  х1 = {x1}; х2 = {x2}.")

else:
    print("Квадратичная функция не имеет корней.")
