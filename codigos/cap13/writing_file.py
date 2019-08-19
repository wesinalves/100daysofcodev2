# Python Journey - Chapter 13
# Opening and writing to a file.

import sys

#open a file with try/except
try:
    file = open("clients.dat", "w")
except IOError as message:
    print("File could not be opened: ", message, file=sys.stderr)
    sys.exit()

print("Enter the account, name and balance.")
print("Enter end-of-file to end input.")

while 1:
    try:
        account_line = input("? ")
    except EOFError:
        break
    else:
        print(account_line, file = file)