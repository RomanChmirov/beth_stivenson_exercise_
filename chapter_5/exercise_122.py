vowels = ['a', 'e', 'i', 'o', 'u']

string = input('Введите строку для перевода в "поросячью латынь": ')
lst = string.split()

for i in lst:

    if i[0] in vowels:
        lst[lst.index(i)] += 'way'
    else:
        index = 0
        while i[index: index + 1] not in vowels:
            index += 1
        lst[lst.index(i)] = lst[lst.index(i)][index::] + lst[lst.index(i)][: index:] + 'ay'


print(f'Строка на "поросячьей латыни": ')
print(*lst)
