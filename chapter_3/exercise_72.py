# Генерируем числа от 1 до 100
for i in range(1, 101, 1):

    # Выводим слово или число согласно правилам игры
    if i % 3 == i % 5 == 0:
        print(i, "Fizz-Buzz")
        continue

    elif i % 5 == 0:
        print(i, "Buzz")

    if i % 3 == 0:
        print(i, "Fizz")

    else:
        print(i)
