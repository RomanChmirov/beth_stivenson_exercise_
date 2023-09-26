# Запрашиваем у пользователя буквенную оценку
letter_score = input("Введите буквенную оценку: ")

numerical_score = ''

len_line = len(letter_score)


if len_line == 2:
    a = letter_score[0]
    b = letter_score[1]

elif len_line == 1:
    a = letter_score[0]
    b = ''

else:
    numerical_score = 'не существует'


# Вычисляем числовую оценку
if (len_line == 2 or len_line == 1) and ((a != '' and b != '') or (a != '' and b == '')):


    if a == 'A':

        if b == '+' or b == '':
            numerical_score = '4,0'
        elif b == '-':
            numerical_score = '3,7'

    if a == 'B':

        if b == '+':
            numerical_score = '3,3'
        elif b == '':
            numerical_score = '3,0'
        elif b == '-':
            numerical_score = '2,7'

    if a == 'C':

        if b == '+':
            numerical_score = '2,3'
        elif b == '':
            numerical_score = '2,0'
        elif b == '-':
            numerical_score = '1,7'

    if a == 'D':

        if b == '+':
            numerical_score = '1,3'
        elif b == '':
            numerical_score = '1,0'

    if a == 'F':

        if b == '':
            numerical_score = '0'


# Выводим результат
print("Такой оценки не существует.") if numerical_score == '' else \
    print(f"Числовая оценка, соответствующая вашей буквенной — {numerical_score}.")
