class Employee:
    def __init__(self, emp_id, name, age, years_of_exp, ctc, tax_per_year, company_name):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.years_of_exp = years_of_exp
        self.ctc = ctc
        self.tax_per_year = tax_per_year
        self.company_name = company_name

    def display_details(self):
        print(f"ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Years of Experience: {self.years_of_exp}")
        print(f"CTC: {self.ctc}")
        print(f"Tax Paying Per Year: {self.tax_per_year}")
        print(f"Company Name: {self.company_name}")

# Example usage
employee = Employee(101, "Alice Smith", 30, 5, 100000, 15000, "TechCorp")
employee.display_details()
