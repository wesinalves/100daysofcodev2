# Python Journey - Chapter 13
# Opening and writing pickled object to file.

import sys, pickle

# open file
try:
    file = open("users.dat", "wb")
except IOError:
    print("File not found", file = sys.stderr)
    sys.exit(1)

print("Enter the user name, name and date of birth.")
print("Enter end-of-file to end input.")

input_list = []

while 1:

    try:
        account_line = input("? ")
    except EOFError:
        break
    else:
        input_list.append(account_line.split())

pickle.dump(input_list, file)

#file.close()

