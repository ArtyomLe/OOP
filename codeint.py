
class CodeInt:
    """Класс для хранения и обработки закодиранного значения числа int"""

    code_string = "ABCDEFG0192837465HIJK!@#$%^&*()_+oli" # Статическая переменная

    def __init__(self, a):
        """Конструктор класса.Создаёт закодированное значение"""
        self.digit = self.code(a)

    def __str__(self):
        """Возвращает ТЕКСТОВОЕ представление объекта"""
        return str(self.decode())

    def __int__(self):
        """Возвращает ЦЕЛОЧИСЛЕННОЕ представление объекта"""
        return self.decode()

    def __add__(self, other):
        """Вызывается при СЛОЖЕНИИ, ПЕРВЫЙ операнд CodeInt"""

        if isinstance(other, CodeInt):
            # Если аргумент - обьект класса CodeInt
            return CodeInt(self.decode() + other.decode())

        elif isinstance(other, int):
            # Если аргумент - обьект int
            return  CodeInt(self.decode() + other)

        # В любом другом случае
        return NotImplemented

    def __radd__(self, other):
        """Вызывается при СЛОЖЕНИИИ, ВТОРОЙ операнд CodeInt"""
        return self.__add__(other)

    def __sub__(self, other):
        """Вычитание self - other"""

        if isinstance(other, CodeInt):
            return CodeInt(self.decode() - other.decode())
        elif isinstance(other, int):
            return CodeInt(self.decode() - other)

        return NotImplemented

    def __rsub__(self, other):
        """Вычитание other - self"""

        if isinstance(other, CodeInt):
            return CodeInt(other.decode() - self.decode())
        elif isinstance(other, int):
            return CodeInt(other - self.decode())

        return NotImplemented

    def __iadd__(self, other):
        """Вызывается при использовании знака += (self += other)"""
        return self.__add__(other)

    def __isub__(self, other):
        """Вызывается при использовании знака -= (self -= other)"""
        return self.__sub__(other)

    def __gt__(self, other):
        """Вызывается при сравнении self > other"""

        if isinstance(other, CodeInt):
            return self.decode() > other.decode()

        elif isinstance(other, int):
            return self.decode() > other

        return NotImplemented

    def __lt__(self, other):
        """Вызывается при сравнении self < other"""

        if isinstance(other, CodeInt):
            return self.decode() < other.decode()

        elif isinstance(other, int):
            return self.decode() < other

        return NotImplemented


    def code(self, n):
        """КОДИРУЕТ число n в строку"""
        if n == 0:
            return CodeInt.code_string[0]
        base = len(CodeInt.code_string)     # 36 - тичное
        res = ""
        while n > 0:
            res = CodeInt.code_string[n % base] + res
            n //= base
        return res

    def decode(self):
        """ДЕКОДИРУЕТ текущую строку в число int"""
        base = len(CodeInt.code_string)
        res = 0

        for i in range(len(self.digit)): # Закодированое число 100
            res = res * base + CodeInt.code_string.find(self.digit[i])
          # res = 0 * 36 + 2 = 2
          # res = 2 * 36 + 28 = 100
        return res
