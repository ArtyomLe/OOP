class Multipliers:
    """Хранит число и работает с его множителями.

    Применяется при обработке множителей натурального числа.

    АТРИБУТЫ:
    ---------
    dgt : int
        целое число (по умолчанию 1).
    muls : list
        список множителей числа в порядке возрастания.

    МЕТОДЫ:
    -------
    getMinMul()   -- вернёт первый множитель больше единицы.
    getIdxMul()   -- вернёт множитель по номеру x.
    getListMul()  -- вернёт список множителей по возрастанию.
    getSumMul()   -- вернёт сумму множителей.

    ПРИМЕЧАНИЕ:
    -----------
    Число обязательно должно быть натуральным.

    ОШИБКИ:
    -------
    Генерирует исключение IndexError в getIdxMul(x),
    если x выходит за границы диапазона списка.
    """
    def __init__(self, dgt=1):
        """Значение аргумента dgt хранится в объекте в поле dgt"""
        self.dgt = dgt
        self.muls = self.getListMul()

    def __str__(self):
        """Выведет строку множителей, разделённую пробелами."""
        return ' '.join(map(str, self.muls))

    def getMinMul(self):
        """Вернёт первый множитель, который больше единицы."""
        return self.muls[1]

    def getIdxMul(self, x):
        """Вернёт множитель по номеру x.
        Не допускайте выхода за границы диапазона для x!"""
        return self.muls[x]

    def getListMul(self):
        """Найдёт и вернёт список множителей."""
        r = []
        for i in range(1, int(self.dgt ** 0.5) + 1):
            if (self.dgt % i == 0):
                r.append(self.dgt // i)
        return sorted(r)

    def getSumMul(self):
        """Вернёт сумму множителей."""
        return sum(self.muls)