class Myclass:
    a=50

obj=Myclass()
print("obj.a = ",obj.a)

class StudentDetails:
    l=[50,74,63,94,56]
    
    def calculateAverage(self):
        s=0
        for i in self.l:
            s+=i
        s/=len(self.l) 
        return s
    
s=StudentDetails ()
avg=s.calculateAverage()
print("Average marks = ",avg)