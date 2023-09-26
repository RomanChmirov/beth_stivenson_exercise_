# Запрашиваем у пользователя длину волны
wavelength = float(input("Введите длину волны в нанометрах(нм): "))


# Вычисляем цвет спектра
if 380 <= wavelength < 450:
    color = "фиолетовый"

elif 450 <= wavelength < 495:
    color = "синий"

elif 495 <= wavelength < 570:
    color = "зелёный"

elif 570 <= wavelength < 590:
    color = "жёлтый"

elif 590 <= wavelength < 620:
    color = "оранжевый"

elif 620 <= wavelength <= 750:
    color = "красный"

else:
    color = ''


# Выводим результат
if color == '':
    print("Волны с данной длиной не существует.")

else:
    print(f"Цвет, соответствующий введённой длине волны — {color}.")
