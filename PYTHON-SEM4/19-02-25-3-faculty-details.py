class Faculty:
    def __init__(self, faculty_id, name, age, teaching_subject, years_of_exp, student_improvement_percentage):
        self.faculty_id = faculty_id
        self.name = name
        self.age = age
        self.teaching_subject = teaching_subject
        self.years_of_exp = years_of_exp
        self.student_improvement_percentage = student_improvement_percentage

    def display_details(self):
        print(f"Faculty ID: {self.faculty_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Teaching Subject: {self.teaching_subject}")
        print(f"Years of Experience: {self.years_of_exp}")
        print(f"Student Improvement Percentage: {self.student_improvement_percentage}")

# Example usage
faculty = Faculty(201, "Dr. John", 45, "Mathematics", 20, 85)
faculty.display_details()
