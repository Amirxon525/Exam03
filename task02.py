class student:
    def __init__(self,name,age,nd):
        self.name=name
        self.nd=nd
        self.age=age
    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, studying in {self.nd}nd course."

x = student("Amir","18","2")
print(x.introduce())