numbers = []
minmid_numbers = []
maxmid_numbers = []
mid_numbers = []

# Добавляем введённые элементы в список
num = float(input("Введите число(для прекращения ввода введите 0): "))
while num:
    numbers.append(float(num))
    num = float(input("Введите число(для прекращения ввода введите 0): "))

print(numbers)
mid_num = sum(numbers) / len(numbers)

for i in numbers:

    if i < mid_num:
        minmid_numbers.append(str(i))
    elif i == mid_num:
        mid_numbers.append(str(i))
    else:
        maxmid_numbers.append(str(i))

print(f"Числа, которые меньше среднего: {minmid_numbers} \n"
      f"Числа, которые равны среднему: {mid_numbers} \n"
      f"Числа, которые больше среднего: {maxmid_numbers}")
