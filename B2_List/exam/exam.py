# Clear code previous
import os
os.system("cls")

from tabulate import tabulate

def exam_1():
    person = [
        {
        "name": "Nguyen Van A",
        "age": 20,
        "address": "Ha Noi"
    },
    {
        "name": "Nguyen Van B",
        "age": 15,
        "address": "Ha Dong"
    }
    ]
    print("Original list of dictionaries:")
    for p in person:
        print(p)

    print("\nImport new person")
    name = input("Name: ")
    age = int(input("Age: "))
    address= input("Address: ")

    new_person = {
        "name": name,
        "age": age,
        "address": address,
    }

    person.append(new_person)

    # Sort the list of dictionaries by age in ascending order
    sorted_person = sorted(person, key=lambda k: k['age'])

    print("\nSorted list of dictionaries by age:")
    for p in sorted_person:
        print(p)

def calculate_score(score_1,score_2):
    final_score = 0.3 * score_1 + 0.7 * score_2
    if final_score < 4.0:
            return 'F'
    elif 4.0 <= final_score < 5.5:
        return 'D'
    elif 5.5 <= final_score < 6.5:
        return 'C'
    elif 6.5 <= final_score < 8.5:
        return 'B'
    else:
        return 'A'

def exam_2():
    students = [
        {
            "STT": 1,
            "Name": "Nguyen Van A",
            "Class": "T2308M",
            "Score 1": 5,
            "Score 2": 7
        },
        {
            "STT": 2,
            "Name": "Nguyen Huu B",
            "Class": "T2308M",
            "Score 1": 7,
            "Score 2": 8
        }
    ]
    print(tabulate(students, headers="keys", tablefmt="grid"))

    for student in students:
        student['Final Score'] = calculate_score(student['Score 1'], student['Score 2'])

    print("\nList of students with final scores:")
    print(tabulate(students, headers="keys", tablefmt="grid"))
    
if __name__ == "__main__":
    exam_1()
