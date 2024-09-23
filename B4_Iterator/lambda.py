import os
os.system("cls")

def lambda_exam():
    demo = lambda a, b: a + b
    print(f"Sum a + b = { demo(2,3) }")
    
    # Đề: cho chuỗi và tìm ra số chẵn, lẻ
    # Cách 1:
def odd_numbers():
    numbers = [2, 5, 32, 53, 76]
    print(f"Current list: {numbers}")

    odd_nums = list(filter(lambda x: x%2 != 0, numbers))
    print(f"\nOdd numbers: {odd_nums}")
    
    # Cách 2:
def even_numbers():
    numbers = [2, 5, 32, 53, 76]
    print(f"Current list: {numbers}")
    even_nums = list(filter(lambda x: x%2 == 0, numbers))
    print(f"\nEven numbers: {even_nums}")
    
def exam_1():
    numbers = [0, 32, 54, 9, 52, 28]
    print(f"Current list: {numbers}")
    
    ketqua = list(filter(lambda x: x%3 == 0, numbers))
    print(f"\nSố chia hết cho 3: {ketqua}")

def soft_exam():
    numbers = [0, 32, 54, 9, 52, 28]
    print(f"Current list: {numbers}")
    
    sorted_nums = list(sorted(numbers, key = lambda x:x))
    # Hoặc viết như này cũng được:
    #sorted_nums = list(sorted(numbers))
    print(f"\nSorted numbers: {sorted_nums}")
    
    sorted_nums_reverse = list(sorted(numbers, key = lambda x:x, reverse=True))
    print(f"\nSorted numbers reverse: {sorted_nums_reverse}")

def exam_2():
    numbers = [0, 32, 54, 9, 52, 28]
    print(f"Current list: {numbers}")
    
    sorted_nums = list(sorted(numbers, key = lambda x:x))
    # Hoặc viết như này cũng được:
    #sorted_nums = list(sorted(numbers))
    print(f"\nSorted numbers: {sorted_nums}")
    
    sorted_nums_reverse = list(sorted(numbers, key = lambda x:x, reverse=True))
    print(f"\nSorted numbers reverse: {sorted_nums_reverse}")
    
    while True:
        try:
            new_num = int(input("Enter new number: "))
        except ValueError:
            print("Please enter a integer number!!!! ")
        else:
            break
    numbers.append(new_num)
    print(f"\nNew list: {numbers}")
    tang_dan = list(sorted(numbers, key= lambda x:x))
    print(f"\nTăng dần: {tang_dan}")
    giam_dan = list(sorted(numbers, key= lambda x:x, reverse=True))
    print(f"\nGiảm dần: {giam_dan}")
    
if __name__ == "__main__":
    exam_2()