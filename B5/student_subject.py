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

def get_all_student():
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

def get_info_student_subject():
    connection = connect_to_db()
    cursor = connection.cursor()

    # Select all records from the students_subjects table
    select_query = """
    SELECT students.id, students.Name, subjects.name
    FROM students
    INNER JOIN students_subjects ON students.id = students_subjects.id_student
    INNER JOIN subjects ON subjects.id = students_subjects.id_subject
    """
    cursor.execute(select_query)

    # Fetch all the rows and print them out in a table format
    records = cursor.fetchall()
    print("Student-Subject relationship:")
    headers = ["Student ID", "Student Name", "Subject Name"]
    print(tabulate(records, headers=headers))

def add_student_subject():
    get_all_student()

    id_student = input("Enter student ID: ")
    id_subject = input("Enter subject ID: ")
    connection = connect_to_db()
    cursor = connection.cursor()
    query = "INSERT INTO students_subjects (id_student, id_subject) VALUES (%s, %s)"
    values = (id_student, id_subject)
    cursor.execute(query, values)
    connection.commit()
    print(cursor.rowcount, "record inserted.")

def get_students_by_subject_id():
    get_info_student_subject()

    subject_name = input("Enter subject id: ")
    connection = connect_to_db()
    cursor = connection.cursor()

    # Select all students who are enrolled in the given subject
    select_query = """
    SELECT students.id, students.Name, students.Age, students.Class
    FROM students
    INNER JOIN students_subjects ON students.id = students_subjects.id_student
    INNER JOIN subjects ON subjects.id = students_subjects.id_subject
    WHERE subjects.id = %s
    """
    values = (subject_name,)
    cursor.execute(select_query, values)

    # Fetch all the rows and print them out in a table format
    students = cursor.fetchall()
    print(f"Students enrolled in {subject_name}:")
    headers = ["ID", "Name", "Age", "Class"]
    print(tabulate(students, headers=headers))

def menu():
    while True:    
        print("\n=== MENU ===")
        print("1. Add student and subject")
        print("2. Get student by subject id")

        choice = input("Enter number your choice: ")
        if choice == "1":
            add_student_subject()
        elif choice == "2":
            get_students_by_subject_id()
        else:
            print("\nPlease enter a valid choice !!!")
if __name__ == '__main__':
    menu()
