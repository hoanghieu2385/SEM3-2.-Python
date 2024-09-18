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

if __name__ == "__main__":
    exam_1()
