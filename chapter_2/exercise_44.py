# Имена людей в соответствие банкнотам
d1 = "Джордж Вашингтон"
d2 = "Томас Джефферсон"
d5 = "Авраам Линкольн"
d10 = "Александр Гамильтон"
d20 = "Эндрю Джексон"
d50 = "Улисс Грант"
d100 = "Бенджамин Франклин"

# Запрашиваем значение банкноты у пользователя
banknote_denomination = int(input("Введите значение банкноты($): "))

# Создаём переменную для имени человека
name = ''


# Узнаём человека по номиналу банкноты
if banknote_denomination == 1:
    name = d1

elif banknote_denomination == 2:
    name = d2

elif banknote_denomination == 5:
    name = d5

elif banknote_denomination == 10:
    name = d10

elif banknote_denomination == 20:
    name = d20

elif banknote_denomination == 50:
    name = d50

elif banknote_denomination == 100:
    name = d100


# Выводим результат
if name == '':
    print("Банкноты с таким номиналом не существует на данный момент!!!")

else:
    print(f"На банкноте изображён {name}.")
