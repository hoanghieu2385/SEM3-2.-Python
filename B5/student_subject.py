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

def add_student_subject(id_student, id_subject):
    connection = connect_to_db()
    cursor = connection.cursor()
    query = "INSERT INTO students_subjects (id_student, id_subject) VALUES (%s, %s)"
    values = (id_student, id_subject)
    cursor.execute(query, values)
    connection.commit()
    print(cursor.rowcount, "record inserted.")

def get_students_by_subject(id_subject):
    connection = connect_to_db()
    cursor = connection.cursor()
    query = "SELECT * FROM students WHERE id IN (SELECT id_student FROM students_subjects WHERE id_subject = %s)"
    values = (id_subject,)
    cursor.execute(query, values)
    result = cursor.fetchall()
    for x in result:
        print(x)
        
if __name__ == '__main__':
    # add_student_subject(3, "hoahoc")
    get_students_by_subject("hoahoc")