# this is an furthr exercise, asks to count characters (vowels, consonants, special characters) in a sentence

import tkinter as tk

root = tk.Tk()
root.title("count characters")
root.geometry("420x200")
root.configure(padx=10, pady=10)

tk.Label(root, text="enter text").pack()
text_entry = tk.Entry(root, width=50)
text_entry.pack()

result_var = tk.StringVar(value="")
tk.Label(root, textvariable=result_var).pack(pady=5)

def count():
    s = text_entry.get()
    total = len(s)
    vowels = sum(1 for ch in s.lower() if ch in "aeiou")
    consonants = sum(1 for ch in s.lower() if ch.isalpha() and ch not in "aeiou")
    special = total - vowels - consonants
    result_var.set(f"total letters: {total} | vowels: {vowels} | consonants: {consonants} | special: {special}")

tk.Button(root, text="count", command=count).pack(pady=5)

root.mainloop()
