class Employee:
    def __init__(self, id,name, age,yoe,ctc,tax, cname):
        self.id=id
        self.name = name
        self.age = age
        self.yoe=yoe
        self.ctc=ctc
        self.tax=tax
        self.cname=cname

        # (ID, NAME, AGE,YEAR OF EXP, CTC, TAX PAYING PER YEAR, COMPANY NAME)
    def __del__(self):
        #display function as destructor
        print("Employee Details : ")
        print("Employee id : ",self.id)
        print("Name:", self.name)
        print("Cost to Company (CTC) : ",self.ctc)
        print("Tax Paying Per year : ",self.tax)
        print("Company name : ",self.cname)

print("Enter the employee details : ")

emp=Employee(input("Enter employee id : "),input("Enter employee name : "),int(input("Enter employee age")),int(input("Enter employee ")),80000,1200,'google')

