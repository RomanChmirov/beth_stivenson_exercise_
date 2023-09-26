from exercise_117 import only_words

string = input("Введите строку: ")

string = string.lower()
result = []
n = len(only_words(string)) - 1

# Переворачиваем строку по словам
for i in only_words(string):
    a = only_words(string)[n]
    result.append(a)
    n -= 1

if result == only_words(string):
    print("Это словесный палиндром.")
else:
    print("Это не палиндром.")
