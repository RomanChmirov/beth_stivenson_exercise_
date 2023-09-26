# Импортируем необходимые функции
from random import randint
from time import sleep

# Задаём номер выемке, в которую якобы упал шарик
number = randint(0, 37)


if number == 37:

    number = '00'


# Выводим приветствие на экран
print("Играем в рулетку.")
sleep(0.7)
print("Рулетка крутится...")
sleep(3.3)
print(f"Выпавший номер: {number}.")
sleep(1.5)

# Выводим сыгравшие ставки
print(f"Выигравшая ставка: {number}.")


if number != '00' and number > 0:

    if ((number % 2 == 1) and ((0 < number < 10) or (20 < number < 28))) or \
            ((number % 2 == 0) and ((10 < number < 20) or (28 < number <= 36))):
        print("Выигравшая ставка: красное.")

    else:
        print("Выигравшая ставка: чёрное.")

    if number % 2 == 1:
        print("Выигравшая ставка: нечётное.")

    else:
        print("Выигравшая ставка: чётное.")

    if 1 <= number <= 18:
        print("Выигравшая ставка: от 1 до 18.")

    elif 19 <= number <= 36:
        print("Выигравшая ставка: от 19 до 36.")
