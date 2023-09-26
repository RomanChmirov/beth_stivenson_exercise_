# Минимальные частоты в разных категориях волн
Micro_MIN = 3 * (10 ** 9)
Infrared_MIN = 3 * (10 ** 12)
Visible_MIN = 4.3 * (10 ** 14)
Ultraviolet_MIN = 7.5 * (10 ** 14)
Xrays_MIN = 3 * (10 ** 17)
Gamma_MIN = 3 * (10 ** 19)

# Запрашиваем у пользователя значение частоты волны
print("Введите частоту волны.")
coefficient = float(input("Введите коэффициент перед 10: "))
tens_exponent = float(input("Введите показатель степени 10: "))

# Создаём переменную для помещения конечного результата пользовательского ввода
wave_frequency = coefficient * 10 ** tens_exponent


if wave_frequency < Micro_MIN:
    name = "радиоволновое"

elif Micro_MIN <= wave_frequency < Infrared_MIN:
    name = "микроволновое излучение"

elif Infrared_MIN <= wave_frequency < Visible_MIN:
    name = "инфракрасное излучение"

elif Visible_MIN <= wave_frequency < Ultraviolet_MIN:
    name = "видимое излучение"

elif Ultraviolet_MIN <= wave_frequency < Xrays_MIN:
    name = "ультрафиолетовое излучение"

elif Xrays_MIN <= wave_frequency < Gamma_MIN:
    name = "рентгеновское излучение"

elif Gamma_MIN <= wave_frequency:
    name = "гамма-излучение"


# Выводим результат
print(f"Данной частоте соответствует {name}.")
