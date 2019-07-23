# Jornada Python - Capítulo 3
# Calculating compound interest.

principal = 1000.0
rate = .05

print("Year %21s" % "Amount on deposit")

for year in range(1, 11):
    amount = principal * (1.0 + rate) ** year
    print("%4d%21.2f" % (year, amount))
