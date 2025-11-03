
#  so we are asked to create a program that converts temperature between celsius and fahrenheit in tkinter

import tkinter as tk  

#firstly make the main window
root = tk.Tk()
root.title("temperature converter")      # the window title
root.geometry("350x150")                 # the window size
root.configure(padx=10, pady=10)         # add padding 

# create a label and entry field for user to input temperature
tk.Label(root, text="enter temperature").pack()
temp_entry = tk.Entry(root)
temp_entry.pack()

# variable to store which conversion mode the user selects (e.g: celsius to fahrenheit or the other way around)
mode_var = tk.StringVar(value="c2f")

# two radio buttons to choose the conversion direction
tk.Radiobutton(root, text="c -> f", variable=mode_var, value="c2f").pack(anchor="w")
tk.Radiobutton(root, text="f -> c", variable=mode_var, value="f2c").pack(anchor="w")

# label to show the conversion result
result_var = tk.StringVar(value="result")
tk.Label(root, textvariable=result_var).pack(pady=5)

# function that performs the conversion when the button is clicked
def convert():
    try:
        # try to get the number entered by the user
        t = float(temp_entry.get())
    except ValueError:
        # if input is not a number, show an error message
        result_var.set("enter a number")
        return

    # if user chose celsius to fahrenheit
    if mode_var.get() == "c2f":
        res = (t * 9/5) + 32
        result_var.set(f"{res:.2f} f")  # show the result rounded to 2 decimals
    else:
        # if user chose fahrenheit to celsius
        res = (t - 32) * 5/9
        result_var.set(f"{res:.2f} c")

# then finally create button to start the conversion
tk.Button(root, text="convert", command=convert).pack(pady=5)

#run the program
root.mainloop()
