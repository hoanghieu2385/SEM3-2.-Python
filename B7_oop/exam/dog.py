# Clear code previous
import os
os.system("cls")

from animal import Animal

class Dog(Animal):
    def __init__(self, name, speak) -> None:
        super().__init__(name)
        self.speak = speak
    
    def get_speak(self):
        return self.speak
    def set_speak(self, speak):
        self.speak = speak

    def display(self):
        super().display()
        print(f"Sound: {self.speak}")

