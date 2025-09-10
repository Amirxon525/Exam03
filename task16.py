class car:
    def __init__(self,car,model,year):
         self.car = car 
         self.model = model
         self.year = year
    def get_info(self):
         return f"{self.car},{self.model},{self.year}"
x = car("BMW","X5","2025")
print(x.get_info())