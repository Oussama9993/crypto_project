from RSA.RSA_enc import *
from RSA.RSA_dec import *
while True:
    print("===========================================================================================================")
    print("1: encrypt\n2:decrypt\n3:exit")
    state = int(input("enter your choice :"))
    if state == 1:
        print("===========================================================================================================")
        print("============================================ RSA Encryptor  ==============================================")
        print(" ")
        key_message = str(input(" - Enter a message key "))
        print(" - Generating your public key-pairs now . . .")
        public_key = generate_public_key(key_message)
        print(" - Your public key is ", public_key)
        message = input(" - Enter a message to encrypt with your public key: ")
        encrypted_msg = encrypt_rsa(public_key, message)
        print(" - Your encrypted message is: ", encrypted_msg)

        print("============================================ END ==========================================================")
        print("===========================================================================================================")

    elif state == 2:
        print(
            "===========================================================================================================")
        print("================================== RSA Decrypter ==============================================")
        print(" ")

        key_message = str(input(" - Enter a message "))

        print(" - Generating your public / private key-pairs now . . .")

        public, private = generate_key_pair(key_message)

        print(" - Your public key is ", public, " and your private key is ", private)
        message = input(" - Enter a message to decrypt with your public key: ")
        print(" - Decrypting message with private key ", private, " . . .")
        print(" - Your message is: ", decrypt_rsa(private, message))

        print(" ")
        print("============================================ END "
              "==========================================================")

    elif state == 3:
        break
    else :
        print("error, choose again")
