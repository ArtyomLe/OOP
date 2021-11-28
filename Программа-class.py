
"""
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if (a % b == 0):
    print(f"{a} делится на {b}")
else:
    print(f"{a} не делится на {b}")


# Оформляем данный процесс как класс
class Divisibility:
    def __init__(self):                             # Конструктор класса (Чтобы вызывать метод без . )
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        if a % b == 0:
            print(f"{a} делится на {b}")
        else:
            print(f"{a} не делится на {b}")
# Создаём(вызываем) ОБЪЕКТ а основе класса
if __name__ == '__main__':
    Divisibility()

"""

class Experiment:
    def run(self):
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        if (a % b == 0):
            print(f"{a} делится на {b}")
        else:
            print(f"{a} не делится на {b}")
if __name__ == '__main__':
    Experiment().run()