# in ex 3 we are asked to create a login page using grid geometry manager

import tkinter as tk

root = tk.Tk()
root.title("login page")
root.geometry("350x180")
root.configure(padx=10, pady=10)

# create the username label and entry
tk.Label(root, text="username:").grid(row=0, column=0, sticky="e", pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, pady=5)

# now the password label and entry
tk.Label(root, text="password:").grid(row=1, column=0, sticky="e", pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, pady=5)

# create the login button function
def login():
    # get values from entries
    user = username_entry.get()
    pwd = password_entry.get()
    # here is a simple way of doing it, so i made the user/username which is ( admin ) and the password is just ( 12345 )
    if user == "admin" and pwd == "12345":
        tk.messagebox.showinfo("login", "login successful")
    else:
        tk.messagebox.showerror("login", "invalid credentials")

# import the messagebox only when needed to avoid the warning
from tkinter import messagebox

# creating the login button which is under the entry area, creates two columns
tk.Button(root, text="login", command=login).grid(row=2, column=0, columnspan=2, pady=10)

#run the program
root.mainloop()
