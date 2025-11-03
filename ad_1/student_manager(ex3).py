
# STUDENT MANAGER - Tkinter GUI Version
 
# so we are asked to display: -->
#  all student records
#  an individual student's record
#  show the highest-scoring student
#  show the lowest-scoring student

import tkinter as tk                 
from tkinter import ttk, messagebox  

# here's the function: load_students
# it reads all student data from a text file, calculates the total, percentages, and gives the grades accordingly.

def load_students(filename):
    students = []  #crate an empty list

    file = open(filename, "r")
    lines = file.readlines()  # read all lines into a list
    file.close()              #close it


    #first line of the ( txt ) file tells us how many students there are
    num_students = int(lines[0])


    for line in lines[1:]:
        #splitting each line by commas
        parts = [p.strip() for p in line.split(",")]

        #assinging each part to a vriable so its organized
        student_id = parts[0]             # eg: "1001"
        name = parts[1]                   # eg: "Ava Williams"
        coursework = list(map(int, parts[2:5]))  # marks
        exam = int(parts[5])              #the exam marks (out of 100)

        #to calculate total(sum of three marks)
        cw_total = sum(coursework)

        #to calculate overall percentage
        overall = ((cw_total + exam) / 160) * 100

        #to determine the grades based on % percentage
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

        #now store all the student info in a dictionary
        students.append({
            "id": student_id,
            "name": name,
            "cw_total": cw_total,
            "exam": exam,
            "overall": overall,
            "grade": grade
        })

    return students  


#create a class: StudentManagerApp, it manages the GUI (window, buttons, etc.)

class StudentManagerApp:
    def __init__(self, root):
        # window setup
        self.root = root
        self.root.title("Student Manager")        # Title bar text
        self.root.configure(bg="#1E90FF")         # blue bg

        # load student data from file
        self.students = load_students("studentMarks.txt")

        # GUI layout section
        # the title label at the top
        title = tk.Label(
            root,
            text="Student Manager",
            bg="#1E90FF",
            fg="white",
            font=("Segoe UI", 18, "bold")
        )
        title.pack(pady=10)  #add padding

        # the frame that has all the action buttons (View All, Highest, Lowest)
        btn_frame = tk.Frame(root, bg="#1E90FF")
        btn_frame.pack(pady=10)

        #now create the button's
        self.create_button(btn_frame, "View All Student Records", self.view_all, 0, 0)
        self.create_button(btn_frame, "Show Highest Score", self.show_highest, 0, 1)
        self.create_button(btn_frame, "Show Lowest Score", self.show_lowest, 0, 2)

        # now making the dropdown section, first we make the frame... this is not for the button
        view_frame = tk.Frame(root, bg="#1E90FF")
        view_frame.pack(pady=10)

        # the label for dropdown section
        label = tk.Label(
            view_frame,
            text="View Individual Student Record:",
            bg="#1E90FF",
            fg="white",
            font=("Segoe UI", 10, "bold")
        )
        label.grid(row=0, column=0, padx=5, pady=5)

        # creating the dropdown box, listing all student names
        names = [s["name"] for s in self.students]
        self.selected_name = tk.StringVar()  # holds specific, chosen student's name
        self.combo = ttk.Combobox(
            view_frame,
            textvariable=self.selected_name,
            values=names,
            width=25
        )
        self.combo.grid(row=0, column=1, padx=5)

        # crate an button to display the selected students record
        self.create_button(view_frame, "View Record", self.view_record, 0, 2)

        #crate the text area/box below to show results of whatever the user searches
        self.output = tk.Text(
            root,
            width=60,
            height=12,
            bg="black",
            fg="white",
            font=("Consolas", 10),
            wrap="word"
        )
        self.output.pack(padx=10, pady=15)


    #creating button with the same style style
    def create_button(self, parent, text, command, row, col):
        btn = tk.Button(
            parent,
            text=text,
            command=command,         
            bg="#104E8B",             # darker blue
            fg="white",
            font=("Segoe UI", 9, "bold"),
            width=22
        )
        btn.grid(row=row, column=col, padx=5, pady=5)


    # the " view all " displays all students' info with class average

    def view_all(self):
        self.output.delete(1.0, tk.END)  # to clear old text first which may have been there before
        total_percentage = 0

        #goes through each student and displays all their data
        for s in self.students:
            total_percentage += s["overall"]
            self.output.insert(tk.END, self.format_student(s) + "\n\n")

        #at the end it shows count and average
        avg = total_percentage / len(self.students)
        self.output.insert(tk.END, f"Total students: {len(self.students)}\n")
        self.output.insert(tk.END, f"Class average percentage: {avg:.2f}%\n")

    
    # shows one/specific students record ( selected from dropdown )
    def view_record(self):
        name = self.selected_name.get()  
        # find the student dictionary to match the name user has asked for
        student = next((s for s in self.students if s["name"] == name), None)

        #clear the box
        self.output.delete(1.0, tk.END)

        if student:
            #once the user chooses it shows all the info about the student..
            self.output.insert(tk.END, self.format_student(student))
        else:
            #if the user asks for something else it displays an error
            messagebox.showerror("Error", "Please select a valid student.")

    
    # now to display the student with the highest marks
    def show_highest(self):
        self.output.delete(1.0, tk.END)
        highest = max(self.students, key=lambda s: s["overall"])  # using max()
        self.output.insert(tk.END, "Student with Highest Score:\n\n")
        self.output.insert(tk.END, self.format_student(highest))


    # now to display the student with the lowest marks
    def show_lowest(self):
        self.output.delete(1.0, tk.END)
        lowest = min(self.students, key=lambda s: s["overall"])  #using min()
        self.output.insert(tk.END, "Student with Lowest Score:\n\n")
        self.output.insert(tk.END, self.format_student(lowest))

    
    
    def format_student(self, s): #this function neatly arranges one student's information, so it looks clean and more readable
        #it formats each student's details neatly using f-strings
        return (
            f"Name: {s['name']}\n"
            f"Number: {s['id']}\n"
            f"Coursework Total: {s['cw_total']}\n"
            f"Exam Mark: {s['exam']}\n"
            f"Overall Percentage: {s['overall']:.2f}%\n"
            f"Grade: {s['grade']}"
        )


# finally create the main program to run the GUI
if __name__ == "__main__":
    root = tk.Tk()                #create the main window
    app = StudentManagerApp(root) #pass the window to our class
    root.mainloop()               
