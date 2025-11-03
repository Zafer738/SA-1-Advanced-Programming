
# so we are asked to create a simple vending machine gui that allows user to choose the  product, insert money/the amount and get change

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('vending machine')
root.geometry('420x260')
root.configure(padx=10, pady=10)

# create the price dictionary, and the prodcuts
products = {'soda': 1.5, 'chips': 1.0, 'chocolate': 1.25}
prod_var = tk.StringVar(value='soda')  # selected product
amount_var = tk.DoubleVar(value=0.0)   # amount inserted by user

# here is the product selection label and the menu area
tk.Label(root, text='product:').grid(row=0, column=0, sticky='w')
prod_menu = tk.OptionMenu(root, prod_var, *products.keys())
prod_menu.grid(row=0, column=1, sticky='w')

# this is where the user can input amounts, the entry widgets
tk.Label(root, text='amount inserted:').grid(row=1, column=0, sticky='w')
amount_entry = tk.Entry(root, textvariable=amount_var)
amount_entry.grid(row=1, column=1, sticky='w')

# create this function to run the vending machine operation and gives feedback depending on what the user picked
def vend():
    try:
        paid = float(amount_var.get())  # the entered amount
    except Exception:
        messagebox.showerror('error', 'enter a numeric amount')
        return
    price = products[prod_var.get()]  # gets price of selected product
    if paid < price:
        # incase th user enters less, shows an insufficient payment warning
        messagebox.showwarning('insufficient', f'inserted {paid:.2f}, price is {price:.2f}')
    else:
        # but if the suer enters correct amount it shows that its a successful purchase, then calculates change and confirms purchase
        change = paid - price
        messagebox.showinfo('thank you', f'enjoy your {prod_var.get()}! change: {change:.2f}')

#this 'buy' button basically runs the program aftet the use rhas selected ther choices
tk.Button(root, text='buy', command=vend).grid(row=2, column=0, columnspan=2, pady=10)

#run the program
root.mainloop()
