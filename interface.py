from tkinter import *
import tkinter as tk
from tkinter import ttk
from ClassScheduling import *
from datetime import datetime
import random
from tkinter import messagebox


class CourseSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Course Scheduler Informatics Engineering")

        self.data = [
            {'Course': 'CSE102', 'Day': 'Wednesday', 'Time': '10:00-11:40'},
            {'Course': 'CSE401', 'Day': 'Monday', 'Time': '10:00-11:40'},
            {'Course': 'CSE101', 'Day': 'Friday', 'Time': '8:00-9:40'}
        ]

        # Create a Treeview widget
        self.tree = ttk.Treeview(root)
        self.tree["columns"] = ("course name", "day", "time")
        self.tree.heading("#0", text="Course")
        self.tree.heading("course name", text="Course Name")
        self.tree.heading("day", text="Day")
        self.tree.heading("time", text="Time")

        # Komponen GUI
        self.label = tk.Label(root, text="Course List:")
        self.label.pack()

        self.course_list = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.course_list.pack()

        self.courses_id_dict = courses_id_dict

        self.page = 0

        # Tambahkan pilihan mata kuliah ke dalam Listbox
        # for i in self.data:
        #     self.course_list.insert(tk.END, i['Course'])

        self.course_list.insert(tk.END, "Data Structures and Algorithms")
        self.course_list.insert(tk.END, "Artificial Intelligence")
        self.course_list.insert(tk.END, "Introduction to Computer Science")
        self.course_list.insert(tk.END, "Operating Systems")
        self.course_list.insert(tk.END, "Database Systems")
        self.course_list.insert(tk.END, "Computer Networks")
        self.course_list.insert(tk.END, "Web Programming")
        self.course_list.insert(tk.END, "Software Engineering")
        self.course_list.insert(tk.END, "Computer Graphics")
        self.course_list.insert(tk.END, "Internet Security")
        self.course_list.insert(tk.END, "Parallel and Distributed Computing")
        self.course_list.insert(tk.END, "Data Mining and Knowledge Discovery")

        self.start_button = tk.Button(root, text="Start", command=self.start_genetic_algorithm)
        self.start_button.pack()

    def insert_to_table(self, result):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for data in result[self.page]:
            course = data
            course_name = self.courses_id_dict[data]
            day = result[self.page][data][0]
            time = result[self.page][data][1]
            self.tree.insert("", "end", text=course, values=(course_name, day, time))

        self.tree.pack()

    def next_page(self, result):
        self.page += 1
        self.insert_to_table(result)

    def next_page_button(self, result):
        self.next_button = tk.Button(root, text="Next", command=self.next_page(result))
        self.next_button.pack()

    def start_genetic_algorithm(self):
        selected_courses = [self.course_list.get(i) for i in self.course_list.curselection()]
        if len(selected_courses) < 2:
            messagebox.showerror("Error", "Please select at least 2 courses.")
        else:
            result = genetic_algorithm(selected_courses)
            self.insert_to_table(result)
            self.next_page_button(result)

if __name__ == "__main__":
    root = tk.Tk()
    app = CourseSchedulerApp(root)
    root.mainloop()