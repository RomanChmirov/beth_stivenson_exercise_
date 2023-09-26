# Записываем частоты нот
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88
# и предел погрешности
limit = 1

# Запрашиваем частоту ноты у пользователя
note_frequency = float(input("Введите частоту ноты(Гц): "))

# Задаём переменную для хранения ноты
note = ''


# Ищем ноту по частоте
if (C4 - limit) <= note_frequency <= (C4 + limit):
    note = 'C4'

elif (D4 - limit) <= note_frequency <= (D4 + limit):
    note = 'D4'

elif (E4 - limit) <= note_frequency <= (E4 + limit):
    note = 'E4'

elif (F4 - limit) <= note_frequency <= (F4 + limit):
    note = 'F4'

elif (G4 - limit) <= note_frequency <= (G4 + limit):
    note = 'G4'

elif (A4 - limit) <= note_frequency <= (A4 + limit):
    note = 'A4'

elif (B4 - limit) <= note_frequency <= (B4 + limit):
    note = 'B4'


# Выводим результат
if note == '':
    print("Ноты, которой бы соответствовала данная частота, не существует.")

else:
    print(f"Эта частота соответствует ноте {note}.")
