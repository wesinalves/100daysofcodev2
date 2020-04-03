# Como Programar em Python - Capítulo 2
# String formatting demonstration

print("O Senhor é meu pastor, nada me faltará. 'Salmo 23:1'")
print("O Senhor é meu pastor, nada me faltará. \"Salmo 23:1\"")
print('O Senhor é meu pastor, nada me faltará. \'Salmo 23:1\'')
print('O Senhor é meu pastor, nada me faltará. "Salmo 23:1"')

integerValue = 4237.05
print("Integer", integerValue)
print("decimal Integer {:.0f}".format(integerValue))
print("Hexadecimal integer {:x}\n".format(int(integerValue)))
print("Right justify Integer ({:8d})".format(int(integerValue)))
print("Left justify integer (%-8d)\n" % integerValue)

floatValue = 4237.05
print("float", floatValue)
print("default float {:f}".format(floatValue))
print("defual exponential float {:e}\n".format(int(floatValue)))

stringValue = "String formatting"
print("Force eight digits in integer %.8d" % integerValue)
print("Five digits after decimal in float %.5f" % floatValue)
print("Fifteen and five characters allowed in string:")
print("({:15s}) ({:.5s})".format(stringValue, stringValue))
