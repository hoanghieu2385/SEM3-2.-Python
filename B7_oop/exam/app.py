# Clear code previous
import os
os.system("cls")

from cat import Cat
from dog import Dog
from person import Person

if __name__ == '__main__':
    cat = Cat("Mèo tam thể", "Meo fuck")
    cat.display()
    
    print("")
    dog = Dog("Chó phốc", "Gâu Fuck")
    dog.display()
    
    print("")
    person_1 = Person("White man", "What the fcuk")
    person_1.display()
