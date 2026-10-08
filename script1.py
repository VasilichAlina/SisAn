# a = float(input("Введите коэффициент a: "))
# b = float(input("Введите коэффициент b: "))
# c = float(input("Введите коэффициент c: "))
#
# left = float(input("Введите левую границу: "))
# right = float(input("Введите правую границу: "))
#
# E = float(input("Введите E: "))
# L = float(input("Введите L: "))
#
# # Функция
# def f(x):
#     global function_calls
#     function_calls += 1
#     return a * x**2 + b * x + c
#
#
# function_calls = 0
# iterations = 0
#
# # Метод дихотомии
# while right - left > L:
#
#     y = (left + right - E) / 2
#     z = (left + right + E) / 2
#
#     fy = f(y)
#     fz = f(z)
#
#     if fy < fz:
#         right = z
#     else:
#         left = y
#
#     iterations += 1
#
#
# x_min = (left + right) / 2
# f_min = f(x_min)
#
# print()
# print("Результат:")
# print("Точка минимума:", x_min)
# print("Минимальное значение:", f_min)
# print("Количество итераций:", iterations)
# print("Количество вычислений функции:", function_calls)
########################zolotoe sechenie###########################################
# import math
#
# a = float(input("Введите коэффициент a: "))
# b = float(input("Введите коэффициент b: "))
# c = float(input("Введите коэффициент c: "))
#
# left = float(input("Введите левую границу: "))
# right = float(input("Введите правую границу: "))
#
# L = 1
#
#
# def f(x):
#     global function_calls
#     function_calls += 1
#     return a * x**2 + b * x + c
#
#
# function_calls = 0
# k = 0
#
# phi = (math.sqrt(5) - 1) / 2
# q = (3 - math.sqrt(5)) / 2
#
# y = left + q * (right - left)
# z = left + right - y
#
# fy = f(y)
# fz = f(z)
#
# while abs(right - left) > L:
#
#     if fy <= fz:
#         right = z
#         z = y
#         fz = fy
#         y = left + right - z
#         fy = f(y)
#
#     else:
#         left = y
#         y = z
#         fy = fz
#         z = left + right - y
#         fz = f(z)
#
#     k += 1
#
#
# x_min = (left + right) / 2
# f_min = a * x_min**2 + b * x_min + c
#
# print()
# print("Результат:")
# print("Точка минимума:", x_min)
# print("Минимальное значение:", f_min)
# print("Количество итераций:", k)
# print("Количество вычислений функции:", function_calls)
#################################################################
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

left = float(input("Введите левую границу: "))
right = float(input("Введите правую границу: "))

E = float(input("Введите E: "))
L = float(input("Введите L: "))


def f(x):
    global function_calls
    function_calls += 1
    return a * x**2 + b * x + c


function_calls = 0
iterations = 0

# Числа Фибоначчи
fib = [0, 1]

while fib[-1] < (right - left) / L:
    fib.append(fib[-1] + fib[-2])

N = len(fib) - 1

# Первые две точки
y = left + fib[N - 2] / fib[N] * (right - left)
z = left + fib[N - 1] / fib[N] * (right - left)

fy = f(y)
fz = f(z)

k = 0

# Основные итерации
while k != N - 3:

    if fy <= fz:
        new_left = left
        new_right = z

        new_y = new_left + fib[N - k - 3] / fib[N - k - 1] * (new_right - new_left)
        new_z = y

        new_fy = f(new_y)
        new_fz = fy

    else:
        new_left = y
        new_right = right

        new_y = z
        new_z = new_left + fib[N - k - 2] / fib[N - k - 1] * (new_right - new_left)

        new_fy = fz
        new_fz = f(new_z)

    left = new_left
    right = new_right
    y = new_y
    z = new_z
    fy = new_fy
    fz = new_fz

    iterations += 1
    k += 1


# Заключительный шаг
y = (left + right) / 2
z = y + E

fy = f(y)
fz = f(z)

if fy <= fz:
    right = z
else:
    left = y

iterations += 1

x_min = (left + right) / 2

# Значение функции отдельно
f_min = a * x_min**2 + b * x_min + c

print()
print("Результат:")
print("N =", N)
print("Точка минимума:", x_min)
print("Минимальное значение:", f_min)
print("Количество итераций:", iterations)
print("Количество вычислений функции:", function_calls)