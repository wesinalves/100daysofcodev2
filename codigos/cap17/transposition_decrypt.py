# Python Journey - Chapter 17
# Transposition Cipher Decryption Program

import math, pyperclip

def main():
    my_message = "IeGtu.ngoen idditn  vhicteenrhr geesb a e"
    my_key = 8

    plain_text = decrypt_message(my_key, my_message)

    print(plain_text + '|')
    pyperclip.copy(plain_text)


def decrypt_message(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values

    columns_number = math.ceil(len(message) / key)
    rows_number = key

    shadedbox_number = (columns_number * rows_number) - len(message)
    plain_text = [''] * columns_number

    # col and row point to where in the grid the next character will go
    col = 0
    row = 0

    for symbol in message:
        plain_text[col] += symbol
        col += 1

        # if there are no more columns or we're at a shaded box, go back to 
        # the first column and the newt row
        if (col == columns_number) or (col == columns_number - 1 and row >= rows_number - shadedbox_number):
            col = 0
            row += 1
    
    return ''.join(plain_text)

if __name__ == "__main__":
    main()