class Department:
    def __init__(self, name, num_faculties, num_students_above_9_cgpa):
        self.name = name
        self.num_faculties = num_faculties
        self.num_students_above_9_cgpa = num_students_above_9_cgpa

    def display_details(self):
        print(f"Department: {self.name}")
        print(f"Number of Faculties: {self.num_faculties}")
        print(f"Number of Students with CGPA above 9: {self.num_students_above_9_cgpa}")

# Example of polymorphism
def show_details(entity):
    entity.display_details()

# Example usage
cse_department = Department("CSE", 30, 50)
ece_department = Department("ECE", 25, 40)

show_details(cse_department)
show_details(ece_department)
