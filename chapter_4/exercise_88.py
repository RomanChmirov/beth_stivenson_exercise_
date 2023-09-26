# Запрашиваем данные у пользователя
print("Введите 3 числа.")
first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))
third_number = float(input("Введите третье число: "))


## Функция вычисляет максимальное число
# @param a — первое число
# @param b — второе число
# @param c — третье число
# @return максимальное число
def calculate_max(a, b, c):

    if b < a:
        if c < a:
            max_v = a
        else:
            max_v = c

    else:
        if c < b:
            max_v = b
        else:
            max_v = c

    return max_v


## Функция вычисляет минимальное число
# @param a — первое число
# @param b — второе число
# @param c — третье число
# @return минимальное число
def calculate_min(a, b, c):

    if b < a:
        if b < c:
            min_v = b
        else:
            min_v = c

    else:
        if a < c:
            min_v = a
        else:
            min_v = c

    return min_v


# Находим минимальное и максимальное значение
min_value = calculate_min(first_number, second_number, third_number)
max_value = calculate_max(first_number, second_number, third_number)


## Функция вычисляет медиану 3 значений
# @param a — первое число
# @param b — второе число
# @param c — третье число
# @return медиана 3 значений
def calculate_the_median(a, b, c):
    return a + b + c - min_value - max_value


# Находим медиану 3 значений
median = calculate_the_median(first_number, second_number, third_number)

# Выводим результат
print(f"Медиана 3 значений равна {median}.")
