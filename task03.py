class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

d = Dog("Rex")
d.bark() 
print(d.name,)
