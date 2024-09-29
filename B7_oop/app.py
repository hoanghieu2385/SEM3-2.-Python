# Clear code previous
import os
os.system("cls")

from person import Person

from vehicle import Vehicle

if __name__ == '__main__':
    # person = Person("Hieu", 23, "Hanoi")
    # person.walk()
    
    car = Vehicle("BMW", 1234, "BMW", 4)
    car.start()
    car.run()
    car.stop()
    
