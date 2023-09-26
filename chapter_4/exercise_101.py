from random import randint


## Функция генерирует случайный номерной знак(старого или нового формата)
# @return номерной знак
def license_plate():
    result = ''
    plate_format = randint(1, 2)

    # Генерируем знак старого формата
    if plate_format == 1:

        while len(result) < 3:
            result += chr(randint(65, 90))
        while len(result) < 6:
            result += chr(randint(48, 57))

    # Генерируем знак нового формата
    if plate_format == 2:

        while len(result) < 4:
            result += chr(randint(48, 57))
        while len(result) < 7:
            result += chr(randint(65, 90))

    return result


def main():
    plate = license_plate()
    print(plate)


main()
