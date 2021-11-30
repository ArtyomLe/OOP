
# Важно использовать разные символы в кодовой строке
cString = "@#$"                    # Кодовая строка (троичная система счисления)

n = "$$$#"                         #  2221 в троичной системе счисления ($ = 2, # = 1)
base = len(cString)                # 3
res = 0

for i in range(len(n)):
    res = res * base + cString.find(n[i])   # res = 0 * 3 + 2 = 2
                                            # res = 2 * 3 + 2 = 8
                                            # res = 8 * 3 + 2 = 26
                                            # res = 26 * 3 + 1 = 79
print(res)
# Результат: 79 (Число 2221 в троичной системе счисления равно 79 в десятичной)