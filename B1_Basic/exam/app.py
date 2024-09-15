def array_string():
    arr = ["Hieu", "Tung", "Lam"]
    for i in arr:
        print(f"{i}")

def array_number():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in arr:
        if i % 2 != 0:
            print(f"{i}")
            
def exam_2():
    list=[1,6,8,3,1]
    print(f"Current array list: {list}")
    last_number = int(input("\nEnter a number: "))
    list.append(last_number)
    print(f"New list: {list}")

def exam_3():
    array_list=[1,6,8,3,9]
    print(f"Current array list: {array_list}")
    last_number = int(input("\nEnter a number: "))
    array_list.append(last_number)
    print(f"New list: {array_list}")
    
    # Counting array elements
    print(f"\n1. The count of element: {len(array_list)}")
    
    # Find max number
    max_num = array_list[0]
    for i in range(len(array_list)):
        if array_list[i] >= max_num:
            max_num = array_list[i]
    print(f"\n2. Max number is: {max_num}")
    
    # Find min number
    min_num = array_list[0]
    for i in range(len(array_list)):
        if array_list[i] <= min_num:
            min_num = array_list[i]
    print(f"\n3. Min number is: {min_num}")
    
    # Counting odd number in array list
    total_odd_num = 0
    total_even_num = 0
    for num in array_list:
        if num % 2 == 0:
            total_even_num += num
        else:
            total_odd_num += num
    print(f"\n4. Total of odd numbers is: {total_odd_num}")
    print(f"\n5. Total of even numbers is: {total_even_num}")

def exam_4():
    array_list_1=[1, 6, 8, 3, 9]
    array_list_2=[0, 2, 3, 6, 7]
    arr_3 = []
    
    print(f"Current array list 1: {array_list_1}")
    print(f"Current array list 2: {array_list_2}")
    
    last_number = int(input("\nEnter a number: "))
    array_list_1.append(last_number)
    array_list_2.append(last_number)
    print(f"New list 1: {array_list_1}")
    print(f"New list 2: {array_list_2}")
    
    # Counting array elements
    print(f"\nThe count of element in array list 1: {len(array_list_1)}")
    print(f"\nThe count of element in array list 2: {len(array_list_2)}")
    
    # Find max, min number in 2 array list
    arr_3 = array_list_1 + array_list_2
    print(f"Current array: {arr_3}")
    
    # Find max number
    max_num = arr_3[0]
    for i in range(len(arr_3)):
        if arr_3[i] >= max_num:
            max_num = arr_3[i]
    print(f"\n1. Max number is: {max_num}")
    
    # Find min number
    min_num = arr_3[0]
    for i in range(len(arr_3)):
        if arr_3[i] <= min_num:
            min_num = arr_3[i]
    print(f"\n2. Min number is: {min_num}")
    
    # Find common numbers
    common_num = list(set(array_list_1) & set(array_list_2))
    print(f"\n3. Common numbers: {common_num}")
    
    # Find unique number
    unique_num_1 = list(set(array_list_1) - set(array_list_2))
    print(f"\n4.1 Unique number in array list 1: {unique_num_1}")
    
    unique_num_2 = list(set(array_list_2) - set(array_list_1))
    print(f"\n4.2 Unique number in array list 1: {unique_num_2}")
    
def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Array string")
        print("2. Array number")
        print("3. Input a number to array")
        print("4. Exam 3")
        print("5. Exam 4")
        
        choice = input("Your choice: ")
        if choice == "1":
            array_string()
        elif choice == "2":
            array_string()
        elif choice == "3":
            exam_2()
        elif choice == "4":
            exam_3()
        elif choice == "5":
            exam_4()
        else:
            print("Please choice number again (1-5)")
        
        

if __name__ == "__main__":
    menu()