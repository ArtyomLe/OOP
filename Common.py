"""
# НОД => Наибольший общий делитель двух чисел
a = int(input("Введите А: "))
b = int(input("Введите В: "))

while (a != 0) and (b != 0):
    if (a > b):
        a %= b
    else:
        b %= a

print(f"НОД = {a+b}")
"""
# Сумма значений списка
a = [10, 25, -29, 23]
s = 0

for i in a:
    s += i
print(s)

a = [10, 25, -29, 23]
s = 0

for i in range(len(a)):
    s += a[i]
print(s)

a = [10, 25, -29, 23]
print(sum(a))       # Встроеная функция Python