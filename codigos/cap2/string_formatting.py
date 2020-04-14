# Como Programar em Python - Capítulo 2
# String formatting demonstration

print("O Senhor é meu pastor, nada me faltará. 'Salmo 23:1'")
print("O Senhor é meu pastor, nada me faltará. \"Salmo 23:1\"")
print('O Senhor é meu pastor, nada me faltará. \'Salmo 23:1\'')
print('O Senhor é meu pastor, nada me faltará. "Salmo 23:1"')

INTEGER_VALUE = 4237.05
print("Integer", INTEGER_VALUE)
print("decimal Integer {:.0f}".format(INTEGER_VALUE))
print("Hexadecimal integer {:x}\n".format(int(INTEGER_VALUE)))
print("Right justify Integer ({:8d})".format(int(INTEGER_VALUE)))
print("Left justify integer (%-8d)\n" % INTEGER_VALUE)

FLOAT_VALUE = 4237.05
print("float", FLOAT_VALUE)
print("default float {:f}".format(FLOAT_VALUE))
print("defual exponential float {:e}\n".format(int(FLOAT_VALUE)))

STRING_VALUE = "String formatting"
print("Force eight digits in integer %.8d" % INTEGER_VALUE)
print("Five digits after decimal in float %.5f" % FLOAT_VALUE)
print("Fifteen and five characters allowed in string:")
print("({:15s}) ({:.5s})".format(STRING_VALUE, STRING_VALUE))
