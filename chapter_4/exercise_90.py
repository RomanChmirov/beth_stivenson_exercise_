from exercise_89 import converting_integers_to_numerals

line_for_the_first_verse = "A partridge in a pear tree."
line_for_next_couplets = "And a partridge in a pear tree."


## Функция выполняет написание одного куплета песни
# @param n — номер куплета
# @return один куплет песни
def verse_display(n):
    numeral_day = converting_integers_to_numerals(n)
    print(f"On {numeral_day} day of Christmas")
    print("My true love gave to me")

    if n == 12:
        print("Twelve drummers drumming,")
    if n >= 11:
        print("Eleven pipers piping,")
    if n >= 10:
        print("Ten lords a-leaping,")
    if n >= 9:
        print("Nine ladies dancing,")
    if n >= 8:
        print("Eight maids a-milking,")
    if n >= 7:
        print("Seven swans a-swimming,")
    if n >= 6:
        print("Six geese a-laying,")
    if n >= 5:
        print("Five golden rings,")
    if n >= 4:
        print("Four calling birds,")
    if n >= 3:
        print("Three French hens,")
    if n >= 2:
        print("Two turtle doves")

    if n == 1:
        print(line_for_the_first_verse)
    else:
        print(line_for_next_couplets)


# Выводим песню
for i in range(1, 13):
    verse_display(i)
    print()
