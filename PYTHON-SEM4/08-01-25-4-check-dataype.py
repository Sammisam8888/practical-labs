#4. Check the data type of user input.

a=input("Enter a value : ")

try:
    a=int(a)
    print(f"The data type of {a} is : ","int")
except:
    try:
        a=float(a)
        print(f"The data type of {a} is : ","float")
    except:
        try:
            a=complex(a)
            print(f"The data type of {a} is : ","complex")
        except:
            print(f"The data type of {a} is : ","string")

            