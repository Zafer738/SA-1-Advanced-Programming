
# so we are asked to create an greeting app with two frames, the inputframe and displayframe

import tkinter as tk
from tkinter import ttk

# create the main window first

root = tk.Tk()  
root.title('greeting app')  
root.geometry('420x180')  # set the window size 
root.configure(padx=10, pady=10)  # add padding 


# "frames" are used to group related widgets visually and/layout-wise
# we create two frames, one input_frame for the controls and display_frame for showing results
#here is the input frame, its a child of root, set the background color, bd, ect...

input_frame = tk.Frame(root, bg='lightyellow', bd=2, relief='groove')

input_frame.pack(fill='x', padx=5, pady=(0,8))
# padx and pady add external spacing around the frame.

display_frame = tk.Frame(root, bg='lightblue', bd=2, relief='ridge')
# display_frame is where the greeting will appear, the different bg so it not the same color

display_frame.pack(fill='both', expand=True, padx=5)
# fill='both' allows the frame to expand in both directions& when expand=True, it lets it grow


# now creating the input frame widgets, a title label, an entry, a color dropdown, and a button

title_label = tk.Label(input_frame, text='enter your name and choose a color', fg='blue', bg='lightyellow')
# the label shows some text. fg sets text color. bg matches the frame so it blends in.

title_label.grid(row=0, column=0, columnspan=3, sticky='w', padx=6, pady=(6,4))
# row and column specify the grid cell. 

# where the user enters their name
name_var = tk.StringVar()  #stringvar holds the text
name_entry = tk.Entry(input_frame, textvariable=name_var, width=30)


name_entry.grid(row=1, column=0, padx=6, pady=6)


# here's the dropdown menu for selecting thje color
color_var = tk.StringVar(value='black')  # holds the selected color, but its black by default
color_options = ['black', 'red', 'green', 'blue', 'purple']  # the color choices that are given
color_menu = ttk.OptionMenu(input_frame, color_var, color_var.get(), *color_options)


color_menu.grid(row=1, column=1, padx=6, pady=6)
# places the dropdown to the right of the name entry

# now create the function that updates the greeting in display_frame
def update_greeting():
    # read the input values
    name = name_var.get().strip()  # get the text and remove sthe whitespace
    color = color_var.get()  # get the selected color from the dropdown

    # now making a greeting text based on whether the user provided a name
    if name == '':
        greeting_text = 'hello, stranger! please enter your name.'
    else:
        greeting_text = f'hello, {name}! nice to see you.'

    # clearing any existing widgets inside display_frame
    # winfo_children() returns a list of child widgets, the "destroy" is to reset the display area
    for widget in display_frame.winfo_children():
        widget.destroy()

    # creating a new label in display_frame to show the greeting
    greeting_label = tk.Label(display_frame, text=greeting_text, fg=color, bg='lightblue', font=('arial', 14))
    # fg uses the chosen color so the greeting appears in that color
    # font tuple ('family', size) sets the text size for readability

    greeting_label.pack(padx=10, pady=10)
    # pack the greeting label with padding

# update greeting button in input_frame, then position it
update_button = tk.Button(input_frame, text='update greeting', command=update_greeting)
update_button.grid(row=1, column=2, padx=6, pady=6)

#now finally run the program
root.mainloop()

