"""
This module triggers appropriate GUI interface for interacting with the database
"""
from tkinter import Tk, StringVar, Entry, W, E, NSEW, GROOVE, END
from tkinter import ttk


def take_data_to_insert():
    """
    This method take the data from the user through the GUI

    :return: response from the GUI
    """

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
        """
        Method is used to add the response to a list and destroys the root

        :return: None
        """
        return_val.append(task_name.get())
        return_val.append(status.get())
        root.quit()
        root.destroy()

    ttk.Button(frame, text="Add Task", command=add_task).grid(column=1, row=3, sticky=W)
    root.mainloop()

    return return_val


def show_values_of_table(table_name, column_titles, table_data):
    """
    This method is used to show the contents of the table

    :param table_name:
    :param column_titles:
    :param table_data:
    :return:
    """
    root = Tk()
    root.title(f"{table_name}")

    for col in range(3):
        root.grid_columnconfigure(col, minsize=100)

    for i, title in enumerate(column_titles):
        entry = Entry(relief=GROOVE, width=20,
                      justify='center',
                      background='gray',
                      font=('Courier New', 10))
        entry.grid(row=0, column=i, sticky=NSEW)
        entry.insert(END, title)

    for i in range(1, len(table_data)+1):
        cols = []
        for j in range(len(column_titles)):
            entry = Entry(relief=GROOVE,
                          width=20,
                          justify='center')
            entry.grid(row=i, column=j, sticky=NSEW)
            data = table_data[i-1][j]
            entry.insert(END, f"{data}")
            cols.append(entry)

    root.mainloop()
