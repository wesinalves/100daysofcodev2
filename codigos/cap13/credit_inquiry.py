'''
How to program in Python - Chapter 13
# Credit inquiry program.
'''

import sys


def get_request():
    '''Request input'''
    while 1:
        request = int(input("\n? "))
        if 1 <= request <= 4:
            break

    return request


def should_display(accountType, balance):
    '''determine if balance should be displayed, based on type'''
    if accountType == 2 and balance < 0:
        return 1
    elif accountType == 3 and balance > 0:
        return 1
    elif accountType == 1 and balance == 0:
        return 1
    else:
        return 0


def output_line(account, name, balance):
    '''print formatted balance data'''
    print(account.ljust(10), name.ljust(10), balance.rjust(10))


def main():
    '''Main Function'''
    # open file
    try:
        file = open("clients.dat", "r")
    except IOError:
        print("File could not been open", file=sys.stderr)
        sys.exit(1)

    print("Enter request")
    print("1 - List accounts with zero balances")
    print("2 - List accounts with credit balances")
    print("3 - List accounts with debit balances")
    print("4 - End of run")

    # process user request(s)
    while 1:
        request = get_request()

        if request == 1:
            print("\nAccounts with zero balances:")
        elif request == 2:
            print("\nAccounts with credit balances:")
        elif request == 3:
            print("\nAccounts with debit balances:")
        elif request == 4:
            break
        else:
            print("\nInvalid Request")

        current_record = file.readline()

        # process each line
        while(current_record != ""):
            account, name, balance = current_record.split()
            balance = float(balance)

            if should_display(request, balance):
                output_line(account, name, str(balance))

            current_record = file.readline()

        file.seek(0, 0)

    print("\n End of run")
    file.close()

    print("\n End of run")


main()
