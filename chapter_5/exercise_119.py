numbers = []
minmid_numbers = []
maxmid_numbers = []
mid_numbers = []

# Добавляем введённые элементы в список
num = float(input("Введите число(для прекращения ввода введите 0): "))
while num:
    numbers.append(float(num))
    num = float(input("Введите число(для прекращения ввода введите 0): "))

mid_num = sum(numbers) / len(numbers)

# Распределяем числа по спискам
for i in numbers:

    if i < mid_num:
        minmid_numbers.append(str(i))
    elif i == mid_num:
        mid_numbers.append(str(i))
    else:
        maxmid_numbers.append(str(i))

# Выводим списки чисел
print(f"Числа ниже среднего: ", end='')
for j in minmid_numbers:
    print(j, end='; ')
print()

if mid_numbers:
    print(f"Числа равные среднему: ", end='; ')
    for l in mid_numbers:
        print(l, end='; ')
    print()

print(f"Числа выше среднего: ", end='')
for t in maxmid_numbers:
    print(t, end='; ')
print()
