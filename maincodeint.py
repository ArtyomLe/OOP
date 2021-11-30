
from codeint import CodeInt

a = CodeInt(100)
b = CodeInt(50)

a.digit = a.code(a.decode() + b.decode())
print(a)