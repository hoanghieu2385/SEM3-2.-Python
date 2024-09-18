def tuple_example():
    print("Tuple example")
    tuple_ex = (1, 6, 4)
    print(f"Tuple: {tuple_ex}")
    
    for i in tuple_ex:
        print(f"Element i: {i}")
    
    tuple_mix = ("Xin chao", 23)
    print(f"Mix: {tuple_mix}")

    # tuple không insert vào được
def tuple_example_2():
    tuple_ex = (8, 4, 7, 4, 6, 1)
    print(f"Count: {tuple_ex.count(4)}")
    
if __name__ == "__main__":
    tuple_example_2()