# so we are asked to create a burger shack type of thing which allows the user to order
# it lets the user choose the burger type, toppings, condiments, sides, calculating total, and processing payment.


import tkinter as tk                      
from tkinter import ttk                   # import the  widgets 
from tkinter import messagebox            # import messagebox for popup dialogs

# creat the main window
root = tk.Tk()                            
root.title('burger shack - order')        # set the text that shows in title, at the top
root.geometry('520x420')                  # set the window size
root.configure(padx=10, pady=10)          # add padding 

# make price dictionaries to give a base price for each category item
# keys are item names (strings) and values are prices (floats)
burger_prices = {'beef': 6.50, 'chicken': 5.50, 'vegetarian': 5.00}
topping_prices = {'cheese': 0.75, 'peanut butter': 0.90, 'avocado': 1.25}
condiment_prices = {'ketchup': 0.10, 'mayonnaise': 0.15, 'bbq sauce': 0.20}
sides_prices = {'fries': 2.0, 'drink': 1.5}

# variables that contains the user selections/options
# tkinter variable classes (StringVar, BooleanVar, DoubleVar, IntVar) allow widgets and code to share state
burger_var = tk.StringVar(value='beef')   # stores which burger type is selected; default is 'beef'
# for toppings/condiments/sides we create boolean variables keyed by item name
toppings_vars = {k: tk.BooleanVar(value=False) for k in topping_prices}
cond_vars = {k: tk.BooleanVar(value=False) for k in condiment_prices}
side_vars = {k: tk.BooleanVar(value=False) for k in sides_prices}

# layout frame: a container to hold the form elements
frame = tk.Frame(root)                     # create a frame inside the root window to organize widgets
frame.pack(fill='both', expand=True)       # pack the frame to fill available space and allow it to expand

# burger selection combobox (drop-down)
tk.Label(frame, text='choose burger:').grid(row=0, column=0, sticky='w')
# ttk.Combobox shows a dropdown list; state='readonly' prevents typing arbitrary text into it
burger_menu = ttk.Combobox(
    frame,
    textvariable=burger_var,
    values=list(burger_prices.keys()),
    state='readonly'
)
burger_menu.grid(row=0, column=1, padx=6, pady=6)  # place the combobox next to its label

# toppings checkbuttons (each toggles a booleanvar stored in toppings_vars)
tk.Label(frame, text='toppings:').grid(row=1, column=0, sticky='nw')  # label aligned to top-left of its cell
top_frame = tk.Frame(frame)                 # create a small sub-frame to stack checkbuttons for toppings
top_frame.grid(row=1, column=1, sticky='w') # place the sub-frame to the right of the toppings label
# iterate over topping_prices keys to create a checkbutton per topping
for i, name in enumerate(topping_prices):
    # text uses an f-string to include the topping name and its price formatted to two decimals
    cb_text = f"{name} (+{topping_prices[name]:.2f})"
    cb = tk.Checkbutton(top_frame, text=cb_text, variable=toppings_vars[name])
    cb.grid(row=i, column=0, sticky='w')   # place each checkbox on its own row inside top_frame

# editing the checkbuttons
tk.Label(frame, text='condiments:').grid(row=2, column=0, sticky='nw')
cond_frame = tk.Frame(frame)
cond_frame.grid(row=2, column=1, sticky='w')
for i, name in enumerate(condiment_prices):
    cb_text = f"{name} (+{condiment_prices[name]:.2f})"
    cb = tk.Checkbutton(cond_frame, text=cb_text, variable=cond_vars[name])
    cb.grid(row=i, column=0, sticky='w')

# sides checkbuttons
tk.Label(frame, text='sides:').grid(row=3, column=0, sticky='nw')
side_frame = tk.Frame(frame)
side_frame.grid(row=3, column=1, sticky='w')
for i, name in enumerate(sides_prices):
    cb_text = f"{name} (+{sides_prices[name]:.2f})"
    cb = tk.Checkbutton(side_frame, text=cb_text, variable=side_vars[name])
    cb.grid(row=i, column=0, sticky='w')

# the calculate_total function sums the base burger price and any selected add-ons
def calculate_total():

    total = 0.0
    # add the base price of the currently selected burger; .get() returns the string value
    total += burger_prices.get(burger_var.get(), 0.0)
    # add topping prices for those that are selected (booleanvar is True)
    for name, var in toppings_vars.items():
        if var.get():                     # var.get() returns True if the checkbox is checked
            total += topping_prices[name]
    # add condiment prices
    for name, var in cond_vars.items():
        if var.get():
            total += condiment_prices[name]
    # add sides prices
    for name, var in side_vars.items():
        if var.get():
            total += sides_prices[name]
    return total

# ui to show total: a stringvar keeps the displayed text in sync with the calculated value
total_var = tk.StringVar(value='0.00')     # initialize with '0.00' so user sees a currency-like value immediately

def update_total_label():
    """
    read the calculated total and write it into total_var formatted with two decimals.
    formatting to two decimals is common for representing currency values.
    """
    total = calculate_total()               # call helper to calcualte the total
    
    total_var.set(f"{total:.2f}")

# button to update the total display; user can press it after changing selections
tk.Button(frame, text='update total', command=update_total_label).grid(row=4, column=0, pady=10)
# label to show the word 'total:' next to the numeric total
tk.Label(frame, text='total:').grid(row=4, column=1, sticky='w')
# label that displays the formatted total using the total_var stringvar
tk.Label(frame, textvariable=total_var).grid(row=4, column=2, sticky='w')

# now this is the payment entry and processing
# pay_var is a DoubleVar that holds the numeric amount entered by the user as 'amount paid'
pay_var = tk.DoubleVar(value=0.0)

tk.Label(frame, text='amount paid:').grid(row=5, column=0, sticky='w')
pay_entry = tk.Entry(frame, textvariable=pay_var)  # entry widget bound to pay_var for easy numeric reading
pay_entry.grid(row=5, column=1, sticky='w')


# now coming to this fucntion, it is really important as it is made to verify payment, make sure it is in numbers and sufficient, calculate change, and show a summary message box with order details, total, paid amount, and change
def process_order():

    total = calculate_total()                 
    try:
        
        paid = float(pay_var.get())
    except Exception:
        # if conversion fails (e.g., non-numeric input), show an error and return early
        messagebox.showerror('error', 'enter a numeric payment amount')
        return

    if paid < total:
        # if paid amount is less than total, show a warning and do not complete the order
        messagebox.showwarning('insufficient', f'paid {paid:.2f} — need {total:.2f}')
        return

    change = paid - total                     # toc heck for change to return to the customer

    # now create a readable summary: start with burger and base price
    
    base_price = burger_prices.get(burger_var.get(), 0.0)
    summary_lines = [f"burger: {burger_var.get()} (base {base_price:.2f})"]

    # list chosen toppings, condiments, and sides by checking the booleanvars
    chosen_toppings = [k for k, v in toppings_vars.items() if v.get()]
    chosen_conds = [k for k, v in cond_vars.items() if v.get()]
    chosen_sides = [k for k, v in side_vars.items() if v.get()]

    # append chosen items to summary only if any were selected (keeps the summary concise)
    if chosen_toppings:
        summary_lines.append('toppings: ' + ', '.join(chosen_toppings))
    if chosen_conds:
        summary_lines.append('condiments: ' + ', '.join(chosen_conds))
    if chosen_sides:
        summary_lines.append('sides: ' + ', '.join(chosen_sides))

    # append pricing lines: total and paid / change
    summary_lines.append(f'total: {total:.2f}')
    summary_lines.append(f'paid: {paid:.2f} — change: {change:.2f}')

    # join the lines with newline characters and show them in an information messagebox
    messagebox.showinfo('order complete', '\n'.join(summary_lines))

# place order button: when clicked, it runs process_order
order_btn = tk.Button(frame, text='place order', command=process_order)
order_btn.grid(row=6, column=0, columnspan=2, pady=12)

#now finally to run the program
root.mainloop()
