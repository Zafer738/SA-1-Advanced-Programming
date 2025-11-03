# so this is an canvas drawing app, where the user gets to select a shape and provide coordinates

import tkinter as tk
from tkinter import ttk

# create the main window, set window size, add padding...
root = tk.Tk()
root.title('draw shape')
root.geometry('600x420')
root.configure(padx=10, pady=10)

# now create the canvas widges, this gives an area where shapes (lines, ovals, rectangles, polygons) can be drawn
canvas = tk.Canvas(root, width=420, height=300, bg='white')
canvas.grid(row=0, column=0, rowspan=6, padx=8, pady=8)

# control frame placed to the right of the canvas
ctrl = tk.Frame(root)
ctrl.grid(row=0, column=1, sticky='n')

# making the dropdown for shape selection
shape_var = tk.StringVar(value='rectangle')
shapes = ['oval', 'rectangle', 'square', 'triangle']
shape_menu = ttk.Combobox(ctrl, textvariable=shape_var, values=shapes, state='readonly')
shape_menu.grid(row=0, column=0, pady=6)

# here's the entry for coordinates, its comma-separated integer values like '50,50,200,150' so the user can input accordingly
coord_var = tk.StringVar(value='50,50,200,150')
coord_entry = tk.Entry(ctrl, textvariable=coord_var, width=20)
coord_entry.grid(row=1, column=0, pady=6)

# here's the function to coordinate string into a list of integers
def parse_coords(s):
    try:
        # split by comma, strip whitespace, filter out empty tokens, and convert to int
        parts = [int(p.strip()) for p in s.split(',') if p.strip()!='']
        return parts
    except Exception:
        # return none if failure
        return None

# this function is to draw the selected shape on the canvas using the coordinates inputed
def draw_shape():
    coords = parse_coords(coord_var.get())
    if not coords:
        # if coords is wrong (None or empty), show a message on the canvas
        canvas.create_text(210, 150, text='invalid coordinates', fill='red')
        return
    shape = shape_var.get()
    canvas.delete('all')  # clear previous drawings so each draw replaces the old one, once the user switches

    if shape == 'oval':
        # oval requires four coordinates, for eg x1, y1, x2, y2 
        if len(coords) >= 4:
            canvas.create_oval(coords[0], coords[1], coords[2], coords[3], fill='lightgreen')
        else:
            canvas.create_text(210, 150, text='need 4 coordinates for oval', fill='red')
    elif shape == 'rectangle':
        # rectangle also requires four coordinates, then also i've set diff colors for each shape
        if len(coords) >= 4:
            canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill='lightblue')
        else:
            canvas.create_text(210, 150, text='need 4 coordinates for rectangle', fill='red')
    elif shape == 'square':
        # however, a square can accept either three coordinates (x, y, side) or four coordiniates (x1,y1,x2,y2)
        if len(coords) >= 3:
            x, y, side = coords[0], coords[1], coords[2]
            canvas.create_rectangle(x, y, x+side, y+side, fill='orange')
        elif len(coords) >= 4:
            canvas.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill='orange')
        else:
            canvas.create_text(210, 150, text='need 3 or 4 coordinates for square', fill='red')
    elif shape == 'triangle':
        # a triangle requires six coords: x1,y1, x2,y2, x3,y3 ,and its inputed different from the rest
        if len(coords) >= 6:
            canvas.create_polygon(coords[0], coords[1], coords[2], coords[3], coords[4], coords[5], fill='pink')
        else:
            canvas.create_text(210, 150, text='need 6 coordinates for triangle', fill='red')

# now creating ther button to draw based on the current selection and coordinates that the user has selected..
draw_btn = tk.Button(ctrl, text='draw', command=draw_shape)
draw_btn.grid(row=2, column=0, pady=8)

#finally to run the program
root.mainloop()
