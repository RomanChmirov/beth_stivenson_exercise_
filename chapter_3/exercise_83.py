from random import randint

# Задаём нулевое значение счётчику смен "лидера"
x = 0

# Генерируем первое число
a = randint(1, 100)
# и задаём переменную для максимального значения
MAX = a

# Выводим первое число
print(a, "<---Первое число")


# Выводим остальные числа
for i in range(1, 100):
    # Генерируем следующие числа
    b = randint(1, 100)

    # Проверяем следующее число на "максимальность" и выводим результат
    if MAX < b:
        MAX = b
        x += 1
        print(b, "<---Обновление")
    else:
        print(b)


# Выводим конечные результаты
print(f"Максимальное число в ряду: {MAX}.")
print(f"Кол-во смен лидера: {x}.")
