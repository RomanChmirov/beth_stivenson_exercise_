# Запрашиваем у пользователя номерной знак машины
number = input("Введите номерной знак машины: ")


# Определяем образец номерного знака
if len(number) == 6 and \
        ('A' <= number[0] <= 'Z') and \
        ('A' <= number[1] <= 'Z') and \
        ('A' <= number[2] <= 'Z') and \
        ('0' <= number[3] <= '9') and \
        ('0' <= number[4] <= '9') and \
        ('0' <= number[5] <= '9'):
    license_plate_sample = "старый"

elif len(number) == 7 and \
        ('0' <= number[0] <= '9') and \
        ('0' <= number[1] <= '9') and \
        ('0' <= number[2] <= '9') and \
        ('0' <= number[3] <= '9') and \
        ('A' <= number[4] <= 'Z') and \
        ('A' <= number[5] <= 'Z') and \
        ('A' <= number[6] <= 'Z'):
    license_plate_sample = "новый"


# Выводим результат
print(f"Образец номерного знака — {license_plate_sample}.")
