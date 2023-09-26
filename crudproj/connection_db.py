import mysql.connector

connection = None
config = {
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'database': 'crudpy',
        'raise_on_warnings': True
    }


def get_connection():
    global connection

    if connection is None:
        connection = mysql.connector.connect(**config)

    return connection
