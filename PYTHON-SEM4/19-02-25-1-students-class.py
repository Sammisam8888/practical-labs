class Student:
    def __init__(self):
        self.sname=input("Enter Student name : ")
        self.rollno=int(input("Enter Student roll no : "))
        self.regyear=int(input("Enter registration year : "))
        self.passout=int(input("Enter the year of passout :"))
        self.cgpa=float(input("Enter the CGPA : "))
    def display(self):
        print("The Student details are :")
        print("Student Name : ",self.sname)
        print("Student Roll No : ",self.rollno)
        print("CGPA Scored : ",self.cgpa)
        print("Registration year : ",self.regyear)
        print("Passout Year : ",self.passout)
    def __del__(self):
        print("Destructor called, Deleted the object")

s1=Student()
s1.display()

print()
del s1;

print()
print("After deletion, print(s1.sname)")
try :
    print(s1.sname)
except NameError:
    print("Object doesn't exist")