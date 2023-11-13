"""
# Journey Python - Chapter 40
# Reading files.
"""

file = open('/home/wesin/Imagens/Capturas de tela/Captura de tela de 2023-08-23 14-41-11.png', 'rb')

for line in file:
    print(line, end='')
#print(file.read(1))

file.close()