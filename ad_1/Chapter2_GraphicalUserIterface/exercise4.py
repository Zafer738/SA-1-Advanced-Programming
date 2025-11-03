# we are asked to create an registration page (student management system)
# this is a simple registration form layout using tkinter widgets

import tkinter as tk

root = tk.Tk()
root.title("student management system")
root.geometry("400x600")
root.configure(bg="#f5f6fa", padx=20, pady=10)

# the header label
tk.Label(root, text="new student registration", font=("helvetica", 14, "bold"), bg="#f5f6fa").pack(pady=10)

# now the student's name
tk.Label(root, text="student name", anchor="w", bg="#f5f6fa").pack(fill="x")
name_entry = tk.Entry(root)
name_entry.pack(fill="x", pady=5)

# enter their mobile number
tk.Label(root, text="mobile number", anchor="w", bg="#f5f6fa").pack(fill="x")
mobile_entry = tk.Entry(root)
mobile_entry.pack(fill="x", pady=5)

# the email id
tk.Label(root, text="email id", anchor="w", bg="#f5f6fa").pack(fill="x")
email_entry = tk.Entry(root)
email_entry.pack(fill="x", pady=5)

# the user has to enter their home address
tk.Label(root, text="home address", anchor="w", bg="#f5f6fa").pack(fill="x")
address_entry = tk.Entry(root)
address_entry.pack(fill="x", pady=5)

# creating a ( gender ) dropdown  (alternative using option/menu's)
tk.Label(root, text="gender", anchor="w", bg="#f5f6fa").pack(fill="x")
gender_var = tk.StringVar(value="select")
tk.OptionMenu(root, gender_var, "male", "female", "other").pack(fill="x", pady=5)

# this is where the user gets to select their courses (the radio buttons)
tk.Label(root, text="course enrolled", anchor="w", bg="#f5f6fa").pack(fill="x")
course_var = tk.StringVar(value="bsc cc")
courses = ["bsc cc", "bsc cy", "bsc psy", "ba & bm"]
for c in courses:
    tk.Radiobutton(root, text=c, variable=course_var, value=c, bg="#f5f6fa").pack(anchor="w")

# now the user gets to select what languages they know (using checkbutton)
tk.Label(root, text="languages known", anchor="w", bg="#f5f6fa").pack(fill="x")
eng_var = tk.IntVar()
tag_var = tk.IntVar()
hin_var = tk.IntVar()
tk.Checkbutton(root, text="english", variable=eng_var, bg="#f5f6fa").pack(anchor="w")
tk.Checkbutton(root, text="tagalog", variable=tag_var, bg="#f5f6fa").pack(anchor="w")
tk.Checkbutton(root, text="hindi/urdu", variable=hin_var, bg="#f5f6fa").pack(anchor="w")

# ea scale which measures how well they may know a language
tk.Label(root, text="rate your english communication skills", anchor="w", bg="#f5f6fa").pack(fill="x", pady=(10,0))
skill_scale = tk.Scale(root, from_=0, to=10, orient="horizontal")
skill_scale.pack(fill="x", pady=5)

# now the submit area, clears it all after clicked
def submit():
    # it collects the info and shows confirmation
    data = {
        "name": name_entry.get(),
        "mobile": mobile_entry.get(),
        "email": email_entry.get()
    }
    tk.messagebox.showinfo("submitted", f"submitted: {data}")

def clear():
    # to reset all the entries once " submitted "
    name_entry.delete(0, "end")
    mobile_entry.delete(0, "end")
    email_entry.delete(0, "end")
    address_entry.delete(0, "end")
    gender_var.set("select")
    course_var.set("bsc cc")
    eng_var.set(0)
    tag_var.set(0)
    hin_var.set(0)
    skill_scale.set(0)

from tkinter import messagebox
# now making the sumbit and clear buttons, frames for it and the button itself.
btn_frame = tk.Frame(root, bg="#f5f6fa")
btn_frame.pack(pady=15)
tk.Button(btn_frame, text="submit", command=submit, width=12).pack(side="left", padx=10)
tk.Button(btn_frame, text="clear", command=clear, width=12).pack(side="left", padx=10)

#run the program
root.mainloop()
