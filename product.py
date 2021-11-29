
class Product:

    # В классе-конструкторе инициализируем поля класса
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def __str__(self): # Текстовое представление объекта
        return f"{self.name:22} Кол-во: {str(self.count):10} Цена: {str(self.price):10} СУММА: {str(self.getPrice()):20}"

    def printCurrent(self): # Вывод строки для каждого товара
        print(f"\nТовар: {self.name.upper()}, количество: {self.count}")

    def add(self, adding): # Метод добавляющий товар
        print(f"Добавленно {adding} единиц {self.name}")
        self.count += adding

    def adding(self): # Запрос необходимого для добавления кол-ва товара и вызывающий (def add) с введённым пользователем аргументом
        self.printCurrent()
        self.add(int(input("Введите, сколько товара добавить (0 - выход): ")))

    def extract(self, ext): # Метод выгружающий товар (вычитает из count указанное аргументом ext количество)
        if ext > self.count:
            print(f"Невозомжно разгрузить {ext} единиц {self.name} (остаток: {self.count})")
            return False
        self.count -= ext
        return True

    def extracting(self): # Метод передающий в (def extract) через переменную а кол-во товара для разгрузки
        self.printCurrent()
        a = int(input("Сколько товара выгрузить (0 - выход): "))
        if (not self.extract(a)): # В случае если (def extract) возвращает False (просим больше чем есть в наличии) то получаем рекурсию
            self.extracting()

    def getPrice(self): # Метод возвращающий общую сумму товара (кол-во x цена)
        return self.count * self.price

    def menu(self): # Метод формирующий меню и обрабатывающий ввод пользователя
        self.printCurrent()
        print("1. Загрузить")
        print("2. Выгрузить")
        print("0. ВЫХОД")
        m = input("Выберите действие: ")
        if m == "1":                    # Скрипт запускающий нужные нам операции
            self.adding()
        elif m == "2":                  # Скрипт запускающий нужные нам операции
            self.extracting()
