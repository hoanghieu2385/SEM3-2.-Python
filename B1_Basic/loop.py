print("Hello world")

#Comment

# Create and call back in python

def summary():
    print("\nSummary: phép cộng ")
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: "))
    total = a + b
    print (f"summary 2 numbers: {total}")

def sub():
    print("\nSubtraction: phép trừ ")
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: "))
    total = a - b
    print (f"summary 2 numbers: {total}")

def div():
    print("\nDivision: phép chia ")
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: "))
    total = a / b
    print (f"summary 2 numbers: {total}")

def mul():
    print("\nMultiplication: phép nhân")
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: "))
    total = a * b
    print (f"summary 2 numbers: {total}")

def sum_array():
    total = 0
    for i in range(10):
        total = total + i
        print(f"Summary position: {i} + {total - i} = {total}")
    print(f"\nTotal: {total}")

def loop_for():
    # đếm lùi
    # for i in range(0, 10, -1):
    # đếm tiến và mỗi lần tăng lên 2 đơn vị
    for i in range(0, 10, 2):
        print(f"i = {i}")
    
def loop_while():
    x = 0;
    while x < 10:
        x += 1
        print(f"x = {x}")
    print("End Loop")

def loop_switch_case():
    x = input("Enter a number (1-2-3):")
    
    match x:
        case "1":
            print("One !!!")
        case "2":
            print("Two !!!")
        case "_":
            print("Default !!!")
        
def menu():
    # cach 1: khong dung try catch thi sai cach nay
    # while True:
    #         print("\n===== MENU =====")
    #         print("1. Sum")
    #         print("2. Sub")
    #         print("3. Div")
    #         print("4. Mul")
            
    #         choice = input("Enter choice: ")
    #         if choice == "1":
    #             summary()
    #         elif choice == "2":
    #             sub()
    #         elif choice == "3":
    #             div()
    #         elif choice == "4":
    #             mul()
    #         else:
    #             print("Please enter again!")
    
    # cach 2: try catch
    try:
        while True:
            print("\n===== MENU =====")
            print("1. Sum")
            print("2. Sub")
            print("3. Div")
            print("4. Mul")
            print("5. Sum array")
            print("6. Loop for")
            print("7. Loop while")
            print("8. Loop switch case")
            
            choice = int(input("\nEnter choice: "))
            if choice == 1:
                summary()
            elif choice == 2:
                sub()
            elif choice == 3:
                div()
            elif choice == 4:
                mul()
            elif choice == 5:
                sum_array()
            elif choice == 6:
                loop_for()
            elif choice == 7:
                loop_while()
            elif choice == 8:
                loop_switch_case()
            
            else:
                print("Please enter again!")
                # Ket thuc vong lap neu khac cac choice
                break
    except:
        print("Please choice only number!! ")
if __name__ == "__main__":
    menu()
    