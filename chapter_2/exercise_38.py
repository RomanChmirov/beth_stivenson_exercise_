# Запрашиваем у пользователя кол-во сторон треугольника
side_quantity = int(input("Введите кол-во(3—10) сторон фигуры, название которой вы хотите узнать: "))


# Вычисляем название фигуры и выводим результат
if side_quantity < 3 or side_quantity > 10:
    print("Вы ввели кол-во сторон выходящее за диапазон программы.")

elif side_quantity == 3:
    print("Это треугольник.")

elif side_quantity == 4:
    print("Это прямоугольник.")

elif side_quantity == 5:
    print("Это пентагон(пятиугольник).")

elif side_quantity == 6:
    print("Это гексагон(шестиугольник).")

elif side_quantity == 7:
    print("Это гептагон(семиугольник).")

elif side_quantity == 8:
    print("Это октагон(восьмиугольник).")

elif side_quantity == 9:
    print("Это девятиугольник.")

elif side_quantity == 10:
    print("Это десятиугольник.")
