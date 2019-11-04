# Python Journey - Chapter 17
# Transposition Cipher Encryption Program

import pyperclip

def main():
    #my_message = 'In the begining God created the universe.'
    my_message = 'Common sense is not so common.'
    my_key = 8

    cipher_text = encrypt(my_key, my_message)

    print(cipher_text + '|')

    pyperclip.copy(cipher_text)

def encrypt(key, message):

    cipher_text = [''] * key

    for col in range(key):
        pointer = col

        # keep looping util pointer goes past the length of the message
        while pointer < len(message):
            # place the character at pointer in message at the end of the
            # current column in the cipher text list

            cipher_text[col] += message[pointer]
            pointer += key

    # Convert the ciphertext list into a single string value and return it.
    return ''.join(cipher_text)


if __name__ == '__main__':
    main()    
    
