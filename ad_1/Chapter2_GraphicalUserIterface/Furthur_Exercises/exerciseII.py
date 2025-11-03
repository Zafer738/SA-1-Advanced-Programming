# this is an additional exercise, the user should be able to capitalize letters (change to upper case), like capitalize the letters

import tkinter as tk

root = tk.Tk()
root.title("capitalize letters")
root.geometry("420x180")
root.configure(padx=10, pady=10)

tk.Label(root, text="enter text").pack()
text_entry = tk.Entry(root, width=50)
text_entry.pack()

result_var = tk.StringVar(value="")
tk.Label(root, textvariable=result_var).pack(pady=5)

def to_upper():
    s = text_entry.get()
    result_var.set(s.upper())

tk.Button(root, text="convert to upper", command=to_upper).pack(pady=5)

root.mainloop()
