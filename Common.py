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

# Сумма значений списка (Списки - это структура)
a = [10, 25, -29, 23]
s = 0

for i in a:
    s += i
print(s)
# ==============================================
a = [10, 25, -29, 23]
s = 0

for i in range(len(a)):
    s += a[i]
print(s)
# ==============================================
a = [10, 25, -29, 23]
print(sum(a))       # Встроеная функция Python


# Максимальное число из двух

class Max2:
    def getMax(a, b):
        if a > b:
            return a
        return b
print(Max2.getMax(10, 50))

# Класс = это блок кода к которому можно обратиться из другого места программы
"""

class Cmn:
    def getSumma(a):
        for i in range(a):
            a += i
        return a
    def getMax(b):
        m = 0
        while (b > 0):
            if (b % 10 > m):
                m = b % 10
            b //= 10
        return m
print(Cmn.getSumma(4), Cmn.getMax(12346))
