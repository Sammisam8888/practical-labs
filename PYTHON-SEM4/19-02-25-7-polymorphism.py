class Department:
    def __init__(self, name, nofac, nosabove9):
        self.name = name
        self.nofac = nofac
        self.nosabove9 = nosabove9

    def displaydetails(self):
        print(f"Department: {self.name}")
        print(f"Number of Faculties: {self.nofac}")
        print(f"Number of Students with CGPA above 9: {self.nosabove9}")

# Example of polymorphism
def showdetails(entity):
    entity.displaydetails()

# Example usage
csedepartment = Department("CSE", 30, 50)
ecedepartment = Department("ECE", 25, 40)

showdetails(csedepartment)
showdetails(ecedepartment)
