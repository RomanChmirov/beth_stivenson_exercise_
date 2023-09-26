# Запрашиваем у пользователя буквенную оценку
letter_score = input("Введите буквенную оценку: ")

# Задаём нулевое значение счётчику числа оценок и сумме оценок
i = 0
estimates = 0


while letter_score:
    #  С каждым входом в цикл увеличиваем счётчик на 1
    i += 1

    # Вычисляем коэффициенты a и b
    len_line = len(letter_score)
    
    if len_line == 2:
        a = letter_score[0]
        b = letter_score[1]

    elif len_line == 1:
        a = letter_score[0]
        b = ''

    # Вычисляем числовую оценку
    if a == 'A':

        if b == '+' or b == '':
            numerical_score = '4.0'
        elif b == '-':
            numerical_score = '3.7'

    if a == 'B':

        if b == '+':
            numerical_score = '3.3'
        elif b == '':
            numerical_score = '3.0'
        elif b == '-':
            numerical_score = '2.7'

    if a == 'C':

        if b == '+':
            numerical_score = '2.3'
        elif b == '':
            numerical_score = '2.0'
        elif b == '-':
            numerical_score = '1.7'

    if a == 'D':

        if b == '+':
            numerical_score = '1.3'
        elif b == '':
            numerical_score = '1.0'

    if a == '0' or a == 'F':
        numerical_score = '0'

    # Считаем сумму всех оценок
    estimates += float(numerical_score)
    # а также их кол-во
    quantity = i

    # Запрашиваем у пользователя следующую буквенную оценку
    letter_score = input("Введите следующую буквенную оценку(для окончания ввода нажмите Enter: ")


# Считаем среднюю оценку
average_score = estimates / i

# Выводим результат
print(f"Средняя оценка в числовом формате: {average_score}.")
