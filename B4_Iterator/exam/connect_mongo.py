# Clear code previous
import os
os.system("cls")
from tabulate import tabulate

from pymongo import MongoClient

# MongoDB connection
connection_string = "mongodb://localhost:27017/"
try:
    client = MongoClient(connection_string)
    database_name = "test"
    collection_name = "students"

    db = client[database_name]
    collection = db[collection_name]

    if collection is None:
        print("Cannot connect")
    else:
        print("Connected successfully")
except Exception as e:
    print("Error connecting to MongoDB:", e)
    
def add_student():
    try:
        student_name = input("Enter student name: ")
        age = input("Enter student age: ")
        class_name = input("Enter class name: ")

        student_info = {
            "student_name": student_name,
            "age": age,
            "class_name": class_name
        }
        
        collection.insert_one(student_info)
        print("\nStudent added successfully!")
    except Exception as e:
        print(f"Error: {e}")

def updateStudentByID():
    try:
        id_input = input("Enter student ID: ")
        student = collection.find_one({"_id": id_input})
        if student:
            print("\nStudent found:")
            print(f"Name: {student['student_name']}")
            print(f"Age: {student['age']}")
            print(f"Class name: {student['class']['class_name']}")
                
            choice = input("\nDo you want to update this student? (y/n): ")
            if choice.lower() == "y":
                student_name = input("Enter updated student name: ")
                class_id =  input("Enter updated class ID: ")
                class_name = input("Enter updated class name: ")
                collection.update_one({"student_id": id_input}, {"$set": {"student_name": student_name, "class.class_id": class_id, "class.class_name": class_name}})
                print("\nStudent updated successfully!")
        else:
            print("\nStudent not found")
    except Exception as e:
        print(f"Error: {e}")
        
def delete_student():
    try:
        id_input = input("Enter student ID: ")
        collection.delete_one({"student_id": id_input})
        print("\nStudent deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Add new student")
        print("2. Update student with id")
        print("3. Delete student with id")
        
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            updateStudentByID()
        elif choice == "3":
            delete_student()
        else: 
            print("Please enter choice again !!")
    
if __name__ == "__main__":
    menu()