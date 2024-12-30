class softwareEngineer:
    
    alias = "Keyboard magician"
    
    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    
    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}, salary = {self.salary}"
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.level == other.level
        
        
# instance
se1 = softwareEngineer("Mamon", 32, "Senior", 90000)
se2 = softwareEngineer("Mfdfdon", 23, "Captain", 300000)
se3 = softwareEngineer("Mfdfdon", 23, "Captain", 3000)
print(se1.name, se1.level, se1.alias)
print(se2)
print(se1 == se2)
print(se3 == se2)   