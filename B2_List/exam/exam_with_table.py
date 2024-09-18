from rich.console import Console
from rich.table import Table
import os
os.system("cls")

def exam_1():
    console = Console()

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

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Name", style="dim", width=12)
    table.add_column("Age")
    table.add_column("Address")

    for p in person:
        table.add_row(p["name"], str(p["age"]), p["address"])

    console.print(table)

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
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Name", style="dim", width=12)
    table.add_column("Age")
    table.add_column("Address")

    for p in sorted_person:
        table.add_row(p["name"], str(p["age"]), p["address"])

    console.print(table)

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
    console = Console()
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
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("STT")
    table.add_column("Name", style="dim", width=12)
    table.add_column("Class")
    table.add_column("Score 1")
    table.add_column("Score 2")
    
    for s in students:
        table.add_row(str(s["STT"]), s["Name"], s["Class"], str(s["Score 1"]), str(s["Score 2"]),)

    console.print(table)

    for student in students:
        student['Final Score'] = calculate_score(student['Score 1'], student['Score 2'])

    print("\nList of students with final scores:")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("STT")
    table.add_column("Name", style="dim", width=12)
    table.add_column("Class")
    table.add_column("Score 1")
    table.add_column("Score 2")
    table.add_column("Final Score")
    
    for s in students:
        table.add_row(str(s["STT"]), s["Name"], s["Class"], str(s["Score 1"]), str(s["Score 2"]), s["Final Score"])

    console.print(table)
if __name__ == "__main__":
    exam_2()
