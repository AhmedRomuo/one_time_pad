from tkinter import *

x_window = Tk()
output_text = StringVar()
check_space = IntVar()
txt_plain_text = Entry(x_window, width=35, font=10)
txt_key = Entry(x_window, width=20, font=10)


def xor(ch1, ch2):
    ch1 = "" + bin(ord(ch1))[2:].zfill(7)
    ch2 = "" + bin(ord(ch2))[2:].zfill(7)
    out = ""

    for index in range(len(ch1)):
        if ch1[index] == ch2[index]:
            out += '0'
        else:
            out += '1'

    return int(out, 2)


def encryption(text, key):
    plain_txt = text.replace(" ", "")
    key_txt = key.replace(" ", "")
    cipher_txt = ""

    for index in range(len(plain_txt) - len(key_txt)):
        key_txt += key_txt[index % len(key_txt)]

    print(plain_txt)
    print(key_txt)

    for index in range(len(plain_txt)):
        cipher_txt += chr(xor(plain_txt[index], key_txt[index]))
        print(xor(text[index], key_txt[index]))

    output_text.set("Cipher text : " + cipher_txt.upper())
    print("Cipher text : " + cipher_txt.upper())


def decryption(text, key):
    key_txt = key.replace(" ", "")
    plain_txt = ""

    for index in range(len(text) - len(key_txt)):
        key_txt += key_txt[index % len(key_txt)]

    for index in range(len(text)):
        plain_txt += chr(xor(text[index], key_txt[index]))
        print(xor(text[index], key_txt[index]))

    output_text.set("Plain text : " + plain_txt.upper())
    print("Plain text : " + plain_txt.lower().upper())


def click_btn1():
    encryption(str(txt_plain_text.get()).upper(), str(txt_key.get()).upper())


def click_btn2():
    decryption(str(txt_plain_text.get()).upper(), str(txt_key.get()).upper())


def main():
    # frame window
    x_window.configure(background="black")
    x_window.title("One Time Pad")
    x_window.geometry("500x300")

    # labels
    lbl_txt1 = Label(x_window, text="Text : ", padx=5, pady=5, bg="black", fg="white")
    lbl_txt2 = Label(x_window, textvariable=output_text, padx=5, pady=5, font=10, bg="black", fg="white")
    lbl_key = Label(x_window, text="Key : ", padx=5, pady=5, bg="black", fg="white")
    lbl_txt1.place(x=10, y=10)
    lbl_key.place(x=10, y=50)

    # text
    txt_plain_text.focus()
    txt_plain_text.place(x=60, y=15)
    txt_key.place(x=60, y=55)

    # Button and check button
    btn_encrypt = Button(x_window, text="Encrypt", padx=5, pady=5, command=click_btn1, bg="gray", fg="white",
                         activebackground="black", activeforeground="white")
    btn_decrypt = Button(x_window, text="Decrypt", padx=5, pady=5, command=click_btn2, bg="gray", fg="white",
                         activebackground="black", activeforeground="white")

    btn_encrypt.place(x=100, y=110)
    btn_decrypt.place(x=250, y=110)

    lbl_txt2.place(x=60, y=160)
    x_window.mainloop()


if __name__ == '__main__': main()
