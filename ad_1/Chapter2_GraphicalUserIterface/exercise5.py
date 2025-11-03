# we are asked to create a simple calculator in this using tk
# it allows addition, subtraction, multiplication, division and modulo

import tkinter as tk

root = tk.Tk()
root.title("calculator")
root.geometry("300x220")
root.configure(padx=10, pady=10)

# first making the entry fields for two numbers
tk.Label(root, text="value 1").pack()
e1 = tk.Entry(root)
e1.pack()

tk.Label(root, text="value 2").pack()
e2 = tk.Entry(root)
e2.pack()

# now this is where the results shall appear
result_var = tk.StringVar(value="result will appear here")
tk.Label(root, textvariable=result_var).pack(pady=5)

# now creating the operation functions
def get_numbers():
    #convert the input to float, then return the tuple or if nothing is entered then it shows an error
    try:
        a = float(e1.get())
        b = float(e2.get())
        return a, b
    except ValueError:
        result_var.set("please enter valid numbers")
        return None, None


def add():
    # calls the get_numbers() function to retrieve the two input numbers
    a, b = get_numbers()

    # if a is None, it means there was an error in getting input (for example invalid entry)
    if a is None:
        return

    # calculate the sum and show it in the result label by updating result_var
    result_var.set(str(a + b))


def subtract():
    # get the two numbers entered by the user
    a, b = get_numbers()

    # check for invalid input
    if a is None:
        return

    # subtract the second number from the first and update the result label
    result_var.set(str(a - b))


def multiply():
    # gets the two numbers entered by the user
    a, b = get_numbers()

    # if input is invalid, stop the function
    if a is None:
        return

    # multiply the numbers and display the result
    result_var.set(str(a * b))


def divide():
    # get the numbers to divide
    a, b = get_numbers()

    # check for invalid input
    if a is None:
        return

    # if the second number is zero, show an error instead of dividing
    if b == 0:
        result_var.set("cannot divide by zero")
    else:
        # divide normally and display the result
        result_var.set(str(a / b))


def modulo():
    # get the numbers from the user input
    a, b = get_numbers()

    # check for invalid input
    if a is None:
        return

    # try to calculate the remainder of a divided by b
    try:
        result_var.set(str(a % b))
    except Exception:
        # to handle if there is any error
        result_var.set("error in modulo operation")


# so these buttons are created for operations, depending on what the user choses it will run...
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="+", width=4, command=add).grid(row=0, column=0, padx=3)
tk.Button(btn_frame, text="-", width=4, command=subtract).grid(row=0, column=1, padx=3)
tk.Button(btn_frame, text="*", width=4, command=multiply).grid(row=0, column=2, padx=3)
tk.Button(btn_frame, text="/", width=4, command=divide).grid(row=0, column=3, padx=3)
tk.Button(btn_frame, text="%", width=4, command=modulo).grid(row=0, column=4, padx=3)

#run the program
root.mainloop()
