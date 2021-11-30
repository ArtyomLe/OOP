
class CodeInt:
    """Класс для хранения и обработки закодиранного значения числа int"""
    code_string = "ABCDEFG0192837465HIJK!@#$%^&*()_+oli" # Статическая переменная

    def __init__(self, a):
        """Конструктор класса.Создаёт закодированное значение"""
        self.digit = self.code(a)

    def __str__(self):
        """Возвращает текстовое представление объекта"""
        return f"Декодированное: {self.decode()}, хранится в памяти как \"{self.digit}\""   # \" \" помещаем значение в скобки ""

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

    def add(self, n):
        """"ДОБАВЛЯЕТ к текущему значению n"""
        self.digit = self.code(self.decode() + n)

    def sub(self, n):
        """ВЫЧИТАЕТ из текущего значения n"""
        self.digit = self.code(self.decode() - n)
