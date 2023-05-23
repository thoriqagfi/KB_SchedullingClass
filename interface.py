import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ClassScheduling import *

class CourseSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Course Scheduler Informatics Engineering")

        # Komponen GUI
        self.label = tk.Label(root, text="Course List:")
        self.label.pack()

        self.course_list = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self.course_list.pack()

        # Mengatur ukuran course_list agar tidak terlalu besar
        self.course_list.config(width=40, height=20)

        # Mengatur height course_list agar sesuai dengan jumlah course
        self.course_list.config(height=self.course_list.size())

        # Styling pada GUI
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview",
                                background="white",
                                foreground="black",
                                rowheight=25,
                                fieldbackground="white")
        self.style.map("Treeview", background=[("selected", "blue")])  

        self.style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])


        # dictionary courses dari ClassScheduling.py
        self.courses_id_dict = courses_id_dict

        # Penunjuk halaman pada saat output hasil GA
        self.page = 0

        # Memasukkan hasil dictionary ke list
        # yang akan dipilih oleh user
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
        self.tree.column("#0", anchor=tk.CENTER)
        self.tree.column("course name", anchor=tk.CENTER)
        self.tree.column("day", anchor=tk.CENTER)
        self.tree.column("time", anchor=tk.CENTER)
        self.tree.column("#0", width=200)
        self.tree.column("course name", width=400)
        self.tree.column("day", width=200)
        self.tree.column("time", width=200)


        self.next_button = tk.Button(root, text="Next", command=self.next_page)
        self.next_button.pack()

        # Menampilkan nomor halaman
        self.page_label = tk.Label(root, text="Page " + str(self.page + 1))
        self.page_label.pack()

        self.next_button.bind("<Button-1>", lambda event: self.page_label.config(text="Page " + str(self.page + 1)))

        self.page_label.place(x=530, y=504)



    def insert_to_table(self):
        '''
        Metode untuk memasukkan hasil Genetic Algorithm ke dalam
        tabel treeview
        '''
        for i in self.tree.get_children():
            self.tree.delete(i)

    
        self.result[self.page] = dict(sorted(self.result[self.page].items(), key=lambda item: (item[1][0], item[1][1]))) 
       
        for data in self.result[self.page]:
            course = data
            course_name = self.courses_id_dict[data]
            day = self.result[self.page][data][0]
            time = self.result[self.page][data][1]
            # Memasukkan data ke dalam tabel urut sesuai hari dan waktu
            self.tree.insert("", tk.END, text=course, values=(course_name, day, time))


    def next_page(self):
        '''
        Metode untuk menampilkan hasil lain dari Genetic Algorithm
        dengan menggunakan 'page'
        '''
        if self.page < len(self.result) - 1:
            self.page += 1
        else:
            self.page = 0
        self.insert_to_table()

    def start_genetic_algorithm(self):
        '''
        Metode untuk memulai Genetic Algorithm berdasarkan
        pilihan course user
        '''
        selected_courses = [self.course_list.get(i) for i in self.course_list.curselection()]
        if len(selected_courses) < 2:
            messagebox.showerror("Error", "Please select at least 2 courses.")
        else:
            self.result = genetic_algorithm(selected_courses)
            self.insert_to_table()

if __name__ == "__main__":
    root = tk.Tk()
    app = CourseSchedulerApp(root)
    root.mainloop()