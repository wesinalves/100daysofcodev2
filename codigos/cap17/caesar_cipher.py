# Python Journey - Chapter 17
# Class for Caesar Cipher

class CaesarCipher:
    """
    Caesar Cipher is the first proeminent substitution cipher
    was credited to Julius Caeser
    """

    def __init__(self):
        print("Caesar Cipher Algorithm. Enter the information required to start")

        self.key = int(input("Please enter the desired key: "))
        
        self.method = input("Please enter the desired option, \n e for encipher\
                 \n d for decipher and \n b for brute force atack: ").upper().replace(" ","")

        self.message = input("Please enter your text: ").upper()

        

    def shift(self, char, key, dec = True):
        """
        Shifts one letter at time. Dec is a optional parameter indicates decipher mode
        """

        if dec:
            shifted = chr(ord(char) - key)
        else:
            shifted = chr(ord(char) + key)
        
        if shifted > 'Z':
            return chr(ord(shifted) - 26)
        elif shifted < 'A':
            return chr(ord(shifted) + 26)
        else:
            return shifted
        
    
    def encipher(self):
        """
        it iterates over each letter in the message, calling shift method in each loop.
        """

        cipher_text = ""
        for char in self.message:
            cipher_text += self.shift(char, self.key, dec = False)
        
        print(cipher_text)
    
    def decipher(self):
        """
        Does the opposite of encipher
        """

        plain_text = ""
        for char in self.message:
            plain_text += self.shift(char, self.key)

        print(plain_text)

    def brute_force(self):
        """
        Brute force method do decipher a message. The inner loop is similar to decipher.
        The outer loop ensures it happens 26 times, changing the key on each iteration.
        """ 

        for key in range(26):
            plain_text = ""
            for char in self.message:
                plain_text += self.shift(char, key)
            
            print(plain_text)


def main():
    """
    Test the Caesar Cipher.
    Opition Avaiable:
    D -> decipher
    E -> encipher
    B -> brute force atack
    """

    cipher = CaesarCipher()

    OPTIONS_DICT = {
        'D': cipher.decipher,
        'E': cipher.encipher,
        'B': cipher.brute_force
    }

    if cipher.method in OPTIONS_DICT:
        do_it = OPTIONS_DICT[cipher.method]
        do_it()
    else:
        print("Invalid Option")

if __name__ == "__main__":
    main()

