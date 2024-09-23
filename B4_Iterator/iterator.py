import os
os.system("cls")

def iterator_exam():
    numbers = [1, 4, 554, 43]
    numbers_iter = iter(numbers)
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    
def iterator_exam_2():
    numbers = [2, 5, 75, 34, 676]
    numbers_iter = iter(numbers)
    for i in numbers_iter:
        print(f"Loop iterator: {i}")
    
    
if __name__ == "__main__":
    iterator_exam_2()