# Clear code previous
import os
os.system("cls")
from tabulate import tabulate

import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "sem3_py"
    )
    
def get_info():
    connection = connect_to_db()
    cursor = connection.cursor()
    
    # Select all students from the database
    select_query = "SELECT `id`, `Name`, `Age`, `Class` FROM students"
    cursor.execute(select_query)
    # Fetch all the rows and print them out in a table format
    students = cursor.fetchall()
    print("Updated students:")
    headers = ["ID", "Name", "Age", "Class"]
    print(tabulate(students, headers=headers))

