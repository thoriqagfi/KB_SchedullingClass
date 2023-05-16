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

        # Komponen GUI
        self.label = tk.Label(root, text="Course List:")
        self.label.pack()

        self.course_list = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.course_list.pack()

        self.courses_id_dict = courses_id_dict

        self.page = 0

        for course_name in self.courses_id_dict.values():
            self.course_list.insert(tk.END, course_name)

        self.start_button = tk.Button(root, text="Start", command=self.start_genetic_algorithm)
        self.start_button.pack()

        # Create a Treeview widget
        self.tree = ttk.Treeview(root)
        self.tree["columns"] = ("course name", "day", "time")
        self.tree.heading("#0", text="Course")
        self.tree.heading("course name", text="Course Name")
        self.tree.heading("day", text="Day")
        self.tree.heading("time", text="Time")
        self.tree.pack()

        self.next_button = tk.Button(root, text="Next")
        self.next_button.pack()

        # Tambahkan pilihan mata kuliah ke dalam Listbox
        # for i in self.data:
        #     self.course_list.insert(tk.END, i['Course'])

    def insert_to_table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        for data in self.result[self.page]:
            course = data
            course_name = self.courses_id_dict[data]
            day = self.result[self.page][data][0]
            time = self.result[self.page][data][1]
            self.tree.insert("", "end", text=course, values=(course_name, day, time))

    def next_page(self):
        if self.page < len(self.result) - 1:
            self.page += 1
        else:
            self.page = 0
        self.insert_to_table()

    def start_genetic_algorithm(self):
        selected_courses = [self.course_list.get(i) for i in self.course_list.curselection()]
        if len(selected_courses) < 2:
            messagebox.showerror("Error", "Please select at least 2 courses.")
        else:
            self.result = genetic_algorithm(selected_courses)
            self.insert_to_table()
            self.next_button.configure(command=self.next_page)

if __name__ == "__main__":
    root = tk.Tk()
    app = CourseSchedulerApp(root)
    root.mainloop()