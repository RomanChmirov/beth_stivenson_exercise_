words = []
word = input("Введите слово(для прекращения ввода нажмите Enter): ")
while word:

    # Если слово уже есть в списке не добавляем его
    if word not in words:
        words.append(word)

    word = input("Введите слово(для прекращения ввода нажмите Enter): ")


for i in words:
    print(i)
