from tkinter import *
from tkinter import messagebox

tasks_list = []
enter_task_field = None
TextArea = None
task_number_entry = None

def check_input_error():
    if enter_task_field.get() == "":
        messagebox.showerror("Input Error", "Task field cannot be empty")
        return False
    return True
 
def clear_task_field():
    enter_task_field.delete(0, END)

def insert_task():
    if not check_input_error():
        return
    content = enter_task_field.get() + "\n"
    tasks_list.append(content)
    TextArea.insert(END, content)
    clear_task_field()

def delete_task():
    try:
        task_no = int(task_number_entry.get())
        if 1 <= task_no <= len(tasks_list):
            del tasks_list[task_no - 1]
            update_text_area()
        else:
            messagebox.showerror("Input Error", "Task number out of range")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid task number")

def update_text_area():
    TextArea.delete(1.0, END)
    for i, task in enumerate(tasks_list, start=1):
        TextArea.insert(END, "[{}] {}\n".format(i, task))

def load_main_window():
    global enter_task_field, TextArea, task_number_entry
    gui = Tk()
    gui.configure(background="Purple")
    gui.title("ToDo App")
    gui.geometry("400x400")

    enter_task_label = Label(gui, text="Enter Your Task", bg="light green", fg="#234F1E")
    enter_task_field = Entry(gui)
    submit_button = Button(gui, text="Submit", fg="Black", bg="Red", command=insert_task)

    scrollbar = Scrollbar(gui)
    global TextArea
    TextArea = Text(gui, height=10, width=30, font="lucida 13", yscrollcommand=scrollbar.set)

    delete_label = Label(gui, text="Delete Task Number", bg="blue")
    global task_number_entry
    task_number_entry = Entry(gui)
    delete_button = Button(gui, text="Delete", fg="Black", bg="Red", command=delete_task)

    enter_task_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
    enter_task_field.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    submit_button.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    TextArea.grid(row=3, column=0, padx=5, pady=5, sticky=W+E, columnspan=2)
    scrollbar.grid(row=3, column=2, padx=5, pady=5, sticky=N+S)
    scrollbar.config(command=TextArea.yview)

    delete_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)
    task_number_entry.grid(row=5, column=0, padx=5, pady=5, sticky=W)
    delete_button.grid(row=5, column=1, padx=5, pady=5, sticky=W)

    # Changing message box color
    gui.tk_setPalette(background='#3944BC', foreground='white', activeBackground='#3944BC', activeForeground='white')

    gui.mainloop()

load_main_window()
