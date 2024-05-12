import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            tkinter.messagebox.showinfo("Error", "Syntax Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "BS":
        entry.delete(len(entry.get()) - 1, tk.END)
    else:
        entry.insert(tk.END, text)

def myclick(number):
    entry.insert(tk.END, number)

window = tk.Tk()
window.title('Calculator')
frame = tk.Frame(master=window, bg="skyblue", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

buttons = [
    "C", "=", "%", "7", "8", "9",
    "-", "+", "*", "4", "5", "6",
    ".", "/", "0", "1", "2", "3", "BS",
    "00", "(", ")", "[", "]"
]

def pack_buttons(buttons, frame):
    for symbol in buttons:
        b = tk.Button(frame, text=symbol, padx=15, pady=5, width=3)
        b.pack(side=tk.LEFT, padx=5, pady=2)
        b.bind("<Button-1>", click)
    frame.pack()

rows = [buttons[i:i+6] for i in range(0, len(buttons), 6)]

for row in rows:
    f = tk.Frame(window, bg="skyblue")
    pack_buttons(row, f)

window.mainloop()
