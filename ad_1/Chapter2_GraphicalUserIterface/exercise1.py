# so we are asked to create a window with a "welcome" label


import tkinter as tk            
from tkinter import font        # import for changing fonts

# creating the main  window
root = tk.Tk()                  
root.title("welcome")           # the window title
root.geometry("400x150")        # set the size
root.resizable(False, False)    # disable resizing 
root.configure(bg="#dfe6e9")    # set bg colour

# create an object for the label (font name, size, weight)
welcome_font = font.Font(family="helvetica", size=20, weight="bold")

#then make the label widget to display the welcome message
label = tk.Label(root,               # parent widget
                 text="welcome to tkinter!",  # text which is shown 
                 font=welcome_font,    # apply the font that we created
                 bg="#dfe6e9")         # window background


label.pack(expand=True)             


root.mainloop()
