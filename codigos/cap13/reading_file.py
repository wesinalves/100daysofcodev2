# Python Journey - Chapter 13
# Reading and priting a file.

import sys

# open a file
try:
    file = open('clients.dat','r')
except IOError:
    print("file could not been opened", file=sys.stderr)

records = file.readlines()
print("Account".ljust(10),"Name".ljust(10),"Balance".rjust(10))

for record in records:
    fields = record.split()
    print(fields[0].ljust(10), fields[1].ljust(10), fields[2].rjust(10))

file.close()