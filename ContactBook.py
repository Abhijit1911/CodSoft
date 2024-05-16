import tkinter as tk
from tkinter import Scrollbar

contactlist = []

class ContactBookApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Book")
        self.contacts = contactlist

        self.layout = tk.Frame(self, bg="lavender", padx=20, pady=20)
        self.layout.pack()

        self.name_label = tk.Label(self.layout, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_input = tk.Entry(self.layout)
        self.name_input.grid(row=0, column=1, padx=10, pady=10)

        self.number_label = tk.Label(self.layout, text="Contact No.:")
        self.number_label.grid(row=1, column=0, padx=10, pady=10)
        self.number_input = tk.Entry(self.layout)
        self.number_input.grid(row=1, column=1, padx=10, pady=10)

        self.add_button = tk.Button(self.layout, text="ADD", command=self.add_contact)
        self.add_button.grid(row=2, column=0, padx=10, pady=10)
        self.edit_button = tk.Button(self.layout, text="EDIT", command=self.edit_contact)
        self.edit_button.grid(row=2, column=1, padx=10, pady=10)
        self.delete_button = tk.Button(self.layout, text="DELETE", command=self.delete_contact)
        self.delete_button.grid(row=2, column=2, padx=10, pady=10)

        self.saved_contacts = tk.Listbox(self.layout, height=10, width=40)
        self.saved_contacts.grid(row=3, columnspan=3, padx=10, pady=10)
        self.scrollbar = Scrollbar(self.layout, orient="vertical")
        self.scrollbar.config(command=self.saved_contacts.yview)
        self.scrollbar.grid(row=3, column=4, sticky="ns")
        self.saved_contacts.config(yscrollcommand=self.scrollbar.set)
        self.saved_contacts.bind('<<ListboxSelect>>', self.on_contact_select)

    def add_contact(self):
        name = self.name_input.get()
        number = self.number_input.get()

        if name and number:
            self.contacts.append([name, number])
            self.update_saved_contacts()
            self.name_input.delete(0, tk.END)
            self.number_input.delete(0, tk.END)
            self.show_popup("Confirmation", "Successfully added new contact")
        else:
            self.show_popup("Error", "Please fill in both the name and number")

    def edit_contact(self):
        selected_index = self.saved_contacts.curselection()
        if selected_index:
            index = selected_index[0]
            name = self.name_input.get()
            number = self.number_input.get()
            if name and number:
                self.contacts[index] = [name, number]
                self.update_saved_contacts()
                self.name_input.delete(0, tk.END)
                self.number_input.delete(0, tk.END)
                self.show_popup("Confirmation", "Successfully updated contact")
            else:
                self.show_popup("Error", "Please fill in both the name and number")
        else:
            self.show_popup("Error", "Please select a contact to edit")

    def delete_contact(self):
        selected_index = self.saved_contacts.curselection()
        if selected_index:
            index = selected_index[0]
            del self.contacts[index]
            self.update_saved_contacts()
            self.show_popup("Confirmation", "Successfully deleted contact")
        else:
            self.show_popup("Error", "Please select a contact to delete")

    def update_saved_contacts(self):
        self.saved_contacts.delete(0, tk.END)
        for contact in self.contacts:
            self.saved_contacts.insert(tk.END, f"{contact[0]} - {contact[1]}")

    def on_contact_select(self, event):
        index = self.saved_contacts.curselection()[0]
        contact = self.contacts[index]
        self.name_input.delete(0, tk.END)
        self.name_input.insert(tk.END, contact[0])
        self.number_input.delete(0, tk.END)
        self.number_input.insert(tk.END, contact[1])

    def show_popup(self, title, message):
        popup = tk.Toplevel()
        popup.title(title)
        popup.geometry("300x200")
        popup_label = tk.Label(popup, text=message)
        popup_label.pack(pady=20)
        ok_button = tk.Button(popup, text="OK", command=popup.destroy)
        ok_button.pack(pady=10)

app = ContactBookApp()
app.mainloop()
