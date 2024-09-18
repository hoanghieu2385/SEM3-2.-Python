# Clear code previous
import os
os.system("cls")

def dict_example():
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
    print(f"{person}")
    print(f"Name: {person[0]['name']}")

if __name__ == "__main__":
    dict_example()