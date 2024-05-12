from tkinter import *
import pyperclip 
import random

root = Tk()
root.title("Password Generator")
root.geometry("700x300")
root.configure(bg="#CBC3E3")  # Set background color to light purple

passwrd = StringVar()
passlen = IntVar()
passlen.set(0)

def low():
    length = passlen.get()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    if var.get() == 1:
        for _ in range(length):
            password += random.choice(lower)
    elif var.get() == 0:
        for _ in range(length):
            password += random.choice(upper)
    elif var.get() == 3:
        for _ in range(length):
            password += random.choice(digits)
    else:
        print("Please choose an option")
    passwrd.set(password)

def generate(): 
    low()

def copyclipboard():
    random_password = passwrd.get()
    pyperclip.copy(random_password)

# Labels
Label(root, text="Strong Password Generator", font="Courier 30 bold", bg="#CBC3E3").pack()
Label(root, text="Enter the number to get password", bg="#CBC3E3").pack(pady=3)
Entry(root, textvariable=passlen).pack(pady=3)

# Radio Buttons for deciding the strength of password
var = IntVar()
radio_low = Radiobutton(root, text="Low", variable=var, value=1, bg="#CBC3E3")
radio_low.pack()
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0, bg="#CBC3E3")
radio_middle.pack()
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3, bg="#CBC3E3")
radio_strong.pack()

Button(root, text="Tap to get", command=generate).pack(pady=7)
Entry(root, textvariable=passwrd).pack(pady=3)
Button(root, text="Tap to copy clipboard", command=copyclipboard).pack()
root.mainloop()
