from tkinter import *
from tkinter import ttk


def take_data_to_insert():
    # Initializing the gui and writing the heading
    root = Tk()
    root.title("Enter task")

    # Declaring the variables
    task_name = StringVar()
    status = StringVar()

    frame = ttk.Frame(root, padding=50)
    frame.grid(column=0, sticky=(W,E))

    ttk.Label(frame, text="Task: ").grid(row=0, column=0, sticky=W)
    ttk.Entry(frame, textvariable=task_name).grid(row=0, column=1)

    ttk.Label(frame, text="Status: ").grid(row=1, column=0, sticky=W)
    ttk.Entry(frame, textvariable=status).grid(row=1, column=1)

    return_val = []

    def add_task():
        return_val.append(task_name.get())
        return_val.append(status.get())
        root.quit()
        root.destroy()

    ttk.Button(frame, text="Add Task", command=add_task).grid(column=1, row=3, sticky=W)
    root.mainloop()

    return return_val


def show_values_of_table(table_name, column_titles, table_data):
    root = Tk()
    root.title(f"{table_name}")

    for col in range(3):
        root.grid_columnconfigure(col, minsize=100)

    for i in range(len(column_titles)):
        entry = Entry(relief=GROOVE, width=20, justify='center', background='gray', font=('Courier New', 10))
        entry.grid(row=0, column=i, sticky=NSEW)
        entry.insert(END, column_titles[i])

    rows = []
    for i in range(1, len(table_data)+1):
        cols = []
        for j in range(len(column_titles)):
            entry = Entry(relief=GROOVE, width=20, justify='center')
            entry.grid(row=i, column=j, sticky=NSEW)
            data = table_data[i-1][j]
            entry.insert(END, f"{data}")
            cols.append(entry)

    root.mainloop()
