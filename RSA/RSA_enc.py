import random
import string
from RSA.common_func import gcd
from RSA.common_func import convert
# state = input("encrypt or decrypt ?:")
print("welcome")

'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def generate_public_key(key):
    q, p = convert(key)
    # n = pq
    n = p * q

    # Phi is the totient of n
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = 3

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e += 1
        g = gcd(e, phi)

    # Return public and private key_pair
    # Public key is (e, n) and private key is (d, n)
    return e, n


def encrypt_rsa(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [pow(ord(char), key, n) for char in plaintext]
    # Return the array of bytes
    en_msg = to_string(cipher)
    return en_msg


def random_ch():
    ch = random.choice(string.ascii_lowercase + string.ascii_uppercase)
    return ch


def to_string(arr):
    text = ""
    for i in range(len(arr)):
        text += str(arr[i]) + random.choice(string.ascii_lowercase + string.ascii_uppercase)
    return text


'''
if __name__ == '__main__':
    
    #Detect if the script is being run directly by the user
    
    print("===========================================================================================================")
    print("============================================ RSA Encryptor  ==============================================")
    print(" ")

    key_message = str(input(" - Enter a message key "))

    print(" - Generating your public key-pairs now . . .")

    public_key = generate_public_key(key_message)

    print(" - Your public key is ", public_key)

    message = input(" - Enter a message to encrypt with your public key: ")
    encrypted_msg = encrypt(public_key, message)

    #    print(" - Your encrypted message is: ", ''.join(map(lambda x: str(x), encrypted_msg)))
    print(" - Your encrypted message is: ", encrypted_msg)

    print("============================================ END ==========================================================")
    print("===========================================================================================================")
'''