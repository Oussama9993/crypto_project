import cv2
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from RSA.RSA_dec import decrypt_rsa,generate_key_pair
from DES.DES_dec import des_dec_exec
from DES.common_func import hex2char,char2hex

image_display_size = 500, 350

def decrypter(key,message):
    # decrypt with rsa
    public, private = generate_key_pair(key)
    decrypted_rsa = decrypt_rsa(private, message)
    print("your decrypted message with rsa is: ", decrypted_rsa)
    decrypted_rsa_hex = char2hex(decrypted_rsa)
    print("your decrypted message with rsa is hex: ", decrypted_rsa_hex)
    # decrypt with des
    decrypted_msg = des_dec_exec(decrypted_rsa_hex, key)

    print(" - Your decrypted message is hex: ", decrypted_msg)
    print(" - Your decrypted message is: ", hex2char(decrypted_msg))
    return hex2char(decrypted_msg)


def decrypt():
    # load the image and convert it into a numpy array and display on the GUI.
    load = Image.open("./encrypted_image.png")
    load.thumbnail(image_display_size, Image.ANTIALIAS)
    load = np.asarray(load)
    load = Image.fromarray(np.uint8(load))
    render = ImageTk.PhotoImage(load)
    img = Label(app, image=render)
    img.image = render
    img.place(x=100, y=50)

    # Algorithm to decrypt the data from the image
    img = cv2.imread("./encrypted_image.png")
    data = []
    stop = False
    for index_i, i in enumerate(img):
        i.tolist()
        for index_j, j in enumerate(i):
            if((index_j) % 3 == 2):
                # first pixel
                data.append(bin(j[0])[-1])
                # second pixel
                data.append(bin(j[1])[-1])
                # third pixel
                if(bin(j[2])[-1] == '1'):
                    stop = True
                    break
            else:
                # first pixel
                data.append(bin(j[0])[-1])
                # second pixel
                data.append(bin(j[1])[-1])
                # third pixel
                data.append(bin(j[2])[-1])
        if(stop):
            break

    message = []
    # join all the bits to form letters (ASCII Representation)
    for i in range(int((len(data)+1)/8)):
        message.append(data[i*8:(i*8+8)])
    # join all the letters to form the message.
    message = [chr(int(''.join(i), 2)) for i in message]
    message = ''.join(message) 
    data_key = txt.get(1.0, "end-1c")
    message=decrypter(data_key, message)
    message_label = Label(app, text=message, bg='lavender', font=("Times New Roman", 10))
    message_label.place(x=30, y=400)

# Defined the TKinter object app with background lavender, title Decrypt, and app size 600*600 pixels.
app = Tk()
app.configure(background='lavender')
app.title("Decrypt")
app.geometry('600x600')
# Add the button to call the function decrypt.
main_button = Button(app, text="Start Program", bg='white', fg='black', command=decrypt)
main_button.place(x=250, y=10)
txt = Text(app, wrap=WORD, width=30)
txt.place(x=340, y=55, height=165)
app.mainloop()
