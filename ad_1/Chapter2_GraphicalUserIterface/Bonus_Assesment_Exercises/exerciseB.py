# so we are asked to create a age calculator
# expected dob format: day/month/year e.g. 8/5/2018

import tkinter as tk              
from datetime import date         # import the class to work with the date and time

# firstly create the main window
root = tk.Tk()
root.title("age calculator")      # set window title
root.geometry("350x140")          # set the window size
root.configure(padx=10, pady=10)  # add some space inside the window

# creating the label and entry for user to enter date of birth
tk.Label(root, text="enter date of birth (d/m/y)").pack()
dob_entry = tk.Entry(root)
dob_entry.pack()

# here's the variable to store and display result
result_var = tk.StringVar(value="")
tk.Label(root, textvariable=result_var).pack(pady=5)

# now make the function to calculate age 
def calc_age():
    s = dob_entry.get().strip()  # get user input and remove extra spaces
    try:
        # split input by '/' and convert for day, month, year
        d, m, y = map(int, s.split("/"))
        # create a date object for the entered date of birth
        dob = date(y, m, d)
        # get today's date
        today = date.today()
        # calculate age in years (subtract 1 if birthday hasn't occurred yet this year)
        years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        # display the calculated age
        result_var.set(f"your age is {years} years")
    except Exception:
        # handle invalid input formats
        result_var.set("please enter dob as d/m/y")

# now creating the button to trigger age calculation
tk.Button(root, text="calculate age", command=calc_age).pack(pady=5)

#run the program
root.mainloop()
