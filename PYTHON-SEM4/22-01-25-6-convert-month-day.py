month=input("Enter the month : ").upper()
print("The number of days in the month are : ",end="")
if month in ["JANUARY","MARCH","MAY","JULY","AUGUST","OCTOBER","DECEMBER"]:
    print("31 days")
elif month in ["APRIL","JUNE","SEPTEMBER","NOVEMBER"]:
    print("30 days")
elif month=="FEBRUARY":
    print("28 or 29 days")