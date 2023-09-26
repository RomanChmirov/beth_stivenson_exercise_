## Функция определяет, является ли строка целым числом
# @param s — исходная строка
# @return  True или False
def isInteger(s):
    # Убираем ведущие и замыкающие пробелы
    s = s.strip()

    # Проверяем является строка целым числом
    if ((s[0] == '+' or s[0] == '-') and s[1:].isdigit()) or s.isdigit():
        b = True
    else:
        b = False

    return b


def main():
    string = input("Введите строку: ")
    print("Строка является целым числом.") if isInteger(string) else print("Строка не является целым числом.")


if __name__ == "__main__":
    main()
