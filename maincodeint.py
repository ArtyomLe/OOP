
from codeint import CodeInt

a = CodeInt(10)

# Прибавляем CodeInt
a = a + CodeInt(10)
print(a)

# Прибавляем int
a = a + 100
print(a)

# Прибавляем список
n = [32, 2, 1]
a = a + n
print(a)
