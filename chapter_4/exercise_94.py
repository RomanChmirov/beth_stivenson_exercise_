## Функция определяет возможность построения треугольника из 3 отрезков
# @param a — 1 отрезок
# @param b — 2 отрезок
# @param c — 3 отрезок
# @return возможность построения треугольника из 3 отрезков(True or False)
def define_a_triangle(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        result = False
    else:

        if a >= b + c or b >= a + c or c >= a + b:
            result = False
        else:
            result = True

    return result


first_segment = float(input("Введите 1 отрезок: "))
second_segment = float(input("Введите 2 отрезок: "))
third_segment = float(input("Введите 3 отрезок: "))

if define_a_triangle(first_segment, second_segment, third_segment):
    print(f"Из отрезков {first_segment}, {second_segment}, {third_segment}, можно построить треугольник.")
else:
    print(f"Из отрезков {first_segment}, {second_segment}, {third_segment}, нельзя построить треугольник.")
