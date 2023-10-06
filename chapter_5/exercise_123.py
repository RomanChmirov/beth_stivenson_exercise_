small_vowels = ['a', 'e', 'i', 'o', 'u']
big_vowels = ['A', 'E', 'I', 'O', 'U']
small_consonants = [chr(i) for i in range(97, 122 + 1) if chr(i) not in small_vowels]
big_consonants = [chr(i) for i in range(65, 90 + 1) if chr(i) not in big_vowels]
vowels = small_vowels + big_vowels
consonants = small_consonants + big_consonants
punctuation_marks = [',', '.', '!', '?']

string = input("Введите строку для перевода в поросячью латынь: ")
lst = string.split()

new_lst = []

pos = 0
for i in lst:

    if i[0] not in (vowels and consonants):
        new_lst.append(i)
        continue
    else:

        if i[0] in vowels:
            if i[0] in big_vowels:
                element = lst[pos] + 'way'
                element = element.capitalize()
            elif i[0] in small_vowels:
                element = lst[pos] + 'way'


        elif i[0] in consonants:
            index = 0
            while i[index: index + 1] in consonants:
                index += 1

            if i[0] in big_consonants:
                element = lst[pos][index::] + lst[pos][: index:] + 'ay'
                element = element.capitalize()
            elif i[0] in small_consonants:
                element = lst[pos][index::] + lst[pos][: index:] + 'ay'

        new_lst.append(element)
        pos += 1


print(new_lst)
