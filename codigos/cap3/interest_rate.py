'''
How to program in Python - Chapter 3
Calculating compound interest.
'''

PRINCIPAL = 1000.0
RATE = .05

print("Year %21s" % "Amount on deposit")

for year in range(1, 11):
    amount = PRINCIPAL * (1.0 + RATE) ** year
    print("%4d%21.2f" % (year, amount))
