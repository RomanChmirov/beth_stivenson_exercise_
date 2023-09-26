# Запрашиваем у пользователя буквенную оценку
numerical_score = float(input("Введите числовую оценку(цифрами): "))


# Вычисляем буквенную оценку
if numerical_score >= 0:

    if 4 <= numerical_score:
        letter_score = 'A+'

    elif 3.85 <= numerical_score < 4:
        letter_score = 'A'

    elif 3.5 <= numerical_score < 3.85:
        letter_score = 'A-'

    elif 3.15 <= numerical_score < 3.5:
        letter_score = 'B+'

    elif 2.85 <= numerical_score < 3.15:
        letter_score = 'B'

    elif 2.5 <= numerical_score < 2.85:
        letter_score = 'B-'

    elif 2.15 <= numerical_score < 2.5:
        letter_score = 'C+'

    elif 1.85 <= numerical_score < 2.15:
        letter_score = 'C'

    elif 1.5 <= numerical_score < 1.85:
        letter_score = 'C-'

    elif 1.15 <= numerical_score < 1.5:
        letter_score = 'D+'

    elif 0.5 <= numerical_score < 1.15:
        letter_score = 'D'

    elif 0 <= numerical_score < 0.5:
        letter_score = 'F'

else:
    letter_score = "не существует"


# Выводим результат
print(f"Буквенная оценка, соответствующая вашей числовой — {letter_score}.")
