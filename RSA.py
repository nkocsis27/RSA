import random

def squareAndMultiply(x, e, n):
    """Calculates x^e mod n using the square and multiply algorithm."""
    y = 1
    binRep = bin(e)[2:]  # Binary representation without the '0b' prefix

    # Performs the operation on each bit of e
    for bit in binRep:
        y = (y * y) % n
        if bit == '1':
            y = (y * x) % n

    # Return the result of square and multiply
    return y


def gcd(a, b):
    """Returns the greatest common divisor of a and b using the Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return a


def modInverse(a, n):
    """Returns the inverse of a mod n using the extended Euclidean algorithm."""
    x, _ = extendedEuclidean(a, n)

    return x % n


def extendedEuclidean(a, b):
    '''returns x, y so that a*x + b*y = gcd(a,b)'''
    #included in template, feel free to use
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    while (b != 0):
        q = a//b
        r = a%b
        
        m = s - t*q
        n = old_s - old_t*q
        
        a, b = b, r
        s, old_s = t, old_t
        t, old_t = m , n
        
    return old_s, s

def setup(p, q):
    """Given prime numbers p and q, calculate n, e, and d for RSA. Return n, e, d."""
    n = p * q
    theta = (p - 1) * (q - 1)
    
    while True:
        e = random.randint(2, theta - 1) # Pick random number between 2 and theta
        if gcd(e, theta) == 1: # Check if number is prime by seeing if GCD of e and theta is 1
            break
    
    # Private key is inverse of e and theta
    d = modInverse(e, theta)
    if d is None: # Should never happen if gcd is equal to 1
        raise ValueError("No modular inverse found. Choose different primes.")
    
    return n, e, d


def main():
    """Asks the user to enter a message, encrypts and decrypts it, and repeats until the message is 0."""
    # p and q should be relatively large for RSA to encrypt and decrypt correctly
    p = int(input("Please enter a prime number for p: ")) 
    q = int(input("Please enter a prime number for q: "))
    
    n, e, d = setup(p, q)
    
    # Output public and private key info
    print("Public Key: ({},{})".format(n, e))
    print("Private Key: {}".format(d))

    # Prompt user for a message as a number to encrypt and decrypt using RSA
    message = input("Enter a message (number) to encrypt, or 0 to exit: ")
    while message != "0":
        message = int(message)
        
        # Encrypt the message
        encrypt = squareAndMultiply(message, e, n)
        print("Encryption: {}".format(encrypt))
        
        # Decrypt the message
        decrypt = squareAndMultiply(encrypt, d, n)
        print("Decryption: {}".format(decrypt))
        
        message = input("Enter a message (number) to encrypt, or 0 to exit: ")


main()
