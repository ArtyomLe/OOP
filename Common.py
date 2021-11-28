
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
print(Max2.getMax(10, 50)) # Создаём ОБЪЕКТ вызываем класс по имени "Max2"

# Класс = это блок кода к которому можно обратиться из другого места программы

# Расположенные внутри класса функции называются методами
class MyFirstClass:
    def getSumma(a):
        s = 0
        while (a > 0):
            s += a % 10
            a //= 10
        return s


    def getMax(a):
        m = 0
        while (a > 0):
            if (a % 10 > m):
                m = a % 10
            a //= 10
        return m
print(MyFirstClass.getSumma(1145))
print(MyFirstClass.getMax(45))

class Slova:
    def getPrivet(a):
        return a
    def getKak(b):
        return b
print(Slova.getPrivet("Привет,"), Slova.getKak("как дела?"))
