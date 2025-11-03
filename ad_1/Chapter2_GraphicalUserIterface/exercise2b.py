# we are asked to create a square grid using pack inside frames,
# the left frame contains a (top) and b (bottom)
# the right frame contains c (top) and d (bottom)

import tkinter as tk

root = tk.Tk()
root.title("square grid with pack")
root.geometry("600x300")
root.configure(bg="#ffffff")

# make the container frame to hold two frames side by side
container = tk.Frame(root, bg="#ffffff")
container.pack(fill="both", expand=True, padx=10, pady=10)

# the left frame with border (5)
left = tk.Frame(container, bd=5, relief="ridge")
left.pack(side="left", fill="both", expand=True, padx=5, pady=5)

# the right frame with border (5)
right = tk.Frame(container, bd=5, relief="ridge")
right.pack(side="left", fill="both", expand=True, padx=5, pady=5)

# a should be at top of left frame as displayed in the pic
a = tk.Label(left, text="a", bg="#2f3640", fg="white")
a.pack(side="top", fill="both", expand=True)

# b would be at bottom of left frame
b = tk.Label(left, text="b", bg="white", fg="#2f3640")
b.pack(side="bottom", fill="both", expand=True)

# c would be at top of right frame
c = tk.Label(right, text="c", bg="white", fg="#2f3640")
c.pack(side="top", fill="both", expand=True)

# d should be at bottom of right frame
d = tk.Label(right, text="d", bg="#2f3640", fg="white")
d.pack(side="bottom", fill="both", expand=True)

root.mainloop()
