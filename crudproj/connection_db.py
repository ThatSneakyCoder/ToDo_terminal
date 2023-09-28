"""
Module sets up connection with the database
"""
import mysql.connector

CONNECTION = None
config = {
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'database': 'crudpy',
        'raise_on_warnings': True
    }


def get_connection():
    """
    This method sets up a connection with the database.

    :return: returns the connection object
    """
    global CONNECTION

    if CONNECTION is None:
        CONNECTION = mysql.connector.connect(**config)

    return CONNECTION
