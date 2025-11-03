# this program shows how to arrange 4 labels using pack()
# and how they change when the window is resized

import tkinter as tk

# first creating the main window
root = tk.Tk()
root.title("gui pack example")
root.geometry("600x300")
root.configure(bg="#e8e8e8")  # set bg color for the window

# create label ( A )  the red bar across the top
label_a = tk.Label(
    root,
    text="A",
    bg="red",
    fg="white",
    bd=5,                   #the border width
    relief="raised"         
)
# pack it to the top 
label_a.pack(fill="x", padx=5, pady=5)

# create label c the (blue) one
label_c = tk.Label(
    root,
    text="C",
    bg="blue",
    fg="white",
    width=10,
    bd=5,
    relief="groove"
)
label_c.pack(side="left", padx=10, pady=10)

# create label b the (yellow) one
label_b = tk.Label(
    root,
    text="B",
    bg="yellow",
    fg="black",
    width=10,
    bd=5,
    relief="groove"
)
label_b.pack(side="left", padx=10, pady=10)

# create label d the (white) one
label_d = tk.Label(
    root,
    text="D",
    bg="white",
    fg="black",
    width=10,
    bd=5,
    relief="groove"
)
label_d.pack(side="left", padx=10, pady=10)

# run it
root.mainloop()
