from random import randint

lst = []

while len(lst) < 6:
    item = randint(1, 50)

    if item in lst:
        continue
    else:
        lst.append(item)

lst.sort()

print(*lst)
