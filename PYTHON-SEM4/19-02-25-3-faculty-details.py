class Faculty:
    def __init__(self, fid, name, age, subject, yoe, stdimpperyr):
        self.fid = fid
        self.name = name
        self.age = age
        self.subject = subject
        self.yoe = yoe
        self.stdimpperyr = stdimpperyr

    def displaydetails(self):
        print(f"Faculty ID: {self.fid}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Teaching Subject: {self.subject}")
        print(f"Years of Experience: {self.yoe}")
        print(f"Student Improvement Percentage: {self.stdimpperyr}")

# Example usage
faculty = Faculty(201, "Dr. John", 45, "Mathematics", 20, 85)
faculty.displaydetails()
