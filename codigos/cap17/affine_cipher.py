# Python Journey - Chapter 18
# Affine Cipher program

import sys
import pyperclip
import cryptomath
import random

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]
^_`abcdefghijklmnopqrstuvwxyz{|}~""" # note the space at the front

def main():
    my_massage = """A computer would deserve to be called intelligent if it \
        could deceive a human into believing that it was human." -Alan Turing"""
    
    my_key = 2023
    my_mode = "encrypt"

    if my_mode == "encrypt":
        translated = encrypt_message(my_key, my_massage)
    elif my_mode == "decrypt":
        translated = decrypt_message(my_key, my_massage)
    
    print('Key: %s' % (my_key))
    print('%sed text:' % (my_mode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('Full %sed text copied to clipboard.' % (my_mode))

def get_keys(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)

    return (keyA, keyB)

def check_keys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key A is set to 1. Choose another key')
    
    if keyB == 0 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key B is set to 0. Choose another key')
    
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
    
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not \
            relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))

def encrypt_message(key, message):
    keyA, keyB = get_keys(key)
    check_keys(keyA, keyB, 'encrypt')
    cipher_text = ''
    for symbol in message:
        if symbol in SYMBOLS:
            # encrypt this symbol
            sym_index = SYMBOLS.find(symbol)
            cipher_text += SYMBOLS[(sym_index * keyA + keyB) % len(SYMBOLS)]
        else:
            cipher_text += symbol # just append this symbol unencrypted

    return cipher_text

def decrypt_message(key, message):
    keyA, keyB = get_keys(key)
    check_keys(keyA, keyB, 'decrypt')
    plain_text = ''

    inverse_keyA = cryptomath.findmod_inverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            # decrypt this symbol
            sym_index = SYMBOLS.find(symbol)
            plain_text += SYMBOLS[(sym_index - keyb) * inverse_keyA % len(SYMBOLS)]
        
        else: 
            plain_text += symbol
    
    return plain_text

def random_key():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))

        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

if __name__ == "__main__":
    main()
     
