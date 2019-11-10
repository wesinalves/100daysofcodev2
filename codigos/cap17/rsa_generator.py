# Python Journey - Chapter 18
# RSA key generator

import random, sys, os, rabinMiller, cryptomath

def main():
    print('Making key files...')
    make_keyfiles('wr_alves', 1024)
    print('Key files made.')

def generate_key(key_size):
    # Creates a public/private key pair with keys that are key_size bits in
    # size. This function may take a while to run.

    # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
    print('Generating p prime...')
    p = rabinMiller.generate_large_prime(key_size)
    print('Generating q prime...')
    q = rabinMiller.generate_large_prime(key_size)
    n = p * q

    # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
    print('Generating e that is relatively prime to (p-1)*(q-1)...')
    while True:
        # Keep trying random numbers for e until one is valid.
        e = random.randrange(2 ** (key_size - 1), 2 ** key_size)
        if cryptomath.gcd(e, (p - 1) * (q -1)) == 1:
            break
    
    # Step 3: Calculate d, the mod inverse of e.
    print('Calculating d that is mod inverse of e...')
    d = cryptomath.find_module_inverse(e, (p - 1) * (q - 1))

    public_key = (n, e)
    private_key = (n, d)

    print('Public key: ', public_key)
    print('Private key: ', private_key)

    return (public_key, private_key)

def make_keyfiles(name, key_size):
    # Creates two files 'x_pubkey.txt' and 'x_privkey.txt' (where x is the
    # value in name) with the the n,e and d,e integers written in them,
    # delimited by comma

    # Our safety check will prevent us from overwriting our old key files:
    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
        sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt already\
            exists! Use a different name or delete these files and re-run this program.' % (name, name))
    
    public_key, private_key = generate_key(key_size)

    print()
    print('The public key is a %s and a %s digit number.' % (len(str(public_key[0])), len(str(public_key[1]))))
    print('Writing public key to file %s_pubkey.txt...' % (name))
    fo = open('%s_pubkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (key_size, public_key[0], public_key[1]))
    fo.close()

    print()
    print('The private key is a %s and a %s digit number.' % (len(str(private_key[0])), len(str(private_key[1]))))
    print('Writing private key to file %s_privkey.txt...' % (name))
    fo = open('%s_privkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (key_size, private_key[0], private_key[1]))
    fo.close()

if __name__ == "__main__":
    main()





