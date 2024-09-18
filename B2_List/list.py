def list_example():
    print("List Example")
    list_ex = [1, 3, 4, 7]
    print(f"\nList int: {list_ex}")
    print(f"First number in list: {list_ex[0]}")
    print(f"Second number in list: {list_ex[1]}")
    print(f"Last number: {list_ex[-1]}") # Khuyến khích
    
    list_str = ["Xin chao", "cac ban"]
    print(f"\nList string: {list_str}")
    
    list_mix = ["Xin chao", 2] # Khác biệt với các ngôn ngữ khác
    print(f"\nList mix: {list_mix}")
    
    # For example
def list_example_2():
    list_ex = [1, 3, 6]
    for i in list_ex:
        print(f"Element: {i}")
    
    # While example
def list_example_3():
    list_ex = [45, 92, 62]
    x = 0
    while x < len(list_ex):
        print(f"Element x: {x} = {list_ex[x]}")
        x += 1
        
    # Append example
def list_example_4():
    list_ex = [94, 23, 65]
    print(f"Current list: {list_ex}")
    num = int(input("Enter a number: "))
    list_ex.append(num)
    print(f"New list: {list_ex}")
    for i in list_ex:
        print(f"Element i: {i}")
        
    # Insert example
def list_example_5():
    list_ex = [94, 23, 65]
    print(f"Current list: {list_ex}")
    num = int(input("Enter a number: "))
    list_ex.insert(2, num)
    print(f"\nNew list: {list_ex}")
    for i in list_ex:
        print(f"Element i: {i}")

    # Remove example
def list_example_6():
    list_ex = [94, 23, 65]
    print(f"Current list: {list_ex}")
    list_ex.remove(23)
    print(f"\nNew list: {list_ex}")
    for i in list_ex:
        print(f"Element i: {i}")
    
    # Remove last number example
def list_example_7():
    list_ex = [94, 23, 65]
    print(f"Current list: {list_ex}")
    list_ex.pop(-1)
    print(f"\nNew list: {list_ex}")
    for i in list_ex:
        print(f"Element i: {i}")
        
if __name__ == "__main__":
    list_example_7()