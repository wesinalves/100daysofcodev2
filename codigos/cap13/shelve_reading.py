# Journey Python - Chapter 13
# Reading from shelve file.

import sys
import shelve

def output_line(account, aList):
    print(account.ljust(10), aList[0].ljust(10), aList[1].ljust(10), aList[2].rjust(10))

try:
    credit_file = shelve.open('credit')
except IOError:
    print("File could not been open", file = sys.stderr)
    sys.exit(1)

print("Account".ljust(10), "Last Name".ljust(10), "First Name".ljust(10), "Balance".rjust(10))

# display each account
for account_number in credit_file.keys():
    output_line(account_number, credit_file[account_number])

credit_file.close()