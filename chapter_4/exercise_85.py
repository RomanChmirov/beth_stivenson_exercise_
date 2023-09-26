from math import sqrt

# Запрашиваем данные у пользователя
first_leg = float(input("Введите длину первого катета: "))
second_leg = float(input("Введите длину второго катета: "))


## Функция вычисляет длину гипотенузы
# @param a — длина первого катета
# @param b — длина второго катета
# @return гипотенуза
def calculate_the_hypotenuse(a, b):
    return sqrt(a ** 2 + b ** 2)


# Находим гипотенузу
hypotenuse = calculate_the_hypotenuse(first_leg, second_leg)

# Выводим результат
print(f"Длина гипотенузы: {hypotenuse}.")
