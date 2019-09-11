# Journey Python - Chapter 13
# Reads shelve file, updates data
# already written to file, creates data
# to be placed in file and deletes data
# already in file.

import sys
import shelve

# prompt for input menu choice
def enter_choice():

    print("\nEnter your choice")
    print("1 - store a formatted text file of accounts")
    print("     called \"print.txt\" for printing")
    print("2 - update account")
    print("3 - add a new account")
    print("4 - delete a account")
    print("5 - end program")

    while 1:
        menu_choice = int(input("? "))
        if not 1 <= menu_choice <= 5:
            print("Incorret choice", file=sys.stderr)
        else:
            break;
    
    return menu_choice

# create formatted text file for printing
def text_file(read_from_file):
    
    try:
        output_file = open("print.txt", "w")
    except IOError:
        print("File couldn't not been found", file=sys.stderr)
        sys.exit(1)
    
    print("Account".ljust(10), file = output_file)
    print("Last Name".ljust(10), file = output_file)
    print("First Name".ljust(10), file = output_file)
    print("Balance".rjust(10), file = output_file)

    for key in read_from_file.keys():
        print(key.ljust(10), file = output_file)
        print(read_from_file[key][0].ljust(10), file = output_file)
        print(read_from_file[key][1].ljust(10), file = output_file)
        print(read_from_file[key][2].rjust(10), file = output_file)

    output_file.close()

# update account balance
def update_record(update_file):

    account = get_account("Enter account to update")

    if update_file.has_key(account):
        output_line(account, update_file[account])

        transaction = input("\nEnter charge (+) or payment (-): ")

        # create temporary record to alter data
        temp_record = update_file[account]
        temp_balance = float(temp_record[2])
        temp_balance += float(transaction)
        temp_balance = "%.2f" % temp_balance
        temp_record[2] = temp_balance

        #update record in shelve
        del update_file[account] # remove old record first
        update_file[account] = temp_record
        output_line(account, update_file[account])
    else:
        print("Account doesn't exist", file = sys.stderr)

# create and insert new record
def new_record(insert_infile):

    account = get_account("Enter account to update")

    if not insert_infile.has_key(account):
        print("Enter lastname, firstname, balance")
        current_data = input("? ")
        insert_infile[account] = current_data.split()
    else:
        print("Account", account, "already exists", file = sys.stderr)


