# Записываем частоты нот
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

# Запрашиваем ноту у пользователя
name = input("Введите ноту(например: D4): ")

# Определяем ноту и октаву
note = name[0]
octave = int(name[1])

# Добавляем переменную для хранения частоты ноты
note_frequency = ''


# Рассчитываем частоту ноты для 4 октавы
if note == 'C':
    note_frequency = C4

elif note == 'D':
    note_frequency = D4

elif note == 'E':
    note_frequency = E4

elif note == 'F':
    note_frequency = F4

elif note == 'G':
    note_frequency = G4

elif note == 'A':
    note_frequency = A4

elif note == 'B':
    note_frequency = B4

else:
    print("Вы ввели не ноту!")


# Адаптируем частоту ноты под любую октаву
note_frequency = note_frequency / 2 ** (4 - octave)

# Выводим результат
print(f"Частота ноты: {note_frequency}.")
