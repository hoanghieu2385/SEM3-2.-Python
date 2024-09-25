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
    
def get_subjects():
    connection = connect_to_db()
    cursor = connection.cursor()
    
    # Select all students from the database
    select_query = "SELECT `id`, `name` FROM subjects"
    cursor.execute(select_query)
    # Fetch all the rows and print them out in a table format
    students = cursor.fetchall()
    print("\n=== Subjects ===:")
    headers = ["ID", "Name"]
    print(tabulate(students, headers=headers))
    
def add_subject():
    get_subjects()
    
    try:
        id = input("Enter subject ID: ")
        name = input("Enter student name: ")
        connection = connect_to_db()
        cursor = connection.cursor()
        
        insert_query = "INSERT INTO students (id, name) VALUES (%s, %s)"
        cursor.execute(insert_query, (id, name))
        
        connection.commit()
        print(f"Add subject: {id} with {name} successful!")
        
        connection.close()
    except :
        connection.rollback()
        print(f"Add subject FAIL !")
        
    get_subjects()
    
    connection.close()

def edit_subject():
    get_subjects()
    
    new_subject_id = int(input("Enter subject id: "))

    new_name = input("Enter NEW subject name: ")

    connection = connect_to_db()
    cursor = connection.cursor()
    
    update_query = "UPDATE `subjects` SET `name`= %s WHERE id = %s"
    cursor.execute(update_query, (new_subject_id, new_name))
    
    connection.commit()
    print(f"Student with id: {new_subject_id} has been updated!!!")
    
    connection.close()

def delete_subject():
    get_subjects()

    new_subject_id = int(input("Enter student id: "))

    connection = connect_to_db()
    cursor = connection.cursor()

    delete_query = "DELETE FROM subjects WHERE id = %s"
    # cursor.execute() yêu cầu tham số phải là một tuple, ngay cả khi chỉ có một phần tử.
    # Trong trường hợp chỉ có một giá trị, bạn cần thêm dấu phẩy sau giá trị để biến nó thành tuple
    cursor.execute(delete_query, (new_subject_id,))
    
    connection.commit()
    print(f"Student with id: {new_subject_id} has been deleted!!!")

    get_subjects()
    
    connection.close()

def menu():
    while True:    
        print("\n=== MENU ===")
        print("1. Add student and subject")
        print("2. Get student by subject id")

        choice = input("Enter number your choice: ")
        if choice == "1":
            add_subject()
        elif choice == "2":
            edit_subject()
        elif choice == "3":
            delete_subject()
        else:
            print("\nPlease enter a valid choice !!!")
if __name__ == '__main__':
    menu()