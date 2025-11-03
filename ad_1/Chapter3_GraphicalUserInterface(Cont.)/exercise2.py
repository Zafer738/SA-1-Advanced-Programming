
# so this is my coffee vending machine gui with image, selection controls, and payment handling

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

# create main window object 
root = tk.Tk()                               
root.title('coffee vending machine')         # set the title text
root.geometry('520x320')                     # set window size 
root.configure(padx=10, pady=10)             # add padding 

# the main_frame is a parent container to hold both image and control sections, buttons, display and all..
main_frame = tk.Frame(root)                  # create a frame to organize the layout, and fill frame
main_frame.pack(fill='both', expand=True)    

# image_frame sits on the left side of main_frame and shows/displays an coffee image
image_frame = tk.Frame(main_frame, width=220, height=220)
image_frame.grid(row=0, column=0, padx=8, pady=8, sticky='n')   #place it in grid

# control_frame sits on the right side for dropdowns, buttons, ect... this is where the user interacts with the vending machine
control_frame = tk.Frame(main_frame)
control_frame.grid(row=0, column=1, padx=8, pady=8, sticky='n')

# inside image_frame we add a label that will hold an image or fallback text
image_label = tk.Label(image_frame)
image_label.pack()   

#to load a basic built-in image from tkinter
images_dir = os.path.join(os.path.dirname(__file__), 'images') if '__file__' in globals() else 'images'
img_path = os.path.join(images_dir, 'coffee1.png')   # the image file

try:
    
    if os.path.exists(img_path):
        coffee_img = tk.PhotoImage(file=img_path)    
        image_label.configure(image=coffee_img)      
        image_label.image = coffee_img               
    else:
        #if image not found
        image_label.configure(text='place an image at images/coffee1.png', width=28, height=10)
except Exception:
    # if any error occurs it shows a message instead of closing down..
    image_label.configure(text='error loading image - check images/coffee1.png', width=28, height=10)

# here's the coffee type section, where the suer gets to slect their preffered coffee type
coffee_var = tk.StringVar(value='espresso')              # holds the current selected coffee type
coffee_label = tk.Label(control_frame, text='choose coffee:')   # label for dropdown
coffee_label.grid(row=0, column=0, sticky='w')           

coffee_choices = ['espresso', 'americano', 'latte', 'cappuccino']  #heres the dropdown options

# ttk.Combobox creates a dropdown list linked to coffee_var
coffee_menu = ttk.Combobox(control_frame, textvariable=coffee_var, values=coffee_choices, state='readonly')
coffee_menu.grid(row=0, column=1, pady=6, padx=6)        

# now this si the dugar sleection section, user gets to select how much sugar they'd like in their coffee's
sugar_var = tk.IntVar(value=1)                           # integer variable for sugar amount
sugar_label = tk.Label(control_frame, text='sugar (spoons):')
sugar_label.grid(row=1, column=0, sticky='w')            

# the "Spinbox" allows user to pick numeric values by clicking up or down arrows
sugar_spin = tk.Spinbox(control_frame, from_=0, to=5, textvariable=sugar_var, width=5)
sugar_spin.grid(row=1, column=1, pady=6)

#now here's the " MILK " option, user gets to select what they prefer
milk_var = tk.BooleanVar(value=True)                     # the boolean variable for milk yes/no
milk_check = tk.Checkbutton(control_frame, text='add milk', variable=milk_var)
milk_check.grid(row=2, column=0, columnspan=2, sticky='w')   # this occupies two columns

# now this function is to show a summary of user selection in a popup box
def show_selection():
    coffee = coffee_var.get()                            # get the coffee type 
    sugar = sugar_var.get()                              # how ,uch sugar the user selects
    milk = 'yes' if milk_var.get() else 'no'             # translate boolean to text
    msg = f'you chose: {coffee}\nsugar: {sugar}\nmilk: {milk}'   # create formatted message on what the user picked
    # messagebox to show standard popup dialog box for warning, or info
    messagebox.showinfo('selection', msg)                

# create the button to confirm the current drink selection
confirm_btn = tk.Button(control_frame, text='make coffee', command=show_selection)
confirm_btn.grid(row=3, column=0, columnspan=2, pady=10)   # grid positions 

# now this was an extension part in the question, to create a payment handling area
# create a labeled frame section to visually hold the  payment controls together
money_frame = tk.LabelFrame(control_frame, text='payment (extension)')
money_frame.grid(row=4, column=0, columnspan=2, pady=6, sticky='we')

price_var = tk.DoubleVar(value=2.50)                    
amount_var = tk.DoubleVar(value=0.0)                     

# price label and display side by side
price_label = tk.Label(money_frame, text='price:')
price_label.grid(row=0, column=0, sticky='w')
price_display = tk.Label(money_frame, textvariable=price_var)   # automatically shows price_var value
price_display.grid(row=0, column=1, sticky='w')

# here's the entry for amount user pays
amount_label = tk.Label(money_frame, text='amount paid:')
amount_label.grid(row=1, column=0, sticky='w')
amount_entry = tk.Entry(money_frame, textvariable=amount_var)   # user types payment value here
amount_entry.grid(row=1, column=1, sticky='w')

# here's the function that checks the payment and calculates change, or if not enough
def process_payment():
    try:
        paid = float(amount_var.get())                    # convert entry text to a number
    except Exception:
        # show error if user types letters
        messagebox.showerror('error', 'please enter a numeric amount')
        return
    price = float(price_var.get())                        # the current price
    if paid < price:
        # if user paid less than required, it shows this message, a warning perhaps..
        messagebox.showwarning('insufficient', f'paid {paid:.2f} — please provide at least {price:.2f}')
    else:
        # if payment is enough, then it calcualtes the change accordingly
        change = paid - price
        # display a " payment accepted" message with formatted change
        messagebox.showinfo('payment accepted', f'payment accepted. change: {change:.2f}')

# once the user clicks this button, it processes the payment
pay_btn = tk.Button(money_frame, text='pay', command=process_payment)
pay_btn.grid(row=2, column=0, columnspan=2, pady=6)

#now finally run the program
root.mainloop()

