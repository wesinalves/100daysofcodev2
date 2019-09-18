# Python Journey - Chapter 13
# Reading pickled object from a file.

import sys, pickle

# open file
try:
    file = open("users.dat", "rb")
except IOError:
    print("File not found", file = sys.stderr)
    sys.exit(1)

records = pickle.load(file)
file.close()

print("Name".ljust(10), "Date of birth".rjust(20))

for record in records:
    print(record[0].ljust(10), record[1].rjust(20))

