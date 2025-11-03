# so we need to make changes to the previous ( Student Manager ) GUI in Tkinter
# so we need to allow the user to:
# view all student records
# view an individual student
#  show the highest marks
#  show the lowest marks
#  sort the student records
#  to add a new student 
#  to delete an existing student
#  to update an existing student
#
# the changes should be saved to ( studentMarks.txt ) so the data is updated in the system

import tkinter as tk
from tkinter import ttk, messagebox


# here's the  function: load_students(filename)
# goes through the student data from the file and stores it in a list of dictionaries.
# each dictionary holds ID, name, coursework marks, exam mark, overall %, and grade.

def load_students(filename):
    students = []
    with open(filename, "r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    num_students = int(lines[0])  # The first line stores the total number of students

    # to go through each student's record line-by-line
    for line in lines[1:]:
        parts = [p.strip() for p in line.split(",")]
        sid = parts[0]
        name = parts[1]
        cw_marks = list(map(int, parts[2:5]))  
        exam = int(parts[5])
        cw_total = sum(cw_marks)
        overall = ((cw_total + exam) / 160) * 100  #to calculate overall percentage

        #to give the grade based on percentage
        if overall >= 70:
            grade = "A"
        elif overall >= 60:
            grade = "B"
        elif overall >= 50:
            grade = "C"
        elif overall >= 40:
            grade = "D"
        else:
            grade = "F"

        #storing data for the student
        students.append({
            "id": sid, "name": name, "cw": cw_marks,
            "cw_total": cw_total, "exam": exam,
            "overall": overall, "grade": grade
        })
    return students



#now here's the function: save_students(filename, students)
# it writes/updates all student records back into the text file after any changes
# it makes sure that records are added, deleted, or updated... accordingly 

def save_students(filename, students):
    with open(filename, "w") as file:
        file.write(f"{len(students)}\n")  #the first line = total number of students
        for s in students:
            cw = ",".join(map(str, s["cw"]))  #join the coursework marks into a single string
            file.write(f"{s['id']}, {s['name']}, {cw},{s['exam']}\n")



# now here's the function: recalc(student)
# it recalculates coursework total, overall percentage, and grade after the user updates anything.. for eg if the user adds or updates any record of the students!

def recalc(student):
    student["cw_total"] = sum(student["cw"])
    student["overall"] = ((student["cw_total"] + student["exam"]) / 160) * 100
    if student["overall"] >= 70:
        student["grade"] = "A"
    elif student["overall"] >= 60:
        student["grade"] = "B"
    elif student["overall"] >= 50:
        student["grade"] = "C"
    elif student["overall"] >= 40:
        student["grade"] = "D"
    else:
        student["grade"] = "F"



# now here's the class: StudentManagerApp
# it handles the graphical interface and functionality of the program, like the visuals

class StudentManagerApp:
    def __init__(self, root):
        
        self.root = root
        self.root.title("Student Manager")
        self.root.configure(bg="#1E90FF")  #blue bg
        self.filename = "studentMarks.txt"
        self.students = load_students(self.filename)  #load all the data on start-up

        
        #the title label
        tk.Label(root, text="STUDENT MANAGER", font=("Arial", 18, "bold"),
                 bg="#1E90FF", fg="white").pack(pady=8)

        
        #frame for the menu buttons
        frame = tk.Frame(root, bg="#1E90FF")
        frame.pack(pady=4)

        # Each button is one of the menu options given in the brief (1–8)
        buttons = [
            (" View All", self.view_all),
            (" View Individual", self.view_individual),
            (" Highest Score", self.show_highest),
            (" Lowest Score", self.show_lowest),
            (" Sort Records", self.sort_records),
            (" Add Student", self.add_student),
            (" Delete Student", self.delete_student),
            (" Update Student", self.update_student)
        ]

        #arranging the buttons in two columns using a grid layout
        for i, (text, cmd) in enumerate(buttons):
            tk.Button(frame, text=text, command=cmd,
                      bg="#104E8B", fg="white", width=18).grid(row=i // 2, column=i % 2, padx=5, pady=5)

        
        # now creating the student selection dropdown 
        # it it used for viewing or selecting individual students
        self.selected_name = tk.StringVar()
        self.dropdown = ttk.Combobox(root, textvariable=self.selected_name,
                                     values=[s["name"] for s in self.students], width=30)
        self.dropdown.pack(pady=4)

        
        # this is the output box, where the text would be displayed.
        # it displays results and student information.

        self.output = tk.Text(root, width=60, height=12,
                              bg="black", fg="white", font=("Consolas", 10))
        self.output.pack(pady=8)

    
    # here's the helper, it formats a students details properly, so it can be displayed neat
    def format_student(self, s):
        return (f"Name: {s['name']}\n"
                f"ID: {s['id']}\n"
                f"Coursework: {s['cw'][0]}, {s['cw'][1]}, {s['cw'][2]} "
                f"(Total: {s['cw_total']})\n"
                f"Exam: {s['exam']}\n"
                f"Overall: {s['overall']:.2f}% | Grade: {s['grade']}\n")

    #this updates the dropdown menu after adding or deleting students
    def refresh_dropdown(self):
        self.dropdown["values"] = [s["name"] for s in self.students]


    #so we were asked to create 8 buttons, including the additional options.

    # 1 - to view all student records
    # to display all students with their scores, grades, and class average
    def view_all(self):
        self.output.delete(1.0, tk.END)
        total = sum(s["overall"] for s in self.students)
        for s in self.students:
            self.output.insert(tk.END, self.format_student(s) + "\n")
        avg = total / len(self.students)
        self.output.insert(tk.END, f"\nClass Size: {len(self.students)}\nAverage Mark: {avg:.2f}%\n")

    
    # 2 - to view an individual student
    # to display only one students details based on user selection, in the dropdown
    
    def view_individual(self):
        name = self.selected_name.get()
        s = next((x for x in self.students if x["name"] == name), None)
        self.output.delete(1.0, tk.END)
        if s:
            self.output.insert(tk.END, self.format_student(s))
        else:
            self.output.insert(tk.END, "Student not found.\n")

    
    # 3 - to find and display the student with the highest overall score

    def show_highest(self):
        top = max(self.students, key=lambda s: s["overall"])
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, "Highest Scorer:\n\n" + self.format_student(top))

    # 4 - to find and display the student with the lowest overall score
    
    def show_lowest(self):
        low = min(self.students, key=lambda s: s["overall"])
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, "Lowest Scorer:\n\n" + self.format_student(low))

    
    # 5 - to sort the student records
    # opens a small window that lets the user choose sort field and order, like ascending, and descending
    
    def sort_records(self):
        win = tk.Toplevel(self.root)
        win.title("Sort Students")
        win.configure(bg="#1E90FF")

        tk.Label(win, text="Sort by:", bg="#1E90FF", fg="white").grid(row=0, column=0, padx=5, pady=5)
        sort_by = tk.StringVar(value="Name")
        box = ttk.Combobox(win, textvariable=sort_by,
                           values=["Name", "ID", "Overall"], width=15)
        box.grid(row=0, column=1)

        tk.Label(win, text="Order:", bg="#1E90FF", fg="white").grid(row=1, column=0)
        order = tk.StringVar(value="Ascending")
        box2 = ttk.Combobox(win, textvariable=order,
                            values=["Ascending", "Descending"], width=15)
        box2.grid(row=1, column=1)

        # it'll sort and update display when button is clicked

        def apply_sort():
            key = sort_by.get()
            reverse = (order.get() == "Descending")
            if key == "Name":
                self.students.sort(key=lambda s: s["name"], reverse=reverse)
            elif key == "ID":
                self.students.sort(key=lambda s: int(s["id"]), reverse=reverse)
            else:
                self.students.sort(key=lambda s: s["overall"], reverse=reverse)
            self.refresh_dropdown()
            self.view_all()
            win.destroy()

        tk.Button(win, text="Sort", command=apply_sort,
                  bg="#104E8B", fg="white").grid(row=2, column=0, columnspan=2, pady=8)


    # 6 - to add student
    # it opens a small window to enter new students details, like if the user wants to add a new student
    
    def add_student(self):
        win = tk.Toplevel(self.root)
        win.title("Add Student")
        win.configure(bg="#1E90FF")

        labels = ["ID", "Name", "CW1", "CW2", "CW3", "Exam"]
        entries = []

        # to create labels and entry fields for each data point
        for i, label in enumerate(labels):
            tk.Label(win, text=label, bg="#1E90FF", fg="white").grid(row=i, column=0, padx=5, pady=5)
            e = tk.Entry(win, width=25)
            e.grid(row=i, column=1)
            entries.append(e)

        # save the new records to the file and refresh
        def save_new():
            sid = entries[0].get().strip()
            name = entries[1].get().strip()
            cw = [int(entries[2].get()), int(entries[3].get()), int(entries[4].get())]
            exam = int(entries[5].get())
            new = {"id": sid, "name": name, "cw": cw, "exam": exam}
            recalc(new)
            self.students.append(new)
            save_students(self.filename, self.students)
            self.refresh_dropdown()
            self.view_all()
            win.destroy()

        tk.Button(win, text="Add", command=save_new,
                  bg="#104E8B", fg="white").grid(row=6, column=0, columnspan=2, pady=8)

    # 7 - if the user wants to delete a student
    # the user can pick a student to remove from the list and the ( studentMarks.txt ) file
    
    def delete_student(self):
        win = tk.Toplevel(self.root)
        win.title("Delete Student")
        win.configure(bg="#1E90FF")

        tk.Label(win, text="Select student:", bg="#1E90FF", fg="white").grid(row=0, column=0, padx=5, pady=5)
        sel = tk.StringVar()
        box = ttk.Combobox(win, textvariable=sel, values=[s["name"] for s in self.students], width=25)
        box.grid(row=0, column=1)

        def delete_action():
            name = sel.get()
            self.students = [s for s in self.students if s["name"] != name]
            save_students(self.filename, self.students)
            self.refresh_dropdown()
            self.view_all()
            win.destroy()

        tk.Button(win, text="Delete", command=delete_action,
                  bg="#B22222", fg="white").grid(row=1, column=0, columnspan=2, pady=8)

    # 8 - to update details about a student
    # opens a sub-window where the user can modify the existing details

    def update_student(self):
        win = tk.Toplevel(self.root)
        win.title("Update Student")
        win.configure(bg="#1E90FF")

        tk.Label(win, text="Select student:", bg="#1E90FF", fg="white").grid(row=0, column=0)
        sel = tk.StringVar()
        box = ttk.Combobox(win, textvariable=sel, values=[s["name"] for s in self.students], width=25)
        box.grid(row=0, column=1)

        # when the button 'Edit' is clicked, opens a detailed edit window!
        def edit_selected():
            name = sel.get()
            s = next((x for x in self.students if x["name"] == name), None)
            if not s:
                return
            win.destroy()
            self.open_edit_window(s)

        tk.Button(win, text="Edit", command=edit_selected,
                  bg="#104E8B", fg="white").grid(row=1, column=0, columnspan=2, pady=8)

    
    # it opens the editable form for updating student data
    
    def open_edit_window(self, s):
        win = tk.Toplevel(self.root)
        win.title("Edit Student")
        win.configure(bg="#1E90FF")

        fields = ["ID", "Name", "CW1", "CW2", "CW3", "Exam"]
        values = [s["id"], s["name"], *map(str, s["cw"]), str(s["exam"])]
        entries = []
        for i in range(6):
            tk.Label(win, text=fields[i], bg="#1E90FF", fg="white").grid(row=i, column=0)
            e = tk.Entry(win, width=25)
            e.insert(0, values[i])  # pre-fill the current values
            e.grid(row=i, column=1)
            entries.append(e)

        def save_changes():
            s["id"] = entries[0].get()
            s["name"] = entries[1].get()
            s["cw"] = [int(entries[2].get()), int(entries[3].get()), int(entries[4].get())]
            s["exam"] = int(entries[5].get())
            recalc(s)
            save_students(self.filename, self.students)
            self.refresh_dropdown()
            self.view_all()
            win.destroy()

        tk.Button(win, text="Save", command=save_changes,
                  bg="#104E8B", fg="white").grid(row=6, column=0, columnspan=2, pady=8)



# finally run the program

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagerApp(root)
    root.mainloop()
