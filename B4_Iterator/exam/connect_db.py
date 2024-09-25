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
    
def add_student():
    get_info()
    
    try:
        name = input("Enter student name: ")
        while True:
            try:
                age = int(input("Enter student age: "))
            except ValueError:
                print("Enter a integer age!!!")
            else:
                break
        class_name = input("Enter class name: ")
        connection = connect_to_db()
        cursor = connection.cursor()
        
        insert_query = "INSERT INTO students (name, age, class) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (name, age, class_name))
        
        connection.commit()
        print(f"Add student {name} !")
        
        connection.close()
    except :
        connection.rollback()
        print(f"Add student FAIL !")
        
    get_info()
    
    connection.close()
    
def edit_student():
    # connection = connect_to_db()
    # cursor = connection.cursor()

    # Select all students from the database
    # select_query = "SELECT `id`, `Name`, `Age`, `Class` FROM students"
    # cursor.execute(select_query)
    
    # students = cursor.fetchall()
    # print("Current students:")
    # for student in students:
    #     print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Class Name: {student[3]}")
        
    get_info()
    
    while True:
        try:
            student_id = int(input("Enter student id: "))
        except ValueError:
            print("Please enter integer id!!!")
        else:
            break
        
    new_name = input("Enter NEW student name: ")
    while True:
        try:
            new_age = int(input("Enter NEW student age: "))
        except ValueError:
            print("Enter a integer age!!!")
        else:
            break
    new_class_name = input("Enter NEW class name: ")
    connection = connect_to_db()
    cursor = connection.cursor()
    
    update_query = "UPDATE `students` SET `Name`= %s,`Age`= %s,`Class`= %s WHERE id = %s"
    cursor.execute(update_query, (new_name, new_age, new_class_name, student_id))
    
    connection.commit()
    print(f"Student with id: {student_id} has been updated!!!")
    
    connection.close()

def delete_student():
    get_info()

    while True:
        try:
            student_id = int(input("Enter student id: "))
        except ValueError:
            print("Please enter integer id!!!")
        else:
            break
    connection = connect_to_db()
    cursor = connection.cursor()

    delete_query = "DELETE FROM students WHERE id = %s"
    # cursor.execute() yêu cầu tham số phải là một tuple, ngay cả khi chỉ có một phần tử.
    # Trong trường hợp chỉ có một giá trị, bạn cần thêm dấu phẩy sau giá trị để biến nó thành tuple
    cursor.execute(delete_query, (student_id,))
    
    connection.commit()
    print(f"Student with id: {student_id} has been deleted!!!")

    get_info()
    
    connection.close()

def find_student():
    try:
        while True:
            try:
                student_id = int(input("Enter student id: "))
            except ValueError:
                print("Please enter integer id!!!")
            else:
                break
        
        connection = connect_to_db()
        cursor = connection.cursor()
        
        select_query = "SELECT `id`, `Name`, `Age`, `Class` FROM students WHERE `id` = %s"
        cursor.execute(select_query, (student_id,))
        
        result = cursor.fetchone()
        if result:
            print(f"\nStudent with id: {student_id} has been found!!!")
            print(f"Name: {result[1]}, Age: {result[2]}, Class: {result[3]}")
        else:
            print(f"\nNo student found with id: {student_id}")
        
        connection.commit()
        print(f"\nStudent with id: {student_id} has found!!!")
        
        connection.close()
    except Exception as e:
        print(f"Error: {e}")
    
def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Add new student")
        print("2. Update student with id")
        print("3. Delete student with id")
        print("4. Find student with id")
        
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            edit_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            find_student()
        else: 
            print("Please enter choice again !!")
    
if __name__ == "__main__":
    menu()