## Озаглавливаем нужные буквы в строке
# @param s – исходная строка для обработки
# @return новая строка
def capitalize(s):
    new_s = s


    ### Озаглавливаем первый непробельный символ
    pos = 0

    # Ищем позицию первого непробельного символа
    while pos < len(s) and new_s[pos] == ' ':
        pos += 1

    if pos < len(s):
        # Записываем в переменную result новую строку с озаглавленным первым непробельным символом
        new_s = new_s[0: pos] + new_s[pos].upper() + new_s[pos + 1: len(new_s)]


    ### Озаглавливаем символ, идущий после точки, восклицательного и вопросительного знаков
    pos = 0
    while pos < len(s):

        # Переходим на символ точки, восклицательного и вопросительного знаков
        if new_s[pos] == '.' or new_s[pos] == '!' or new_s[pos] == '?':
            pos += 1

            # Пропускаем пробелы
            while pos < len(s) and new_s[pos] == ' ':
                pos += 1

            # Если не достигли конца строки, меняем текущий символ на заглавную букву
            if pos < len(s):
                new_s = new_s[0: pos] + new_s[pos].upper() + new_s[pos + 1: len(new_s)]

        pos += 1


    ### Озаглавливаем букву 'i', если перед ней стоит пробел,
    ### а после пробел, точка, восклицательный или вопросительный знак, апостроф или запятая
    pos = 1
    while pos < len(s) - 1:

        if (new_s[pos] == 'i' and new_s[pos - 1] == ' ') and \
                (new_s[pos + 1] == ' ' or new_s[pos + 1] == '.' or new_s[pos + 1] == '!' or
                 new_s[pos + 1] == '?' or new_s[pos + 1] == "'" or new_s[pos + 1] == ','):
            new_s = new_s[0: pos] + new_s[pos].upper() + new_s[pos + 1: len(new_s)]

        pos += 1


    return new_s


def main():
    string = input("Введите строку: ")
    new_string = capitalize(string)
    print(f"Исправленная версия: {new_string}.")


main()
