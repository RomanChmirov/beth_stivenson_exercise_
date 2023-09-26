## Функция убирает знаки препинания из строки
# @param s — строка
# @return список из слов из строки без знаков препинания
def only_words(s):
    data = list(s)
    pos = 0
    result = ''

    # Заменяем знаки препинания в списке на пустые строки
    while pos < len(data):

        if data[pos] == '.' or data[pos] == ',' or data[pos] == '!' or data[pos] == '?' or \
                data[pos] == '-' or data[pos] == ':' or data[pos] == ';':
            data[pos] = ''
        elif data[pos] == "'":
            if pos == 0 or pos == len(data) - 1:
                data[pos] = ''
            elif data[pos - 1] == ' ' or data[pos + 1] == ' ':
                data[pos] = ''

        pos += 1

    # Убираем пробелы из списка
    for i in data:
        result += i
    result = result.split(' ')
    while '' in result:
        result.remove('')

    return result


def main():
    string = input("Введите строку: ")
    print(*only_words(string))


if __name__ == "__main__":
    main()
