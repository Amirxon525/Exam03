class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def get_info(self):
        return f"{self.brand},{self.model},{self.year}"

x = Car("BMW","X7","2025")
print(x.get_info())