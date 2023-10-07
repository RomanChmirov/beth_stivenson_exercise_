xs = []
ys = []

amount_points = 0
x = float(input("Введите координату точки по оси x(для прекращения ввода 0): "))
while x:
    xs.append(x)
    y = float(input("Введите координату точки по оси y(для прекращения ввода 0): "))
    ys.append(y)
    x = float(input("Введите координату точки по оси x(для прекращения ввода 0): "))
    amount_points += 1

# Считаем коэффициенты m и b
xy = []
x_squared = []

for i in range(0, amount_points):
    xy.append(xs[i] * ys[i])

for i in range(0, amount_points):
    x_squared.append(xs[i] ** 2)

m = (sum(xy) - sum(xs) * sum(ys) / amount_points) / (sum(x_squared) - sum(xs) ** 2 / amount_points)


b = sum(ys) / len(ys) - m * (sum(xs) / len(xs))

str_best_line = f"y = %.2fx + %.2f" % (m, b)

print(f"Формула линии наилучшего соответствия: {str_best_line}.")
