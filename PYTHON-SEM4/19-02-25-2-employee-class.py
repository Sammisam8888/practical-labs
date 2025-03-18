class Employee:
    def __init__(self, id, name, age, yoe, ctc, tax, cname):
        self.id = id
        self.name = name
        self.age = age
        self.yoe = yoe
        self.ctc = ctc
        self.tax = tax
        self.cname = cname

    def display_details(self):
        print("Employee Details : ")
        print("Employee id : ", self.id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Years of Experience:", self.yoe)
        print("Cost to Company (CTC) : ", self.ctc)
        print("Tax Paying Per year : ", self.tax)
        print("Company name : ", self.cname)

print("Enter the employee details : ")

emp = Employee(input("Enter employee id : "), input("Enter employee name : "), int(input("Enter employee age: ")), int(input("Enter years of experience: ")), 80000, 1200, 'google')
emp.display_details()

