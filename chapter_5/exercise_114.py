integers = []
# Добавляем введённые элементы в список
num = (input("Введите число(для прекращения ввода нажмите Enter): "))
while num != '':
    integers.append(num)
    num = (input("Введите число(для прекращения ввода нажмите Enter): "))

for i in integers:

    if int(i) < 0:
        print(i)

for i in integers:
    if int(i) == 0:
        print(i)

for i in integers:
    if int(i) > 0:
        print(i)
