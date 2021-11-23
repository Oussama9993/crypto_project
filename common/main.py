from RSA.RSA_dec import generate_key_pair, decrypt_rsa
from RSA.RSA_enc import generate_public_key, encrypt_rsa
from DES.DES_enc import des_enc_exec
from DES.DES_dec import des_dec_exec
from DES.common_func import hex2char, char2hex

state = int(input("enter 1:enc\n2:dec"))
if state == 1:
    #key_message = str(input(" - Enter your key "))
    key_message = "key navas"
    message = input(" - Enter a message to encrypt")
    # encrypt with des
    encrypted_des_hex = des_enc_exec(message, key_message)
    print("your encrypted message with des is: ", encrypted_des_hex)
    encrypted_des = hex2char(encrypted_des_hex)
    # encrypt with rsa
    public_key = generate_public_key(key_message)
    encrypted_msg = encrypt_rsa(public_key, encrypted_des)
    print(" - Your encrypted message is: ", encrypted_msg)
elif state == 2:
    #key_message = str(input(" - Enter your key "))
    key_message = "key navas"
    message = input(" - Enter a cipher message to decrypt")
    # decrypt with rsa
    public, private = generate_key_pair(key_message)
    decrypted_rsa = decrypt_rsa(private, message)
    print("your decrypted message with rsa is: ", decrypted_rsa)
    decrypted_rsa_hex = char2hex(decrypted_rsa)
    print("your decrypted message with rsa is hex: ", decrypted_rsa_hex)
    # decrypt with des
    decrypted_msg = des_dec_exec(decrypted_rsa_hex, key_message)

    print(" - Your decrypted message is hex: ", decrypted_msg)
    print(" - Your decrypted message is: ", hex2char(decrypted_msg))
