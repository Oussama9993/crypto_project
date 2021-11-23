from RSA.common_func import gcd
from RSA.common_func import convert

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


def generate_key_pair(key):
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

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private key_pair
    # Public key is (e, n) and private key is (d, n)
    return (e, n), (d, n)


def to_array(text):
    arr = []
    i = 0
    while i < len(text):
        j = i
        temp = ""
        while text[j].isdigit():
            temp += text[j]
            j += 1
        i = j + 1
        arr.append(int(temp))

    return arr


def decrypt_rsa(pk, ciphertext):
    ciphertext = to_array(ciphertext)
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    aux = [str(pow(int(char), key, n)) for char in ciphertext]
    # Return the array of bytes as a string
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)


'''
if __name__ == '__main__':
    
    #Detect if the script is being run directly by the user
    
    print("===========================================================================================================")
    print("================================== RSA Decrypter ==============================================")
    print(" ")

    key_message = str(input(" - Enter a message "))

    print(" - Generating your public / private key-pairs now . . .")

    public, private = generate_key_pair(key_message)

    print(" - Your public key is ", public, " and your private key is ", private)

    message = input(" - Enter a message to decrypt with your public key: ")

    print(" - Decrypting message with private key ", private, " . . .")
    print(" - Your message is: ", decrypt(private, message))

    print(" ")
    print("============================================ END ==========================================================")
    print("===========================================================================================================")
'''
