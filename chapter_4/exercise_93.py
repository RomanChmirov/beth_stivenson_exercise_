## Функция центрирует строку
# @param s — строка
# @param w — ширина окна в символах
# @return отцентрированная строка
def center_the_line(s, w):

    if len(s) >= w:
        news = s
    else:
        # Рассчитываем кол-во ведущих пробелов
        spaces = (w - len(s)) // 2
        # и добавляем их в начало строки
        news = spaces * " " + s

    return news


# Примеры использования функции
print(center_the_line("qwerty", 8))
print(center_the_line("Very important person!", 15))
print(center_the_line("My laptop.", 34))
print(center_the_line("Roman", 45))