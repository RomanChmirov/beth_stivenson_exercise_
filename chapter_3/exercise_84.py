from random import randint

# счётчику подбрасываний
x = 0
# и общему числу подбрасываний
all_tries = 0


# Осуществляем 10 попыток. В одном цикле будет 1 попытка
for j in range(0, 10):
    # Задаём переменной result значение пустой строки
    result = ''
    # Задаём нулевое значение счётчику попыток
    g = 0


    # Осуществляем 3 первых подбрасывания. В одном цикле 1 подбрасывание
    for i in range(0, 3):
        o_or_r = randint(0, 1)

        coin_value = 'O' if o_or_r == 0 else 'P'

        result += coin_value

        g += 1

    # Осуществляем остальные подбрасывания. В одном цикле 1 подбрасывание
    while result[-1] != result[-2] or result[-1] != result[-3] or result[-2] != result[-3]:
        o_or_r = randint(0, 1)

        coin_value = 'O' if o_or_r == 0 else 'P'

        result += coin_value

        g += 1

    # Выводим кол-во подбрасываний
    print(result, f"(кол-во подбрасываний: {g})", )

    # Считаем общее кол-во попыток
    all_tries += g
    # и подбрасываний
    x += 1


# Вычисляем среднее количество подбрасываний
average_number_of_tries = all_tries / x

# Выводим результат
print(f"Среднее количество подбрасываний: {average_number_of_tries}.")
