# Python Journey - Chapter 11
# Manipulating string.

string1 = "Tudo posso naquele que me fortalece!"

print(string1.center(50))
print(string1.ljust(50))
print(string1.rjust(50))


string2 = "\t \n Nem só de pão vive o homem. \t\t \n"

print('Original string: "%s"\n' % string2)
print('Using strip: "%s"\n' % string2.strip())
print('Using left strip: "%s"\n' % string2.lstrip())
print('Using right strip: "%s"\n' % string2.rstrip())



