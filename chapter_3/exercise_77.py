# Получаем первую строку и переходим на следующую
print('    ', end='')


for i in range(1, 11):
    print('%4i' % i, end='')


# Получаем вторую и следующие строки
for i in range(1, 11):
    print()

    print('%4i' % i, end='')


    for j in range(1, 11):
        print('%4i' % (i * j), end='')
