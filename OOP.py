



class SoftwareEngineer:

    # class attributes

    alias  = "Keyboard Magician"

    def __init__(self, name, age, level, salary):

        # Instance attributes

        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # İnstance Method

    def code(self):
        print(f"{self.name} is writing code...")

# İnstance
se1 = SoftwareEngineer("Max", 20, "Jumior", 5000)

se1.code()


# Inheritance ( Child and Parent Class)

class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
     


class SoftwareEngineer(Employee):

    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level
    
    def debug(self):
        print(f"{self.name} is debugging")
            

class Designer(Employee):
    pass




se = SoftwareEngineer("Philipp", 27, 5000, "Junior")
se.debug()