"""
This module contains the main driver code for static code analysis
"""
import os
import gui_module
from connection_db import get_connection


# Crud: For creating data in the table
def put_data(connection):
    """
    This method inserts data into the database

    :param connection: connection object of DB
    :return: None
    """
    task_name, task_status = gui_module.take_data_to_insert()
    cursor = connection.cursor()
    query = "INSERT INTO checklist (task, status) VALUES(%s,%s)"
    cursor.execute(query, (task_name, task_status))
    connection.commit()


# cRud: For reading data from the table
def get_data(connection):
    """
    This method retrieves data from the database

    :param connection: connection object of DB
    :return: None
    """
    cursor = connection.cursor()
    query = "SELECT * FROM checklist"
    cursor.execute(query)
    table_data = []
    for (task_number, task, status) in cursor:
        table_data.append([task_number, task, status])
    gui_module.show_values_of_table("checklist",
                                    ["Task Number", "Task", "Status"],
                                    table_data)


# cruD: For deleting data from the table
def delete_data(connection):
    """
    This method deletes data from the database

    :param connection: connection object of DB
    :return: None
    """
    id_to_delete = input("Enter id of element to delete")
    cursor = connection.cursor()
    query = "DELETE FROM checklist WHERE (`task_number` = %s)"
    cursor.execute(query, [id_to_delete])
    connection.commit()
    get_data(connection)


# crUd: For updating data of the table
def update_table(connection):
    """
    This method updates values in the table

    :param connection: connection object of DB
    :return: None
    """
    user_input_id = input("Enter id of task")
    user_input_status = input("Enter the new status")
    new_details = [user_input_status, user_input_id]
    cursor = connection.cursor()
    query = ("UPDATE checklist "
             "SET status = %s "
             "WHERE (task_number = %s)")
    cursor.execute(query, new_details)
    connection.commit()
    get_data(connection)


def clear_screen():
    """
    To clear the console

    :return: None
    """
    os.system("clear")


if __name__ == '__main__':
    # set up the connection to the database
    connection_db = get_connection()

    while True:
        option = input("Enter what you want to do: \n"
                       "\t1: INSERT\n"
                       "\t2: SHOW TABLE\n"
                       "\t3: UPDATE TABLE\n"
                       "\t4: DELETE\n"
                       "\te: EXIT THE PROGRAM\n")

        match option:
            case '1':
                clear_screen()
                put_data(connection_db)
            case '2':
                clear_screen()
                get_data(connection_db)
            case '3':
                clear_screen()
                update_table(connection_db)
            case '4':
                clear_screen()
                delete_data(connection_db)
            case 'e':
                clear_screen()
            case default:
                clear_screen()
                print("Incorrect value entered")
                continue

    print("Thank you for using the program")
