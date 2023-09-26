from connection_db import get_connection
import gui_module
import os


# Crud: For creating data in the table
def put_data(connection):
    task_name, task_status = gui_module.take_data_to_insert()
    cursor = connection.cursor()
    query = f"INSERT INTO checklist (task, status) VALUES(%s,%s)"
    cursor.execute(query, (task_name, task_status))
    connection.commit()


# cRud: For reading data from the table
def get_data(connection):
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
    id_to_delete = input(f"Enter id of element to delete")
    cursor = connection.cursor()
    query = f"DELETE FROM checklist WHERE (`task_number` = %s)"
    cursor.execute(query, [id_to_delete])
    get_data(connection)


# crUd: For updating data of the table
def update_table(connection):
    user_input_id = input(f"Enter id of task")
    user_input_status = input(f"Enter the new status")
    new_details = [user_input_status, user_input_id]
    cursor = connection.cursor()
    query = (f"UPDATE checklist "
             f"SET status = %s "
             f"WHERE (task_number = %s)")
    cursor.execute(query, new_details)
    connection.commit()
    get_data(connection)


def clear_screen():
    os.system("clear")


if __name__ == '__main__':
    # set up the connection to the database
    connection_db = get_connection()

    while True:
        option = input(f"Enter what you want to do: \n"
                       f"\t1: INSERT\n"
                       f"\t2: SHOW TABLE\n"
                       f"\t3: UPDATE TABLE\n"
                       f"\t4: DELETE\n"
                       f"\te: EXIT THE PROGRAM\n")

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
                break
            case default:
                clear_screen()
                print("Incorrect value entered")
                continue

    print("Thank you for using the program")
