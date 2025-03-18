class Student:
    def __init__(self, rollno, name, branch, regyear, cgpa, passoutyear):
        self.rollno = rollno
        self.name = name
        self.branch = branch
        self.regyear = regyear
        self.cgpa = cgpa
        self.passoutyear = passoutyear
 
    def displaydetails(self):
        print(f"Roll No: {self.rollno}")
        print(f"Name: {self.name}")
        print(f"Branch: {self.branch}")
        print(f"Registration Year: {self.regyear}")
        print(f"CGPA: {self.cgpa}")
        print(f"Passout Year: {self.passoutyear}")

# Example usage
student = Student(1, "John Doe", "CSE", 2018, 9.5, 2022)
student.displaydetails()
