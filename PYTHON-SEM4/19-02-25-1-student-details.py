class Student:
    def __init__(self, roll_no, name, branch, registration_year, cgpa, passout_year):
        self.roll_no = roll_no
        self.name = name
        self.branch = branch
        self.registration_year = registration_year
        self.cgpa = cgpa
        self.passout_year = passout_year

    def display_details(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Branch: {self.branch}")
        print(f"Registration Year: {self.registration_year}")
        print(f"CGPA: {self.cgpa}")
        print(f"Passout Year: {self.passout_year}")

# Example usage
student = Student(1, "John Doe", "CSE", 2018, 9.5, 2022)
student.display_details()
