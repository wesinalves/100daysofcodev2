'''
How to program in Python - Chapter 13
Writing to shelve file.
'''

import sys
import shelve

def main():
    '''Main Function'''
    try:
        out_credit = shelve.open('credit')
    except IOError:
        print("File could not been open", file = sys.stderr)
        sys.exit(1)

    print("Enter account number (1 to 100, 0 to end input)")

    # get account information
    while 1:
        account_number = int(input("\nEnter account number\n?" ))

        if 0 < account_number <= 100:
            print("Enter lastname, firstname, balance")
            current_data = input("? ")
            out_credit[str(account_number)] = current_data.split()
        elif account_number == 0:
            break

    out_credit.close()

main()
