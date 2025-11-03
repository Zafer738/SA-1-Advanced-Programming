# so we are asked to create a "tabbed" ( e.g like the tabs opened on chrome ) area calculator for circle, square, and rectangle
# so i've used the notebook widget cause it provides separate tabs, each containing inputs and a calculation button

import tkinter as tk
from tkinter import ttk
import math  # imports the mathematical constants 

# create the main window, window size, padding ect..
root = tk.Tk()
root.title('Area Calculator - tabs')
root.geometry('420x260')
root.configure(padx=10, pady=10)

# create the notebook widget 
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# this is the circle tab
circle_tab = ttk.Frame(notebook)  # creating the frame that will be used as the circle tab content
notebook.add(circle_tab, text='circle')  # adding the frame to the notebook with tab text 'circle'

# there are the variables to hold the radius input and result text
c_radius_var = tk.DoubleVar(value=1.0)  # doublevar stores float numbers for tkinter widgets
c_result_var = tk.StringVar(value='')   # stringvar stores text results that will be shown

# moreover, this is the label and entry for radius
tk.Label(circle_tab, text='radius:').grid(row=0, column=0, padx=6, pady=6, sticky='w')
tk.Entry(circle_tab, textvariable=c_radius_var).grid(row=0, column=1, padx=6, pady=6)

# creating the function to calculate area of a circle given the radius
def calc_circle_area():
    try:
        r = float(c_radius_var.get())  # check the radius and ensure it's a float
    except Exception:
        c_result_var.set('enter a valid number')
        return
    if r < 0:
        c_result_var.set('radius must be non-negative')
        return
    # area formula: pi * r^2
    area = math.pi * r * r
    c_result_var.set(f'area = {area:.4f}')  # setting the result with 4 decimal places so its easier to read

# creating the calculate button and (result) display label
tk.Button(circle_tab, text='calculate', command=calc_circle_area).grid(row=1, column=0, columnspan=2, pady=6)
tk.Label(circle_tab, textvariable=c_result_var).grid(row=2, column=0, columnspan=2)

# this is the square tab
square_tab = ttk.Frame(notebook)
notebook.add(square_tab, text='square')

s_side_var = tk.DoubleVar(value=1.0)  # holds the side length input
s_result_var = tk.StringVar(value='')  # contains the result text for square

tk.Label(square_tab, text='side length:').grid(row=0, column=0, padx=6, pady=6, sticky='w')
tk.Entry(square_tab, textvariable=s_side_var).grid(row=0, column=1, padx=6, pady=6)

# now this is the to calculate the area of a square, checking if its valid or not
def calc_square_area():
    try:
        s = float(s_side_var.get())  # read side length
    except Exception:
        s_result_var.set('enter a valid number')
        return
    if s < 0:
        s_result_var.set('side must be non-negative')
        return
    area = s * s  # square area formula, side^2
    s_result_var.set(f'area = {area:.4f}')

#creating the buttons that runs the whole thing after the user clicks it, with values entered...
tk.Button(square_tab, text='calculate', command=calc_square_area).grid(row=1, column=0, columnspan=2, pady=6)
tk.Label(square_tab, textvariable=s_result_var).grid(row=2, column=0, columnspan=2)

#this is the rectangle tab
rect_tab = ttk.Frame(notebook)
notebook.add(rect_tab, text='rectangle')

r_width_var = tk.DoubleVar(value=1.0)  # variable for width
r_height_var = tk.DoubleVar(value=1.0)  # variable for height
r_result_var = tk.StringVar(value='')   # variable that  shows the result

tk.Label(rect_tab, text='width:').grid(row=0, column=0, padx=6, pady=6, sticky='w')
tk.Entry(rect_tab, textvariable=r_width_var).grid(row=0, column=1, padx=6, pady=6)

tk.Label(rect_tab, text='height:').grid(row=1, column=0, padx=6, pady=6, sticky='w')
tk.Entry(rect_tab, textvariable=r_height_var).grid(row=1, column=1, padx=6, pady=6)

#now this is the to calculate the area of a rectangle, checking if its valid or not
def calc_rect_area():
    try:
        w = float(r_width_var.get())
        h = float(r_height_var.get())
    except Exception:
        r_result_var.set('enter valid numbers')
        return
    if w < 0 or h < 0:
        r_result_var.set('dimensions must be non-negative')
        return
    area = w * h  # rectangle area formula: width * height
    r_result_var.set(f'area = {area:.4f}')

#making the buttons that runs/calculates the whole thing, positioning it ect..
tk.Button(rect_tab, text='calculate', command=calc_rect_area).grid(row=2, column=0, columnspan=2, pady=6)
tk.Label(rect_tab, textvariable=r_result_var).grid(row=3, column=0, columnspan=2)

#finally to run the program
root.mainloop()
