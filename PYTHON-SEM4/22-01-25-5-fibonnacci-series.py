#WAP TO PRINT FIBONNACI SERIES UPTO 50
first=0
second=1
for i in range (50):
    print(first, end = " ")
    
    d=first+second
    first=second
    second=d
